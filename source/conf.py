import os


__version__ = "0.1"
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "agentos"
copyright = "agentos Developers"
author = "support@weilan.com"
release = __version__
version = __version__


# -- Internationalization -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#internationalization

locale_dirs = ['locale/']   # 翻译文件的路径
gettext_compact = False     # 每个文件单独生成 pot 文件
gettext_uuid = True        # 添加唯一的消息标识符
gettext_location = True    # 添加源文件位置信息
gettext_auto_build = True  # 自动构建翻译文件

language = 'zh_CN'         # 默认语言
languages = [
    ('en', 'English'),
    ('zh_CN', '简体中文'),
]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "myst_parser",
    "sphinx_subfigure",
    "sphinxcontrib.video",
    "sphinx_togglebutton",
    "sphinx_design"
]

# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = ["colon_fence", "dollarmath"]
# https://github.com/executablebooks/MyST-Parser/issues/519#issuecomment-1037239655
myst_heading_anchors = 4

templates_path = ["_templates"]
# exclude_patterns = ["user_guide/reference/_autosummary/*"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_logo = "_static/html_logo.png"
html_favicon = "_static/alphadog.png"

json_url = "_static/version_switcher.json"
version_match = os.environ.get("READTHEDOCS_VERSION")
if version_match is None:
    version_match = "v" + __version__
html_theme_options = {
    "show_nav_level": 2,
    "use_edit_page_button": True,
    "logo": {
        "image_dark": "_static/html_logo_white.png",
    },
    "navbar_center": ["version-switcher", "navbar-nav"],
    "show_version_warning_banner": False,
    "switcher": {
        "json_url": json_url,
        "version_match": version_match,
    },
}

html_context = {
    "display_github": True,
    "github_user": "00make",
    "github_repo": "agentos",
    "github_version": "main",
    "conf_py_path": "/source/",
    "doc_path": "/source"
}
html_css_files = [
    'css/custom.css',
]
html_static_path = ['_static']

### Autodoc configurations ###
autodoc_typehints = "signature"
autodoc_typehints_description_target = "all"
autodoc_default_flags = ['members', 'show-inheritance', 'undoc-members']
autodoc_member_order = "bysource"
autosummary_generate = True
