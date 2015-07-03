# * vim: ft=ruby *

require 'yaml'
CONFIG_FILE = 'ansible/group_vars/vagrant.yml'
parms = YAML::load File.open(CONFIG_FILE)

Vagrant.configure("2") do |config|
  config.vm.box     = 'debian'
  config.vm.box_url = 'http://static.gender-api.com/debian-8-jessie-rc2-x64-slim.box'

  config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--memory",  1024]
    v.customize ["modifyvm", :id, "--usb",     "on"]
    v.customize ["modifyvm", :id, "--usbehci", "on"]
  end

  config.vm.synced_folder '.', parms["app_path"]
  config.vm.network :private_network, ip: "192.168.33.70"

  config.vm.provision :ansible do |ansible|
    ansible.playbook = 'ansible/vagrant.yml'
    ansible.inventory_path = 'ansible/hosts'
    ansible.limit = 'vagrant'
    ansible.host_key_checking = false
    ansible.sudo = true
    ansible.extra_vars = { ansible_ssh_user: 'vagrant' }
  end
end
