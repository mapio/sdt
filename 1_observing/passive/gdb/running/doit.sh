#!/bin/bash

./clean.sh

gcc -g anagrams.c -o anagrams
gdb anagrams

