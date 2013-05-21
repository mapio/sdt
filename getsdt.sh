#!/bin/bash

if [ -d .hg ] || [ -d .git ]; then
	echo "*** This script can't be run from a git/hg repository."
	exit
fi

if [ -r Vagrantfile ]; then
	echo "*** Removing the previous versions of 'Vagrantfile', 'provision.sh', and 'provision.d'..."
	rm -rf Vagrantfile provision.sh provision.d
fi

echo -n "*** Downloading the required files from GitHub..."
curl -sL https://github.com/mapio/sdt/archive/master.tar.gz | tar --strip 1 --wildcards -zxvf - '*/Vagrantfile' '*/provision.*' >/dev/null 2>&1
echo " done."
echo -e "*** Now, please run the following commands:\n"
echo -e "\tvagrant up\n\tvagrant reload --no-provision\n\tvagrant vbguest --no-provision\n\tvagrant reload\n"
echo "*** Errors during the provisioning are normal, execpt during the invocation of the last command."
