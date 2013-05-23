#!/bin/bash

echocol() { echo -e "\033[31m$@...\033[0m " >&2; }

echocol "Installing werkzeug [this example uses Python 2.7]"

. ~/.sdtvenv2/bin/activate
pip install werkzeug

echocol "Running without protection... (perss CTRL-C to proceed to the next example)"

python buggy.py

echocol "Running wrapped by Werkzeug... (perss CTRL-C to proceed to the next example)"

python wrap.py

echocol "Running served by Werkzeug... (perss CTRL-C to proceed to the next example)"

python serve.py
