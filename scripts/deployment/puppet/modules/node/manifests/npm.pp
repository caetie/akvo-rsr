class node::npm {

  file { "/opt/npm":
    ensure => "directory",
    require => Class['node::node'],
  }
  
  exec { "download-npm":
    cwd => "/opt/npm",
    command => "/usr/bin/wget http://npmjs.org/install.sh",
    creates => "/opt/npm/install.sh",
    require => File['/opt/npm'],
  }

  exec { "install-npm":
    cwd => "/opt/npm",
    command => "sudo sh install.sh",
    creates => "/usr/local/bin/npm",
    require => [Exec["download-npm"]],
  }

}
