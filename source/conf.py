# Copyright (c) 2023 Vicharak Computers LLP
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.

import os
import sys
import subprocess
from datetime import date
from sphinxawesome_theme.postprocess import Icons

sys.path.insert(0, os.path.abspath("_themes"))

# General information about the project.
project = "Vicharak"
author = "Vicharak Computers PVT LTD"
copyright = f"{date.today().year}, {author}"
version = "0.1"

latex_engine = 'xelatex'  # or 'lualatex'
# Extensions
extensions = [
    "breathe",
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_design",
    "sphinx_favicon",
    "sphinx_togglebutton",
    "sphinxawesome_theme",
    "sphinxcontrib.spelling",
    "sphinx_tabs.tabs",
    "sphinxawesome_theme.highlighting"
    ]

# Spelling extension settings
spelling_ignore_contributor_names = True
spelling_ignore_pypi_package_names = True
spelling_show_suggestions = True
spelling_show_whole_line = True
spelling_word_list_filename = "spelling_wordlist.txt"
spelling_exclude_patterns = ["_build/**"]

# Enable colon fence for code blocks
myst_enable_extensions = [
    "attrs_block",
    # Enable inline attribute parsing
    "attrs_inline",
    # Enable code fences using ::: delimiters
    "colon_fence",
    # Enable definition lists
    "deflist",
    # Enable linkify extension
    "linkify",
    # Automatically convert standard quotations
    # to their opening/closing variants
    "smartquotes",
    # Enable strikethrough
    "strikethrough",
    # Add check-boxes to the start of list items
    "tasklist",
]

# Enable MyST implicit header references
myst_heading_anchors = 4

# Convert MyST titles to header
myst_title_to_header = True

suppress_warnings = ["myst.header", "myst.xref_missing"]

# Source file parsers
source_suffix = [".rst", ".md"]

# Set templates and exclude patterns
templates_path = ["_templates"]
exclude_patterns = ["_build"]

# HTML settings
html_theme = "sphinxawesome_theme"
html_static_path = ["_static", "_static/images"]
html_title = "Vicharak"
# CSS files to include
html_css_files = [
    "css/fonts.css",
    "css/custom.css",
]
# Theme options
html_theme_options = {
    # sphinxawesome_theme options
    "logo_light": "_static/images/vicharak-logo-light.svg",
    "logo_dark": "_static/images/vicharak-logo-dark.svg",
    "show_breadcrumbs": True,
    "show_prev_next": True,
}
# HTML favicon
html_favicon = "_static/images/favicon.ico"
# HTML Permalinks icon
html_permalinks_icon = Icons.permalinks_icon

html_baseurl = "https://docs.vicharak.in/"
html_sidebars = {
  "**": ["sidebar_main_nav_links.html", "sidebar_toc.html"]
}


# LATEX PDF SETUP to support webp image extension
#def convert_webp_to_png(app, docname, source):
#    source_dir = app.srcdir
#    for root, dirs, files in os.walk(source_dir):
#        for file in files:
#            if file.endswith(".webp"):
#                webp_file = os.path.join(root, file)
#                png_file = os.path.splitext(webp_file)[0] + ".png"
#                if not os.path.exists(png_file):  # Avoid re-conversion
#                    subprocess.run(['convert', webp_file, png_file])
#                    print(f"Converted: {webp_file} -> {png_file}")
#
#def setup(app):
#    app.connect('builder-inited', convert_webp_to_png)

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'geometry': r'''
        \usepackage{geometry}
        \geometry{
            top=25mm,       % Top margin: 25mm (~1 inch)
            bottom=25mm,    % Bottom margin: 25mm
            left=15mm,      % Left margin: 30mm (~1.2 inches)
            right=15mm      % Right margin: 30mm
        }
    ''',
    'preamble': r'''
        \usepackage{fontspec}
        \setmainfont{DejaVu Sans}
    '''
}

# Project metadata (already set by sphinx-quickstart)
project = 'Vicharak Documentation Guide'
author = 'Vicharak Computer Pvt Ltd, Surat'
release = '1.11.1.0'

#favicons = [
#    "images/android-chrome-192x192.png",
#    "images/android-chrome-512x512.png",
#    "images/apple-touch-icon.png",
#    "images/favicon-16x16.png",
#    "images/favicon-32x32.png",
#    "images/favicon.ico",
#    "images/mstile-150x150.png",
#    "images/safari-pinned-tab.svg",
#]
