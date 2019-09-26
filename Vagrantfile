# -*- mode: ruby -*-
# vi: set ft=ruby :

BOX0_IP = "192.168.56.100"
BOX1_IP = "192.168.56.101"
BOX2_IP = "192.168.56.102"
DOMAIN = "example.com"
PRIVATE_KEY = "~/.ssh/id_rsa"
PUBLIC_KEY = '~/.ssh/id_rsa.pub'

Vagrant.configure("2") do |config|
  config.vm.define "graylogg" do |s0|
    s0.vm.box = "centos/7"
    s0.vm.hostname = 'graylogg' + '.' + DOMAIN
    s0.vm.network :private_network, ip: BOX0_IP
    s0.vm.synced_folder '.', '/vagrant', disabled: true
    s0.ssh.insert_key = false
    s0.ssh.private_key_path = [PRIVATE_KEY, "~/.vagrant.d/insecure_private_key"]
    s0.vm.provision "file", source: PUBLIC_KEY, destination: "~/.ssh/authorized_keys"
    s0.vm.provision "shell", inline: <<-SHELL
    ln -s /usr/share/terminfo/r/rxvt-256color /usr/share/terminfo/r/rxvt-unicode-256color
    SHELL
    
    s0.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"
      vb.cpus = "2"
   end
  end

  config.vm.define "s1" do |s1|
    s1.vm.box = "centos/7"
    s1.vm.hostname = "s1.example.com"
    s1.vm.synced_folder ".", "/vagrant", id: "vagrant-root", disabled: true
    s1.vm.network :private_network, ip: BOX1_IP
    s1.vm.provision "ansible" do |ansible|
    ansible.playbook = "sidecar_playbook.yml"
  end
    s1.vm.provider :virtualbox do |vb|
      vb.memory = "1024"
    end
  end

  config.vm.define "s2" do |s2|
    s2.vm.box = "centos/7"
    s2.vm.hostname = "s2.example.com"
    s2.vm.synced_folder ".", "/vagrant", id: "vagrant-root", disabled: true
    s2.vm.network :private_network, ip: BOX2_IP
    s2.vm.provision "ansible" do |ansible|
    ansible.playbook = "sidecar_playbook.yml"
  end
    s2.vm.provider :virtualbox do |vb|
      vb.memory = "1024"
    end
  end

end
