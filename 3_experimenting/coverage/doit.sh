#!/bin/bash

. ~/.sdtvenv3/bin/activate
pip install nose coverage

./clean.sh

export PYTHONPATH=$(pwd)

coverage run tests.py
coverage html -d report --include code.py
cd report && python -m http.server
