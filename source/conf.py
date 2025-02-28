# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '포트폴리오'
copyright = '2025, Seungju Baek'
author = 'Seungju Baek'
release = '0.11.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []
# extensions.append("sphinx_wagtail_theme")

templates_path = ['_templates']
exclude_patterns = []

language = 'ko'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# html_theme = 'sphinx_wagtail_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

# html_theme_options = dict(
#     project_name = project,
#     logo_alt = "Wagtail",
#     logo_height = 59,
#     logo_url = "/",
#     logo_width = 45,
# )