class nginx::deps {

  package {
    [
      "libc6",
      "libpcre3",
      "libpcre3-dev",
      "lsb-base",
      "zlib1g",
      "zlib1g-dev",
    ]:
    ensure => installed,
    require => Class['system::deps'],
  }
  
}
