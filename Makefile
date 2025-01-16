# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile gettext html-all

# 生成翻译模板
gettext:
	$(SPHINXBUILD) -b gettext $(SOURCEDIR) $(BUILDDIR)/gettext
	sphinx-intl update -p $(BUILDDIR)/gettext -l zh_CN

# 构建多语言文档 
html-all:
	# English
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)/html/en
	# Chinese
	$(SPHINXBUILD) -b html -D language=zh_CN $(SOURCEDIR) $(BUILDDIR)/html/zh_CN

# 实时预览
livehtml:
	sphinx-autobuild source build/html/en

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
