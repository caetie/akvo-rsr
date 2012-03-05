class nginx::install {

  exec { "download-nginx":
    cwd => "/opt",
    command => "/usr/bin/wget http://nginx.org/download/nginx-1.0.12.tar.gz",
    creates => "/opt/nginx-1.0.12.tar.gz",
    require => Class['nginx::deps'],
  }

  exec { "unpackage-nginx":
    cwd => "/opt",
    command => "/bin/tar -zxf /opt/nginx-1.0.12.tar.gz",
    creates => "/opt/nginx-1.0.12",
    require => [Exec["download-nginx"]],
  }
  
  exec { "configure-nginx":
    cwd => "/opt/nginx-1.0.12",
    command => "/opt/nginx-1.0.12/configure",
    require => [Exec["unpackage-nginx"]],
  }

  exec { "make-nginx":
    cwd => "/opt/nginx-1.0.12",
    command => "make",
    require => [Exec["configure-nginx"]],
  }

  exec { "install-nginx":
    cwd => "/opt/nginx-1.0.12",
    command => 'sudo make install',
    creates => "/usr/local/nginx/sbin/nginx",
    require => [Exec["make-nginx"]],
  }

}
