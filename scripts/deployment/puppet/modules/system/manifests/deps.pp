class system::deps {

  package {
    [
      "build-essential",
      "checkinstall",
    ]:
    ensure => "latest",
    require => Class['system::apt'],
  }
  
}
