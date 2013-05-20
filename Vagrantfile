$script = <<SCRIPT

export DEBIAN_FRONTEND=noninteractive

if ! [ -r /.sdt-updated ]; then

	apt-get update
	apt-get -q -y dist-upgrade
	touch /.sdt-updated

fi

if ! [ -r /.sdt-python3 ]; then

	apt-get install -y curl python-dev python-setuptools python3 python3-dev
	touch /.sdt-python3

fi

if ! [ -r /usr/local/bin/hg ]; then

	curl -sL https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
	pip install --upgrade distribute
	pip install --upgrade pip
	pip install mercurial hg-git

fi

if ! [ -r /home/vagrant/.hgrc ]; then

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

fi

if ! [ -r /home/vagrant/.hgignore ]; then

	cat >/home/vagrant/.hgignore <<-EOF
		syntax: glob

		*.elc
		*.pyc
		*~
		.DS_Store
	EOF

	fi

	if ! [ -r /home/vagrant/.inputrc ]; then

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

fi

if ! [ -d /home/vagrant/sdt ]; then
	su - vagrant -c 'hg clone git://github.com/mapio/sdt.git'
else
	su - vagrant -c 'hg -R sdt pull --update'
fi

chown -R vagrant:vagrant /home/vagrant
chmod -R go= /home/vagrant

SCRIPT

Vagrant.configure("2") do |config|
  config.vm.define :sdt do |sdt|
	sdt.vm.box     = "precise32"
	sdt.vm.box_url = "http://files.vagrantup.com/precise32.box"
    sdt.vbguest.auto_update = false
    sdt.vm.network :forwarded_port, guest: 8000, host: 8000
    sdt.vm.provision :shell, :inline => $script
  end
end
