# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = src
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile autobuild

setup:
	git lfs checkout
	git lfs pull
	unzip examples/working_with_data/pandas/tree-census-data.zip -d src/working_with_data/pandas

autobuild:
	@sphinx-autobuild src/ _build/html -b html

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# DEPLOYING TO GITHUB PAGES
#
# If a gh-pages branch does not already exist, it can be created
# like this:
#
#   git checkout --orphan gh-pages
#   git reset --hard
#   git commit --allow-empty -m "Initializing gh-pages branch"
#   git push origin gh-pages
#   git checkout main
#
# The above steps only need to be carried out once (ever). The
# following steps need to be done every time you create a new
# clone of the repository, and want to be able to deploy from it:
#
#   make clean
#   git worktree add -B gh-pages _build/html origin/gh-pages
#
# This associates the gh-pages branch with the _build/html directory.
# So, anything we put there, will be pushed to the gh-pages branch.

deploy:
	echo gitdir: $(shell pwd)/.git/worktrees/html > $(BUILDDIR)/html/.git
	echo book.cs-apps.org > $(BUILDDIR)/html/CNAME
	cp $(BUILDDIR)/latex/computersciencewithapplications.pdf $(BUILDDIR)/html/cs-apps-book.pdf
	git --work-tree=$(BUILDDIR)/html/ --git-dir=$(BUILDDIR)/html/.git add -A .
	git --work-tree=$(BUILDDIR)/html/ --git-dir=$(BUILDDIR)/html/.git commit -m"Updated website"
	git --work-tree=$(BUILDDIR)/html/ --git-dir=$(BUILDDIR)/html/.git push origin gh-pages
