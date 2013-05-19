Systematic Debugging Techniques
===============================

Questo repository contiene il materiale di supporto del corso di dottorato
[Systematic Debugging Techniques](http://santini.di.unimi.it/d/sdt/).

Per sperimentare con il codice messo a disposizione è necessario installare e
configurare vari software di supporto; al fine di facilitare gli studenti in
questo compito è possibile adoperare l'immagine di una *macchina virtuale*
appositamente predisposta.

Per farlo è necessario intsallare il seguente software:

* scaricare ed installare [VirtualBox](https://www.virtualbox.org/), seguendo le [apposite istruzioni](https://www.virtualbox.org/manual/ch02.html) (non è necessario installare l'*extension pack*);
* scaricare ed insallare [Vagrant](http://www.vagrantup.com/), seguendo le [apposite istruzioni](http://docs.vagrantup.com/v2/installation/index.html);
* installare il plugin [vagrant-vbguest](https://github.com/dotless-de/vagrant-vbguest) e predisporre l'immagine base `precise32`, per farlo è sufficiente impartire (alla *shell* del sistema operativo) i comandi:

```python
	vagrant box add precise32 http://files.vagrantup.com/precise32.box
	vagrant plugin install vagrant-vbguest
```

Una volta ottenuta in questo modo una installazione base di Vagrant, portatevi
in una directory vuota a vostro piacimento impartite i seguenti comandi:

```bash
	curl -sLO https://raw.gith ub.com/mapio/sdt/master/Vagrantfile
	vagrant up
	vagrant reload
	vagrant vbguest
	vagrant reload
```

dove il primo comando può essere sostituito con qualunque altro modo di salvare in un file di nome
`Vagrantfile` il contenuto all'URL https://raw.github.com/mapio/sdt/master/Vagrantfile.

Se tutto ha funzionato a dovere, impartendo dalla stessa directory il comando
`vagrant ssh` è possibile collegarsi a tale macchina virtuale; osservate che
nella home dell'utente corrente troverete la sottodirectory `sdt` che
costituisce un *clone* di questo repository e che sotto `/vagrant`sarà montata
la directory del sistema ospite dove avete scaricato il file `Vagrantfile` (e
lanciato i vari comandi `vagrant`).
