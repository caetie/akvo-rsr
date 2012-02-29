class python::pip {

  exec { "download-distribute":
    cwd => "/opt",
    command => "/usr/bin/wget http://python-distribute.org/distribute_setup.py",
    creates => "/opt/distribute_setup.py",
    require => Class['python::python'],
  }

  exec { "install-distribute":
    cwd => "/opt",
    command => "/usr/local/bin/python2.7 /opt/distribute_setup.py",
    require => [Exec["download-distribute"]],
  }

  exec { "download-pip":
    cwd => "/opt",
    command => "/usr/bin/wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py",
    creates => "/opt/get-pip.py",
    require => [Exec["install-distribute"]],
  }

  exec { "install-pip":
    cwd => "/opt",
    command => "/usr/local/bin/python2.7 /opt/get-pip.py",
    creates => "/usr/local/bin/pip",
    require => [Exec["download-pip"]],
  }

}
