#!/bin/bash

for i in {1..12}; do wget `printf "http://pcgbook.com/wp-content/uploads/chapter%02d.pdf" $i`; done
pdfunite chapter*.pdf ProceduralContentGenerationInGames.pdf
