$functions = <<FUNCTIONS
function _fixperms {
	echo "*** Fixing /home/vagrant permissions and ownership" 1>&2
	chown -R vagrant:vagrant /home/vagrant
	chmod -R go= /home/vagrant
}
function _github {
	if ! [ -d /home/vagrant/sdt ]; then
		echo "*** Cloning 'sdt' from GitHub" 1>&2
		su - vagrant -c 'hg clone git://github.com/mapio/sdt.git'
	else
		echo "*** Updating 'sdt' from GitHub" 1>&2
		su - vagrant -c 'hg -R sdt pull --update'
	fi
}
function _provision {
	if [ -r "$2" ]; then
		echo "*** Already provisioned: $1" 1>&2
	elif [ "$(type -t "$1")" == function ]; then
		echo "*** Provisioning: $1" 1>&2
	 	"$1" && touch "$2"
	else
		echo "*** Provisioning (via apt-get): $1" 1>&2
		apt-get -y install "$1" && touch "$2"
	fi
}
function _update {
	if ! [ -r /.sdt-updated-on-$(date +%Y%m%d) ]; then
		apt-get -q -y update
		#apt-get -q -y dist-upgrade
		rm -f /home/vagrant/postinstall.sh /.sdt-updated-on-*
		touch /.sdt-updated-on-$(date +%Y%m%d)
	fi
}
function daikon {
	apt-get install -y unzip
	
	curl -sL http://groups.csail.mit.edu/pag/daikon/download/daikon.zip > /tmp/daikon.zip
	
	cd /usr/local/lib && unzip /tmp/daikon.zip
	chown -R root:root /usr/local/lib/daikon
	
	rm -f /tmp/daikon.zip
	
	
}
function eclipse {
	curl -sL http://mirror.switch.ch/eclipse/technology/epp/downloads/release/juno/SR2/eclipse-java-juno-SR2-linux-gtk.tar.gz > /tmp/eclipse.tgz
	
	cd /usr/local/lib && tar zxvf /tmp/eclipse.tgz
	chown -R root:root /usr/local/lib/eclipse
	
	ln -s /usr/local/lib/eclipse/eclipse /usr/local/bin/
	
	rm /tmp/eclipse.tgz
}
function jars {
	curl -sL https://oss.sonatype.org/content/repositories/releases/org/jolokia/jolokia-jvm/1.1.1/jolokia-jvm-1.1.1-agent.jar > /usr/share/java/jolokia.jar
	curl -sL https://oss.sonatype.org/content/repositories/releases/org/softee/pojo-mbean/1.1/pojo-mbean-1.1.jar > /usr/share/java/pojo-mbean.jar
}
function java7 {
	add-apt-repository -y ppa:webupd8team/java && apt-get -q -y update
	
	echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
	echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections
	
	apt-get -y install libxtst6 oracle-java7-installer
}
function javalanche {
	cd /tmp
	
	curl -sL https://github.com/david-schuler/javalanche/archive/master.zip > javalanche.zip
	
	rm -rf javalanche-master
	unzip javalanche.zip
	cd javalanche-master
	./makeDist.sh
	
	mv javalanche-* /usr/local/lib/javalanche
	chown -R root:root /usr/local/lib/javalanche
}
function jython {
	curl -sL http://search.maven.org/remotecontent?filepath=org/python/jython-installer/2.5.3/jython-installer-2.5.3.jar > /tmp/ji.jar
	
	java -jar /tmp/ji.jar -s -d /usr/lib/jython/2.5.3
	
	rm -f /tmp/ji.jar
	
	if [ -r /usr/lib/jython/2.5.3/bin/jython ]; then
		ln -s /usr/lib/jython/2.5.3/bin/jython /usr/local/bin/
	fi
	
	cat >/home/vagrant/.jython <<-EOF
		python.cachedir=/home/vagrant/.jython-cachedir
	EOF
}
function mercurial {
	pip install mercurial hg-git
	
	cat >/home/vagrant/.hgrc <<-EOF
		[ui]
		username = SDT Student <none@none.com>
		ignore = ~/.hgignore
	
		[web]
		style = gitweb
		allow_archive = gz zip bz2
	
		[hostfingerprints]
		github.com = ce:67:99:25:2c:ac:78:12:7d:94:b5:62:2c:31:c5:16:a6:34:73:53
		bitbucket.org = 24:9c:45:8b:9c:aa:ba:55:4e:01:6d:58:ff:e4:28:7d:2a:14:ae:3b
	
		[extensions]
		graphlog =
		color =
		hggit =
		mq =
		rebase =
		progress =
	EOF
	
	cat >/home/vagrant/.hgignore <<-EOF
		syntax: glob
	
		*.elc
		*.pyc
		*~
		.DS_Store
	EOF
}
function python3 {
	#add-apt-repository -y ppa:fkrull/deadsnakes && apt-get -q -y update
	
	apt-get install -y curl python-dev python-setuptools python3 python3-dev
	
	curl -sL https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
	pip install --upgrade distribute
	pip install --upgrade pip
	pip install virtualenv
}
function userfiles {
	cat >/home/vagrant/.inputrc <<-EOF
		# silence!
		set bell-style none
	
		# be 8 bit clean
		set input-meta on
		set output-meta on
		set convert-meta off
	
		# Mac OSX filenames
		set completion-ignore-case on
	
		# misc
		"\e[3~": delete-char
		"\C-h": backward-delete-char
		"\e[6~": history-search-forward
		"\e[5~": history-search-backward
	
		# python
		Tab: complete
	EOF
	
	cat > /home/vagrant/.bash_aliases <<-EOF
		# SDT aliases
		alias l='/bin/ls -Ghl'
	EOF
	
	mkdir -p /home/vagrant/.pip
	cat > /home/vagrant/.pip/pip.conf <<-EOF
		[global]
		download_cache = ~/.pip/cache
	EOF
	
}
function virtualenvs {
	sudo -iu vagrant virtualenv -p /usr/bin/python2 /home/vagrant/.sdtvenv2
	sudo -iu vagrant virtualenv -p /usr/bin/python3 /home/vagrant/.sdtvenv3
}
FUNCTIONS
$provision = <<PROVISION
# Update the package archive
export DEBIAN_FRONTEND=noninteractive
_update
# Provisioned via apt-get install
_provision ant /usr/bin/ant
_provision gdb /usr/bin/gdb
_provision gnuplot /usr/bin/gnuplot
_provision maven2 /usr/bin/mvn
_provision python-software-properties /usr/bin/add-apt-repository
_provision splint /usr/bin/splint
_provision valgrind /usr/bin/valgrind
_provision wamerican-small /usr/share/dict/words
# Provisioned by a function
_provision python3 /usr/bin/python3
_provision java7 /usr/lib/jvm/java-7-oracle/jre/bin/java
_provision jython /usr/local/bin/jython
_provision mercurial /usr/local/bin/hg
_provision userfiles /home/vagrant/.userfiles
_provision jars /usr/share/java/.sdt-jars
_provision daikon /usr/local/lib/daikon/README.txt
_provision javalanche /usr/local/lib/javalanche/javalanche.xml
_provision virtualenvs /home/vagrant/.sdtvenv
#_provision eclipse /usr/local/bin/eclipse
# Finalizing
_github
_fixperms
PROVISION

Vagrant.configure("2") do |config|
  config.vm.define :sdt do |sdt|
	sdt.vm.box     = "precise32"
	sdt.vm.box_url = "http://files.vagrantup.com/precise32.box"
    sdt.vbguest.auto_update = false
    sdt.vm.network :forwarded_port, guest: 8000, host: 8000
    sdt.vm.network :forwarded_port, guest: 8081, host: 8081
    sdt.vm.provision :shell, :inline => $functions + "\n" + $provision
    sdt.ssh.forward_x11 = true
  end
end
