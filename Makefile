all: astropy.tex references.bib
	latex astropy.tex
	bibtex astropy.aux
	latex astropy.tex
	latex astropy.tex
