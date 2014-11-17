R = viewdep-paper
STY = TexInputs/egpubl.cls
FIG = images/*.pdf images/*.eps images/*.tex

pdf: ms-thesis.pdf

$(R).bbl: $(R).bib
	pdflatex $(R)
	bibtex $(R)
	pdflatex $(R)

ms-thesis.bbl: $(R).bib
	cp -f $(R).bib ms-thesis.bib
	pdflatex ms-thesis
	bibtex ms-thesis
	pdflatex ms-thesis

ms-thesis.pdf: *.tex $(STY) $(FIG) ms-thesis.bbl
	pdflatex ms-thesis
	pdflatex ms-thesis

clean:
	rm -f $(R).log $(R).aux $(R).bbl $(R).blg $(R).out
	rm -f ms-thesis.log ms-thesis.aux ms-thesis.bbl ms-thesis.blg ms-thesis.out
