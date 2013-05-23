#!/bin/bash

./clean.sh

ant test

cat target/test-reports/TEST-sdt.TestSuite.txt
