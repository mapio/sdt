#!/bin/bash

./clean.sh

gcc -g segfault.c -o segfault
ulimit -c $((1024*1024))
./segfault
gdb segfault core

