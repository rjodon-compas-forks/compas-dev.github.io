# -*- coding: utf-8 -*-

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

import sphinx_compas_theme

# -- General configuration ------------------------------------------------

templates_path   = ['_templates', ]
source_suffix    = ['.rst', ]
master_doc       = 'index'
project          = 'COMPAS'
copyright        = '2017, Block Research Group - ETH Zurich'
author           = 'Tom Van Mele'
version          = '0.1'
release          = '0.1.0'
language         = None
exclude_patterns = []
pygments_style   = 'sphinx'
show_authors     = True
add_module_names = True


# -- Extension configuration ------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
]

# -- Options for HTML output ----------------------------------------------

html_theme = 'compas'
html_theme_path = sphinx_compas_theme.get_html_theme_path()
html_theme_options = {
    'navbar_active' : 'home',
}
html_context = {}
html_static_path = ['_static']
html_extra_path = ['.nojekyll']
html_last_updated_fmt = ''
html_copy_source = False
html_show_sourcelink = False
html_add_permalinks = ''
html_experimental_html5_writer = True
html_compact_lists = True
