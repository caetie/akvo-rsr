class python::python {

  exec { "download-python":
    cwd => "/opt",
    command => "/usr/bin/wget http://python.org/ftp/python/2.7.2/Python-2.7.2.tgz",
    creates => "/opt/Python-2.7.2.tgz",
    require => Class['python::deps'],
  }

  exec { "unpackage-python":
    cwd => "/opt",
    command => "/bin/tar -xvf /opt/Python-2.7.2.tgz",
    creates => "/opt/Python-2.7.2",
    require => [Exec["download-python"]],
  }
  
  exec { "install-python":
    cwd => "/opt/Python-2.7.2",
    command => "/opt/Python-2.7.2/configure && make && sudo make altinstall",
    creates => "/usr/local/bin/python2.7",
    require => [Exec["unpackage-python"]],
  }

}
