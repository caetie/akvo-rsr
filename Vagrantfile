# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  # config.vm.boot_mode = :gui
  config.vm.box_url = "https://dl.dropbox.com/s/ld90w9x8vc0wxa2/akvo_ubuntu_10.04_64_4.1.8_base.box?dl=1"
  #config.vm.box_url = "https://www.dropbox.com/s/ld90w9x8vc0wxa2/akvo_ubuntu_10.04_64_4.1.8_base.box"
  config.vm.box = "akvo_ubuntu_10.04_64_4.1.8_base"

  config.vm.network "33.33.33.15"
  config.vm.forward_port "http", 80, 4520
  config.vm.forward_port("mysql", 3306, 3309)

  config.vm.share_folder("v-root", "/var/akvo", ".", :nfs => true)
end
