class python::venv {

  exec { "install-venv":
    cwd => "/opt",
    command => "/usr/local/bin/pip install virtualenv",
    creates => "/usr/local/bin/virtualenv",
    require => Class['python::pip'],
  }
  
}
