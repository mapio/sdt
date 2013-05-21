#!/bin/bash

if [ -r Vagrantfilex ]; then
	echo "I found a 'Vagrantfile', please run this command from an empty directory"
	exit
fi

echo -n "*** Downloading the required files from GitHub..."
#curl -sL https://github.com/mapio/sdt/archive/master.tar.gz | tar --strip 1 --wildcards -zxvf - '*/Vagrantfile' '*/provision.*' >/dev/null 2>&1
echo " done."
echo -e "*** Now, please run the following commands:\n"
echo -e "\tvagrant up\n\tvagrant reload --no-provision\n\tvagrant vbguest --no-provision\n\tvagrant reload\n"
echo "*** Errors during the provisioning are normal, execpt during the invocation of the last command."
