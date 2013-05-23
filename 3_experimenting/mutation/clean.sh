#!/bin/bash

killall java >/dev/null 2>&1
ant clean
ant -f javalanche.xml -propertyfile javalanche.properties cleanJavalanche
rm -rf /tmp/db-data mutation-files
