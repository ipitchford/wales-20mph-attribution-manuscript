#!/usr/bin/env bash
# Build MANUSCRIPT.pdf from MANUSCRIPT.md (pandoc + XeLaTeX, Linux Libertine / Libertinus Math).
set -euo pipefail
cd "$(dirname "$0")"
export PATH="$HOME/Library/TinyTeX/bin/universal-darwin:$PATH"
pandoc MANUSCRIPT.md \
  -f markdown+tex_math_dollars+raw_tex \
  --lua-filter=code-to-path.lua \
  --number-sections \
  -H header.tex \
  -V documentclass=article -V fontsize=11pt -V papersize=a4 \
  -V geometry:margin=2.5cm -V linkcolor=black!70!blue -V urlcolor=black!70!blue -V colorlinks=true \
  --pdf-engine=xelatex -s -o MANUSCRIPT.tex
pandoc MANUSCRIPT.md \
  -f markdown+tex_math_dollars+raw_tex \
  --lua-filter=code-to-path.lua \
  --number-sections \
  -H header.tex \
  -V documentclass=article -V fontsize=11pt -V papersize=a4 \
  -V geometry:margin=2.5cm -V linkcolor=black!70!blue -V urlcolor=black!70!blue -V colorlinks=true \
  --pdf-engine=xelatex -o MANUSCRIPT.pdf
echo "built MANUSCRIPT.pdf"
