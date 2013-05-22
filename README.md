Systematic Debugging Techniques
===============================

![CC SA3.0](http://i.creativecommons.org/l/by-sa/3.0/88x31.png)

This repository contains the support material related to the PhD class
[Systematic Debugging Techniques](http://santini.di.unimi.it/d/sdt/) and is
licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/deed.en_US>).

To practice with the provided code requires the installation and configuration
of several software tools; in order to help students in such task, a *virtual
machine* image possible is provided.

To setup such image on your *host* operating system you'll need to:

* download and install [VirtualBox](https://www.virtualbox.org/), following the [instructions](https://www.virtualbox.org/manual/ch02.html) (there is no need to intsall the *extension pack*);
* download and install [Vagrant](http://www.vagrantup.com/), following the [instructions](http://docs.vagrantup.com/v2/installation/index.html);
* install the [vagrant-vbguest](https://github.com/dotless-de/vagrant-vbguest), by entering at the host *shell* prompt: `vagrant plugin install vagrant-vbguest`.

Once such a basic Vagrant setup has been reached, move to an *empty directory*
on the host filesystem and issue the command:

```bash
	curl -sL http://git.io/getsdt.sh | bash
```

and follow the given instructions (to run this script, you must have `curl`,
`bash`, and GNU `tar` installed on the host). You can run again the above
command in the same directory to *update* the virtual machine.

If no errors are encountered, you can connect to the virtual machine with the
command `vagrant ssh`; please note that in the home directory of the *guest*
system you'll find a `sdt` subdirectory containing a *clone* of this
repository and that under the guest directory `/vagrant` is mounted the
directory of the host where you have run the above installation command.
