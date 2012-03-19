class nginx::install {

  exec { "download-nginx":
    cwd => "/opt",
    command => "/usr/bin/wget http://nginx.org/download/nginx-1.0.12.tar.gz",
    creates => "/opt/nginx-1.0.12.tar.gz",
    require => Class['nginx::deps'],
    onlyif => "/bin/sh -c '[ ! -x /usr/local/nginx/sbin/nginx ]'",
  }

  exec { "unpackage-nginx":
    cwd => "/opt",
    command => "/bin/tar -zxf /opt/nginx-1.0.12.tar.gz",
    creates => "/opt/nginx-1.0.12",
    require => [Exec["download-nginx"]],
    onlyif => "/bin/sh -c '[ ! -x /usr/local/nginx/sbin/nginx ]'",
  }
  
  exec { "configure-nginx":
    cwd => "/opt/nginx-1.0.12",
    command => "/opt/nginx-1.0.12/configure",
    require => [Exec["unpackage-nginx"]],
    onlyif => "/bin/sh -c '[ ! -x /usr/local/nginx/sbin/nginx ]'",
  }

  exec { "make-nginx":
    cwd => "/opt/nginx-1.0.12",
    command => "make",
    require => [Exec["configure-nginx"]],
    onlyif => "/bin/sh -c '[ ! -x /usr/local/nginx/sbin/nginx ]'",
  }

  exec { "install-nginx":
    cwd => "/opt/nginx-1.0.12",
    command => 'sudo make install',
    creates => "/usr/local/nginx/sbin/nginx",
    require => [Exec["make-nginx"]],
    onlyif => "/bin/sh -c '[ ! -x /usr/local/nginx/sbin/nginx ]'",
  }

}
