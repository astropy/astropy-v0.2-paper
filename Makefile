all: astropy.tex references.bib
	pdflatex astropy.tex
	bibtex astropy.aux
	pdflatex astropy.tex
	pdflatex astropy.tex
