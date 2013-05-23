#!/bin/bash

. ~/.sdtvenv3/bin/activate
pip install nose coverage

./clean.sh

export PYTHONPATH=$(pwd)

run() {
	func=$1
	num=$2
	nosetests --with-coverage --cover-package=code test.py:test_${func}_${num}
	coverage html -d report_${func}_${num} --include code.py
}

for num in 0 1 2 3; do
	run path $num
done

for num in 0 1 2; do
	run branch $num
done

python3 -m http.server

