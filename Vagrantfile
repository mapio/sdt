$script = <<SCRIPT

if ! [ -r /.sdt-provisioned ]; then

export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get -q -y dist-upgrade
apt-get install -y curl python-dev python-setuptools
curl -sL https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
pip install --upgrade distribute
pip install --upgrade pip
pip install mercurial hg-git

cat >/home/vagrant/.hgrc << EOF
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

cat >/home/vagrant/.hgignore << EOF
syntax: glob

*.elc
*.pyc
*~
.DS_Store
EOF

cat >/home/vagrant/.inputrc << EOF
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

chown vagrant:vagrant /home/vagrant/.hg*

su vagrant -c 'hg clone git://github.com/mapio/sdt.git'

touch /.sdt-provisioned

fi

SCRIPT

Vagrant.configure("2") do |config|
  config.vm.define :sdt do |sdt|
    sdt.vm.box = "precise32"
    sdt.vbguest.auto_update = false
    sdt.vm.network :forwarded_port, guest: 8000, host: 8000
    sdt.vm.provision :shell, :inline => $script
  end
end
