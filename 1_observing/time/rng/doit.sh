#!/bin/bash

javac *.java

java -Xrunhprof:cpu=times,file=slow.txt WhatIsSlow s 100000

sed -n '/^CPU TIME.*BEGIN/,/CPU TIME.*END/ p' < slow.txt  | head -n 10

java -Xrunhprof:cpu=times,file=fast.txt WhatIsSlow f 100000

sed -n '/^CPU TIME.*BEGIN/,/CPU TIME.*END/ p' < fast.txt  | head -n 10

