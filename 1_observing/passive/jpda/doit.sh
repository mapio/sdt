#!/bin/bash

export CLASSPATH=./classes:/usr/lib/jvm/java-7-oracle/lib/tools.jar

./clean.sh

mkdir classes
javac -d classes ThreadTest.java

java -agentlib:jdwp=transport=dt_socket,server=y,address=8000,suspend=n ThreadTest 1 10 >/dev/null 2>&1 &

jython monitor.jy


