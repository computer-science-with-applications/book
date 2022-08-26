# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../ext'))


# -- Project information -----------------------------------------------------

project = 'Computer Science with Applications'
copyright = '2021, Anne Rogers and Borja Sotomayor'
author = 'Anne Rogers and Borja Sotomayor'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'csapps.ext.include',
    'csapps.ext.special',

]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

todo_include_todos = False

# Add custom CSS file

def setup(app):
    app.add_css_file("csapps.css")

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
     'papersize': 'letterpaper',
     # The font size ('10pt', '11pt' or '12pt').
     #
     # 'pointsize': '10pt',

     # Additional stuff for the LaTeX preamble.
     #
     'preamble': r"""
\usepackage{pmboxdraw}
\usepackage{awesomebox}
\usepackage{fontawesome}
\usepackage{newunicodechar}

\newunicodechar{🤔}{\includegraphics[height=\fontcharht\font`X]{emoji.pdf}}

\setcounter{tocdepth}{0}

\definecolor{notecolor}{HTML}{6AB0DE}
\definecolor{pitfallcolor}{HTML}{F0B37E}
\definecolor{technicalcolor}{HTML}{1ABC9C}
\definecolor{tipcolor}{HTML}{A91CCE}

\newenvironment{note}[1]%
{\begin{awesomeblock}[notecolor]{2pt}{\faInfoCircle}{notecolor}\textbf{#1}\setlength{\parskip}{1ex}}%
{\end{awesomeblock}}

\newenvironment{pitfall}[1]%
{\begin{awesomeblock}[pitfallcolor]{2pt}{\faBug}{pitfallcolor}\textbf{#1}\setlength{\parskip}{1ex}}%
{\end{awesomeblock}}

\newenvironment{technical}[1]%
{\begin{awesomeblock}[technicalcolor]{2pt}{\faCogs}{technicalcolor}\textbf{#1}\setlength{\parskip}{1ex}}%
{\end{awesomeblock}}

\newenvironment{tip}[1]%
{\begin{awesomeblock}[tipcolor]{2pt}{\faHandORight}{tipcolor}\textbf{#1}\setlength{\parskip}{1ex}}%
{\end{awesomeblock}}
""",

     # Latex figure (float) alignment
     #
     # 'figure_align': 'htbp',

     'releasename': ''
}

latex_toplevel_sectioning = 'part'

latex_additional_files = ['getting_started/basics/emoji.pdf']

latex_documents = [
    ('index', 'computersciencewithapplications.tex', project, author, 'scrbook')
]
