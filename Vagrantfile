# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  # config.vm.boot_mode = :gui
  config.vm.host_name = "akvo.dev"
  config.vm.box_url = "https://dl.dropbox.com/s/dqw9m7mujye0rix/akvo_ubuntu_10.04_64_4.1.8.box?dl=1"
  config.vm.box = "akvo_ubuntu_10.04_64_4.1.8"

  config.vm.network :hostonly, "33.33.33.15"
  config.vm.forward_port 80, 4520
  config.vm.forward_port 3306, 3309

  config.vm.share_folder("v-root", "/var/akvo", ".", :nfs => true)

  config.vm.provision :puppet do |puppet|
     puppet.manifests_path = "scripts/deployment/puppet/manifests"
     puppet.manifest_file  = "base.pp"
     puppet.module_path = "scripts/deployment/puppet/modules"
     puppet.options = "--verbose --debug"
  end
end
