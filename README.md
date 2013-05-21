Systematic Debugging Techniques
===============================

![CC SA3.0](http://i.creativecommons.org/l/by-sa/3.0/88x31.png)

This repository contains the support material related to the PhD class
[Systematic Debugging Techniques](http://santini.di.unimi.it/d/sdt/) and is
licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US>).

To practice with the provided code requires the installation and configuration
of several software tools; in order to help students in such task, a *virtual
machine* image possible is provided.

To setup such image you'll need to:

* download and install [VirtualBox](https://www.virtualbox.org/), following the [instructions](https://www.virtualbox.org/manual/ch02.html) (there is no need to intsall the *extension pack*);
* download and install [Vagrant](http://www.vagrantup.com/), following the [instructions](http://docs.vagrantup.com/v2/installation/index.html);
* install the [vagrant-vbguest](https://github.com/dotless-de/vagrant-vbguest), by entering at the operating system *shell* prompt: `vagrant plugin install vagrant-vbguest`.

Once a basic Vagrant setup has been reached, move to an empty directory of your choice and give the following command:

```bash
	curl -sL https://raw.github.com/mapio/sdt/master/getsdt.sh | bash
```

and follow the given instructions (the script requires the presence of `curl`, `bash`, and GNU `tar`).

If no errors are encountered, you can connect to the virtual machine with the
command `vagrant ssh`; please note that in the home directory of the guest
(virutal) system you'll find a `sdt` subdirectory containing a *clone* of this
repository and that under `/vagrant` is mounted the directory of the host
system where you have downloaded the file `Vagrantfile` (and run the various
`vagrant` commands).
