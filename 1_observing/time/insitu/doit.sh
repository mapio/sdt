#!/bin/bash

python3 insitu.py > insitu.txt
gnuplot -e "plot 'insitu.txt' using 1:2 with l title 'normal', 'insitu.txt' using 1:3 with l title 'insitu'; pause -1"
