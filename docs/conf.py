"""Sphinx configuration for py-acidbase."""

project = "acidbase"
author = "Michael Steinbaugh"
copyright = "Acid Genomics"
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "numpydoc",
]
autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
}
napoleon_numpy_docstring = True
napoleon_google_docstring = False
numpydoc_show_class_members = False
html_theme = "acidgenomics"
html_theme_path = ["_themes"]
html_title = "acidbase"
html_theme_options = {
    "sitesearch": "python.acidgenomics.com",
    "repo_url": "https://github.com/acidgenomics/py-acidbase",
    "copyright_start_year": "2019",
    "license_name": "Apache 2.0",
    "license_url": "https://www.apache.org/licenses/LICENSE-2.0",
    "license_file_url": "https://github.com/acidgenomics/py-acidbase/blob/main/LICENSE",
}
html_show_sourcelink = False
html_show_sphinx = False
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "pandas": ("https://pandas.pydata.org/docs", None),
}
