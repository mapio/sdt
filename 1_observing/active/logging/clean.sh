#!/bin/bash

rm -f *.log*
find . -depth -name __pycache__ -exec rm -rf {} \;
