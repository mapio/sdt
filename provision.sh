#!/bin/bash

export DEBIAN_FRONTEND=noninteractive

provision() {
	if [ -r "$2" ]; then
		echo "*** Already provisioned: $1" 1>&2
	else
		echo "*** Provisioning: $1" 1>&2
	 	bash "/vagrant/provision.d/$1" && touch "$2"
	 fi
}

provision update 	/.sdt-updated
provision python3	/usr/bin/python3
provision java7 	/usr/lib/jvm/java-7-oracle/jre/bin/java
provision gdb 		/usr/bin/gdb
provision valgrind 	/usr/bin/valgrind
provision jython 	/usr/local/bin/jython
provision mercurial /usr/local/bin/hg
provision bash 		/home/vagrant/.bash_aliases
provision words 	/usr/share/dict/words
provision gnuplot 	/usr/bin/gnuplot
provision jars 		/usr/share/java/.sdt-jars

if ! [ -d /home/vagrant/sdt ]; then
	echo "*** Cloning 'sdt' from GitHub" 1>&2
	su - vagrant -c 'hg clone git://github.com/mapio/sdt.git'
else
	echo "*** Updating 'sdt' from GitHub" 1>&2
	su - vagrant -c 'hg -R sdt pull --update'
fi

echo "*** Fixing /home/vagrant permissions and ownership" 1>&2
chown -R vagrant:vagrant /home/vagrant
chmod -R go= /home/vagrant
