#!/bin/bash

echocol() { echo -e "\033[31m$@\033[0m " >&2; }

echocol "No warnings"
gcc -w test.c
echocol "Normal wanings"
gcc test.c
echocol "All warnings"
gcc -Wall test.c

rm -f a.out
