Systematic Debugging Techniques
===============================

This repository contains the support material related to the PhD class
[Systematic Debugging Techniques](http://santini.di.unimi.it/d/sdt/).

To practice with the provided code requires the installation and configuration
of several software tools; in order to help students in such task, a *virtual
machine* image possible is provided.

To setup such image you'll need to:

* download and install [VirtualBox](https://www.virtualbox.org/), following the [instructions](https://www.virtualbox.org/manual/ch02.html) (there is no need to intsall the *extension pack*);
* download and install [Vagrant](http://www.vagrantup.com/), following the [instructions](http://docs.vagrantup.com/v2/installation/index.html);
* install the [vagrant-vbguest](https://github.com/dotless-de/vagrant-vbguest), by entering (at the operating system *shell* prompt) the command `vagrant plugin install vagrant-vbguest`.

Once a basic Vagrant setup has been reached, move to an empty directory of your choice and give the following commands:

```bash
	curl -sLO https://raw.github.com/mapio/sdt/master/Vagrantfile
	vagrant up
	vagrant reload
	vagrant vbguest
	vagrant reload
```

where the first command can be replaced by any other methof of saving in a file named
`Vagrantfile` the content at URL https://raw.github.com/mapio/sdt/master/Vagrantfile.

If non errors are encountered, you can connect to the virtual machine with the
command `vagrant ssh`; please not that in the home directory of the guest
(virutal) system you'll find a `sdt` subdirectory containing a *clone* of this
repository and that under `/vagrant` is mounted the directory of the host
system where you have downloaded the file `Vagrantfile` (and run the various
`vagrant` commands).
