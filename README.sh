pandoc README.md -f markdown -t rst -s -o README.rst.tmp && \
cat README.rst.tmp | \
grep === | \
xargs echo > README.rst && \
cat README.rst.tmp >> README.rst
