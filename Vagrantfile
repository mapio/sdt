Vagrant.configure("2") do |config|
  config.vm.define :sdt do |sdt|
	sdt.vm.box     = "precise32"
	sdt.vm.box_url = "http://files.vagrantup.com/precise32.box"
    sdt.vbguest.auto_update = false
    sdt.vm.network :forwarded_port, guest: 8000, host: 8000
    sdt.vm.provision :shell, :path => "provision.sh"
    sdt.ssh.forward_x11 = true
  end
end
