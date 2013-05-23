#! /bin/bash

echocol() { echo -e "\n\033[31m$@\033[0m \n" >&2; }

echocol "*** Cleanup previous runs..."

./clean.sh
mkdir /tmp/db-data

echocol "*** Compile the project and run the tests..."

ant test

echocol "*** Setup the Javalanche db (errors are normal during the first run)..."

ant -f javalanche.xml -propertyfile javalanche.properties startHsql
ant -f javalanche.xml -propertyfile javalanche.properties schemaexport
ant -f javalanche.xml -propertyfile javalanche.properties startHsql
ant -f javalanche.xml -propertyfile javalanche.properties schemaexport

echocol "*** See if Javalanche can find the tests..."

ant -f javalanche.xml -propertyfile javalanche.properties testTask1

echocol "*** Check if the tests are independent of execution frequency and execution order..."

ant -f javalanche.xml -propertyfile javalanche.properties testTask2
ant -f javalanche.xml -propertyfile javalanche.properties testTask3

echocol "*** Scan the project to look for mutable files..."

ant -f javalanche.xml -propertyfile javalanche.properties scanProject

echocol "*** Fix the exclusion list..."

cat > ./mutation-files/exclude.txt <<-EOF
	# triangle.Triangle
	triangle.TriangleType
	triangle.tests.Triangle1Test
	triangle.tests.Triangle2Test
	triangle.tests.Triangle3Test
	triangle.tests.TriangleTestSuite
EOF

echocol "*** Scan for mutations..."

ant -f javalanche.xml -propertyfile javalanche.properties scan

echocol "*** Prepare and run mutations..."

ant -f javalanche.xml -propertyfile javalanche.properties createTasks
ant -f javalanche.xml -propertyfile javalanche.properties runMutations

echocol "*** Summarize the results..."

ant -f javalanche.xml -propertyfile javalanche.properties analyzeResults
