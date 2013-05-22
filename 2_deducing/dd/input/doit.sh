#!/bin/bash

echocol() { echo -e "\033[31m$@\033[0m " >&2; }

export PYTHONPATH=..:.

echocol "Simplify...\n"

python3 simplify.py

echocol "Isolate...\n"

python3 isolate.py
