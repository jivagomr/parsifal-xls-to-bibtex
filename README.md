A very simple python script to generate bibtex files from xls spreedsheet exported by parsif.al

The script uses pandas xlrd: pip install xlrd pandas

The scripts agroups the bases from spreedsheet column "source" and then generate a .bib file for each base.

The script looks for a 'articles.xls' files at the root of directory, but you can change it at line 3.
