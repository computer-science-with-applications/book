from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx.util.docutils import SphinxDirective
from sphinx.errors import SphinxWarning


class SpecialAdmonition(nodes.Admonition, nodes.Element):
    pass


class SpecialSection(nodes.Element):
    pass


class SpecialDirective(SphinxDirective):

    has_content = True
    optional_arguments = 1
    final_argument_whitespace = True

    def run(self):
        has_content = len(self.content) > 0
        has_title = len(self.arguments) == 1

        if not has_content and has_title:
            return [document.reporter.warning(
                f'Unexpected parameter: {self.arguments[0]}'
            )]

        if not has_content:
            # We're modifying a section (this isn't checked until the
            # visitor function is run)

            node = SpecialSection()
            css_class = f"section-{self.css_class}"
            node['classes'].append(css_class)
            return [node]
        else:
            # We're creating a special admonition

            if has_title:
                title = self.arguments[0]
            else:
                title = self.default_title

            admonition_node = SpecialAdmonition('\n'.join(self.content))
            admonition_node += nodes.title(title, title)
            css_class = f"admonition-{self.css_class}"
            admonition_node['classes'].append(css_class)
            self.state.nested_parse(self.content, self.content_offset, admonition_node)

            return [admonition_node]


class InfoNoteDirective(SpecialDirective):

    default_title = "Note"
    css_class = "info-note"


class TechnicalDetailsDirective(SpecialDirective):

    default_title = "Technical Details"
    css_class = "technical-details"


class CommonPitfallsDirective(SpecialDirective):

    default_title = "Common Pitfalls"
    css_class = "common-pitfalls"


class TipDirective(SpecialDirective):

    default_title = "Tip"
    css_class = "tip"


def visit_special_admonition_node_html(self, node):
    self.visit_admonition(node)


def depart_special_admonition_node_html(self, node):
    self.depart_admonition(node)


def get_admonition_latex_environment(node):
    if "admonition-info-note" in node["classes"]:
        env_type = "note"
    elif "admonition-common-pitfalls" in node["classes"]:
        env_type = "pitfall"
    elif "admonition-technical-details" in node["classes"]:
        env_type = "technical"
    elif "admonition-tip" in node["classes"]:
        env_type = "tip"
    else:
        raise ValueError(f"Node doesn't include valid admonition class (classes: {node['classes']}")

    return env_type


def visit_special_admonition_node_latex(self, node):
    env_type = get_admonition_latex_environment(node)
    self.body.append('\n' + r'\begin{' + env_type + '}')
    self.no_latex_floats += 1


def depart_special_admonition_node_latex(self, node):
    env_type = get_admonition_latex_environment(node)
    self.body.append(r'\end{' + env_type + '}\n')
    self.no_latex_floats -= 1


def visit_special_section_node(self, node):
    pass


def depart_special_section_node(self, node):
    next_node = node.next_node(ascend=True, siblings=True)

    if next_node is None or not isinstance(next_node, nodes.section):
        # TODO: Print an actual Sphinx warning
        print("Section modifier not applied to a section!")
    else:
        next_node['classes'].extend(node['classes'])


def setup(app):
    app.add_node(SpecialAdmonition,
                 html=(visit_special_admonition_node_html, depart_special_admonition_node_html),
                 latex=(visit_special_admonition_node_latex, depart_special_admonition_node_latex))

    app.add_node(SpecialSection,
                 html=(visit_special_section_node, depart_special_section_node),
                 latex=(visit_special_section_node, depart_special_section_node))

    app.add_directive('info-note', InfoNoteDirective)
    app.add_directive('technical-details', TechnicalDetailsDirective)
    app.add_directive('common-pitfalls', CommonPitfallsDirective)
    app.add_directive('tip', TipDirective)

