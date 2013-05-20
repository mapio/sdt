#!/bin/bash

gcc -o anagrams anagrams.c
valgrind --tool=memcheck --leak-check=full --show-reachable=yes ./anagrams
