#!/bin/bash

echocol() { echo -e "\n\033[31m$@\033[0m \n" >&2; }

./clean.sh

echocol "*** Compiling and running tests..."

ant test

echocol "*** Report..."

cat build/reports/TEST-sdt.TestSuite.txt

cd build/reports/junit && python3 -m http.server
