class system::deps {

  package {
    [
      "build-essential",
      "checkinstall",
      "libssl-dev",
    ]:
    ensure => "latest",
    require => Class['system::apt'],
  }
  
}
