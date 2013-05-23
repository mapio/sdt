#!/bin/bash

export DEBIAN_FRONTEND=noninteractive

provision() {
	if [ -r "$2" ]; then
		echo "*** Already provisioned: $1" 1>&2
	elif [ -r "/vagrant/provision.d/$1" ]; then
		echo "*** Provisioning: $1" 1>&2
	 	bash "/vagrant/provision.d/$1" && touch "$2"
	 else
		echo "*** Provisioning (via apt-get): $1" 1>&2
	 	apt-get -y install "$1" && touch "$2"
	 fi
}

# Provisioned via a script in provision.d

provision update 	/.sdt-updated-on-$(date +%Y%m%d)
provision python3	/usr/bin/python3
provision java7 	/usr/lib/jvm/java-7-oracle/jre/bin/java
provision jython 	/usr/local/bin/jython
provision mercurial /usr/local/bin/hg
provision userfiles /home/vagrant/.userfiles
provision jars 		/usr/share/java/.sdt-jars
provision daikon 	/usr/local/lib/daikon/README.txt
provision javalanche /usr/local/lib/javalanche/javalanche.xml
provision virtualenvs /home/vagrant/.sdtvenv
#provision eclipse 	/usr/local/bin/eclipse

# Provisioned via apt-get install

provision ant /usr/bin/ant
provision gdb /usr/bin/gdb
provision gnuplot /usr/bin/gnuplot
provision maven2 /usr/bin/mvn
provision python-software-properties /usr/bin/add-apt-repository
provision splint /usr/bin/splint
provision valgrind /usr/bin/valgrind
provision wamerican-small /usr/share/dict/words

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
