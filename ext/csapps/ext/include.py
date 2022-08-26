import sys
import os
import os.path
import codecs

from io import StringIO

from six import string_types

import baron
import redbaron

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util.nodes import set_source_info

# From http://code.activestate.com/recipes/577585-universal-eval-to-string-function/
def execute(code, mode, _globals={}, _locals={}):
    fake_stdout = StringIO()
    __stdout = sys.stdout
    sys.stdout = fake_stdout

    try:
        exec(compile(code, "<stdin>", mode=mode), _globals, _locals)
    except:
        sys.stdout = __stdout
        import traceback
        buf = StringIO()
        ei = sys.exc_info()
        l = traceback.format_exception(ei[0], ei[1], ei[2].tb_next, chain=False)
        return "".join(l)
    else:
        sys.stdout = __stdout
        return fake_stdout.getvalue()

def formatting_type(argument):
    return directives.choice(argument, ('interpreter', 'separate'))

# Based on Sphinx's LiteralInclude
class PythonRun(Directive):

    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        'encoding': directives.encoding,
        'tab-width': int,       
        'formatting': formatting_type 
    }

    def read_with_encoding(self, filename, document, codec_info, encoding):
        try:
            with codecs.StreamReaderWriter(open(filename, 'rb'), codec_info[2],
                                           codec_info[3], 'strict') as f:
                content = f.read()
                return content
        except (IOError, OSError):
            return [document.reporter.warning(
                'Include file %r not found or reading it failed' % filename,
                line=self.lineno)]
        except UnicodeError:
            return [document.reporter.warning(
                'Encoding %r used for reading included file %r seems to '
                'be wrong, try giving an :encoding: option' %
                (encoding, filename))]        
                    
    def run(self):
        has_content = len(self.content) > 0
        has_file = len(self.arguments) == 1
        
        if has_content and has_file:
            return [document.reporter.warning(
                'python-run must have either a file parameter or code content, but not both'
                )]        
         
        document = self.state.document
        if has_file and not document.settings.file_insertion_enabled:
            return [document.reporter.warning('File insertion disabled',
                                              line=self.lineno)]
        env = document.settings.env
        
        
        doc_directory = os.path.dirname(env.doc2path(env.docname))
        sys.path.append(doc_directory)

        old_cwd = os.getcwd()
        os.chdir(doc_directory)

        
        formatting = self.options.get('formatting', 'interpreter')
        
        if has_file:
            rel_filename, filename = env.relfn2path(self.arguments[0])
        
            encoding = self.options.get('encoding', env.config.source_encoding)
            codec_info = codecs.lookup(encoding)
    
            content = self.read_with_encoding(filename, document, codec_info, encoding)
            if content and not isinstance(content, string_types):
                return content        

            env.note_dependency(rel_filename)
            
            source = filename
        elif has_content:
            content = "\n".join(self.content)
            source = None
        
        if not hasattr(env, 'python_state'):
            env.python_state = {}
            
        if not env.docname in env.python_state:
            env.python_state[env.docname] = {}
            env.python_state[env.docname]["globals"] = {}
            env.python_state[env.docname]["locals"] = {} # <- Not clear if this is necessary
        
        python_state = env.python_state[env.docname]

        rv = []
               
        if formatting == "interpreter":
            executed_lines = []
    
            try:
                fst = redbaron.RedBaron(content)
                for statement in fst.filtered():
                    statement_str = statement.dumps()
                    statement_lines = statement_str.split("\n")
                    executed_lines.append(">>> {}\n".format(statement_lines[0]))
                    for l in statement_lines[1:]:
                        executed_lines.append("... {}\n".format(l))
                    
                    res = execute(statement_str, "single", python_state["globals"], python_state["globals"])
                    executed_lines.append(res)
            
                text = ''.join(executed_lines)
                if self.options.get('tab-width'):
                    text = text.expandtabs(self.options['tab-width'])
                retnode = nodes.literal_block(text, text, source=source)
                set_source_info(self, retnode)
                
                self.add_name(retnode)
                
                rv = [retnode]
            except baron.parser.ParsingError as pe:
                rv = [document.reporter.warning(
                    'Could not parse this code:\n' + content
                    )]
            except Exception as e:
                rv = [document.reporter.warning(
                    'Unexpected exception {} while parsing:\n{}'.format(str(e), content)
                    )]
                
        elif formatting == "separate":
            output = execute(content, "exec", python_state["globals"], python_state["globals"])
            
            codenode = nodes.literal_block(content, content, source=source)
            set_source_info(self, codenode)
            self.add_name(codenode)
            
            if len(output) > 0:
                outputnode = nodes.literal_block(output, output)
                outputnode["language"] = "none"
                
                set_source_info(self, outputnode)
                
                self.add_name(outputnode)
                
                rv = [codenode, outputnode]
            else:
                rv = [codenode]
        
        sys.path.remove(doc_directory)
        os.chdir(old_cwd)
                
        return rv         
        

def purge_doc_state(app, env, docname):
    if not hasattr(env, 'python_state'):
        return
    env.python_state.pop(docname, None)

def purge_all_state(app, doctree):
    if not hasattr(app.env, 'python_state'):
        return
    app.env.python_state.clear()


def setup(app):
    app.add_directive('python-run', PythonRun)
    app.connect('env-purge-doc', purge_doc_state)
    app.connect('doctree-read', purge_all_state)

