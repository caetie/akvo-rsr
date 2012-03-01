class node::node {

  exec { "download-node":
    cwd => "/opt",
    command => "/usr/bin/wget http://nodejs.org/dist/v0.6.8/node-v0.6.8.tar.gz",
    creates => "/opt/node-v0.6.8.tar.gz",
    require => Class['node::deps'],
  }

  exec { "unpackage-node":
    cwd => "/opt",
    command => "/bin/tar -zxf /opt/node-v0.6.8.tar.gz",
    creates => "/opt/node-v0.6.8",
    require => [Exec["download-node"]],
  }
  
  exec { "configure-node":
    cwd => "/opt/node-v0.6.8",
    command => "/opt/node-v0.6.8/configure",
    # creates => "/usr/local/bin/python2.7",
    require => [Exec["unpackage-node"]],
  }

  exec { "make-node":
    cwd => "/opt/node-v0.6.8",
    command => "make",
    require => [Exec["configure-node"]],
  }

  exec { "install-node":
    cwd => "/opt/node-v0.6.8",
    command => 'checkinstall --install=yes --pkgname=nodejs --pkgversion "0.6.8" --default',
    creates => "/usr/local/bin/node",
    require => [Exec["make-node"]],
  }

}
