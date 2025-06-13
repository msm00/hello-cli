"""Sphinx configuration."""
project = "hcli"
author = "Milan Smid"
copyright = "2025, Milan Smid"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
