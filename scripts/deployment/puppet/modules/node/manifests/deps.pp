class node::deps {

  package {
    [
      "pkg-config",
      "gcc",
      "g++",
    ]:
    ensure => installed,
    require => Class['python::deps'],
  }
  
}
