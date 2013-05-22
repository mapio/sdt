#!/bin/bash

rm adder adder.c
cp orig.c adder.c

while (( "$#" )); do
	num=$1
	patch adder.c patch.$num
	shift
done

make adder
./adder
