#!/bin/bash

echocol() { echo -e "\033[31m$@...\033[0m " >&2; }

cleanup() {
	echocol "Stopping the Jolokia agent"
	java -jar jolokia.jar stop $loop

	echocol "Stopping the very trivial Loop.java class"
	kill $loop

	echocol "Stopping the web server for ./html dir"
	kill $http
}

if ! [ -r  jolokia.jar ]; then
	echocol "Getting the jolokia.jar"
	curl -sL http://labs.consol.de/maven/repository/org/jolokia/jolokia-jvm/1.1.1/jolokia-jvm-1.1.1-agent.jar > jolokia.jar
fi

echocol "Start the very trivial Loop.java class"
javac Loop.java
java Loop > /dev/null & loop=$!

echocol "Start the Jolokia agent"
java -jar jolokia.jar --port 8081 --host 0.0.0.0 start $loop

echocol "Starting a web server for ./html dir"
cd html
python -m SimpleHTTPServer & http=$!
cd ..

echocol "Please point your brower to 'http://127.0.0.1/8000' when\n\t'Serving HTTP on 0.0.0.0 port 8000 ...'\nappears on the next line; hit ctrl-c when done"

trap cleanup SIGINT
wait $http
