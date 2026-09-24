#!/bin/bash
# Cloud environment setup script for belief-free research sessions.
# Paste into: environment menu (session title bar) -> Edit -> Setup script.
set -e

# Scientific Python stack (analysis, symbolic/exact math, simulations, plots)
pip install -q numpy scipy sympy mpmath matplotlib pandas numba networkx statsmodels jupyter

# LaTeX toolchain for compiling the paper (remove if not needed; adds a few minutes)
apt-get update -qq
apt-get install -y -qq --no-install-recommends \
  texlive-latex-extra texlive-science texlive-fonts-recommended \
  texlive-bibtex-extra biber latexmk pandoc
