# Copyright (c) 2023 Vicharak Computers LLP
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.

import os
import sys
from datetime import date
from sphinxawesome_theme.postprocess import Icons

from docutils import nodes
from docutils.parsers.rst import roles

def bgcolor_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    color, content = text.split(":", 1)
    style = (
        'display: inline-block; '
        'width: 24px; '
        'height: 24px; '
        'line-height: 24px; '
        'text-align: center; '
        'vertical-align: middle; '
        f'background-color: {color.strip()}; '
        'color: white; '
        'font-weight: bold; '
        'font-family: monospace; '
        'font-size: 12px; '
        'margin: 2px; '
        'box-sizing: border-box; '
    )
    node = nodes.raw('', f'<span style="{style}">{content.strip()}</span>', format='html')
    return [node], []

roles.register_canonical_role('bgcolor', bgcolor_role)

sys.path.insert(0, os.path.abspath("_themes"))

# General information about the project.
project = "Vicharak"
author = "Vicharak Computers PVT LTD"
copyright = f"{date.today().year}, {author}"
version = "0.1"

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
exclude_patterns = ["_build", "vicharak_sbcs/axon-lite/axon-lite-linux/linux-development-guide", "vicharak_sbcs/axon-lite/axon-lite-linux/linux-configuration-guide", "vicharak_sbcs/axon-lite/axon-lite-accessories/fan.rst", "vicharak_sbcs/axon-mini/axon-mini-linux/linux-development-guide", "vicharak_sbcs/axon-mini/axon-mini-linux/linux-configuration-guide"]

# HTML settings
html_theme = "sphinxawesome_theme"
html_static_path = ["_static", "_static/images"]
html_title = "Vicharak"
# CSS files to include
html_css_files = [
    "css/fonts.css",
    "css/custom.css",
]
# JS files to include
html_js_files = [
    "js/clarity.js",
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