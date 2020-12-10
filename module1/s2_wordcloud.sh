#!/usr/bin/env bash

# Building a wordcloud based on one year of bulletins

YEAR= $1
echo ${YEAR}
cat data/txt/*_${YEAR}_*.txt > module3/${YEAR}.txt
python module3/filtering.py $YEAR
wordcloud_cli --text module3/${YEAR}_keywords.txt --imagefile module3/${YEAR}.png --width 2000 --height 1000
display module3/${YEAR}.png
