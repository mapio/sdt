#!/bin/bash

export DAIKONDIR=/usr/local/lib/daikon
export JAVA_HOME=/usr/lib/jvm/java-7-oracle/
. $DAIKONDIR/bin/daikon.bashrc

./clean.sh

mkdir bin
javac -g -d bin src/sdt/*.java
java -cp $CLASSPATH:bin daikon.Chicory sdt.Arithmetic >/dev/null 2>&1
java daikon.Daikon Arithmetic.dtrace.gz >/dev/null 2>&1
java daikon.PrintInvariants --ppt-select-pattern sdt.Adder Arithmetic.inv.gz
java -cp $CLASSPATH:bin daikon.tools.jtb.Annotate Arithmetic.inv.gz src/sdt/Adder.java

