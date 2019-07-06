#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim:syntax=python:sw=4:ts=4:expandtab
import sys,re




END_DOC = """\
\\end{enumerate}
\\end{document}
"""

def main():
    pre = sys.argv[1].split('.',2)[0]
    output_file = open("%s.tex" % pre,'w')

    # First, write the header
    HEADER="""\
\\documentclass[12pt,twocolumn]{article}

\\usepackage{chessboard}

\\usepackage{enumerate}
\\usepackage[top=2cm,nofoot,bottom=1cm,left=1cm,right=1cm]{geometry}
\\usepackage{fancyhdr}
\\usepackage{lastpage}


\\lhead{XXX}
%\\chead{}
\\rhead{}
%\\rhead{SCHOOL NAME}
\\lfoot{}
\\cfoot{}
\\rfoot{Page \\thepage}
\\renewcommand{\\headrulewidth}{0.4pt}
\\renewcommand{\\footrulewidth}{0pt}

%% FONT
%\\usepackage[T1]{fontenc}
%\\usepackage[math]{iwona} %nice font

\\setchessboard{boardfontsize=23pt}

%% OWN command

\\newcommand{\\game}[2]{
    \\item \\begin{tabular}[t]{l}
    \\chessboard[
    setfen= #1,
    mover= #2
    ]
    \\end{tabular}
}


\\begin{document}\\raggedbottom
\\pagestyle{fancy}

\\setcounter{page}{1}
\\pagenumbering{arabic}

\\begin{enumerate}[1.]
"""
	
    HEADER = HEADER.replace('XXX', pre) 
    output_file.write(HEADER)

    expr = re.compile('^\[FEN "([^"]+)"\]')
    for line in open(sys.argv[1]).readlines():
        result = expr.search(line)
        if result:
            results = result.group(1).split(' ')[:2]
            output_file.write("""\game{%s}{%s}\n""" % (results[0], results[1]))

    output_file.write(END_DOC)
    output_file.close()

if __name__ == '__main__':
    main()
