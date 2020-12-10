#!/usr/bin/env bash

# Building a wordcloud based on one year of bulletins

YEAR=$1
cat data/txt/*_${YEAR}_*.txt > ./${YEAR}.txt
py filteringe.py $YEAR
wordcloud_cli --text ./${YEAR}_keywords.txt --imagefile ./${YEAR}.png --width 2000 --height 1000
#display ./${YEAR}.png

