
class python::deps {
  
  package {
    [
      "libncursesw5-dev", 
      "libssl-dev", 
      "libsqlite3-dev", 
      #"tk-dev", 
      "libgdbm-dev", 
      "libc6-dev", 
      "libbz2-dev"
    ]:
    ensure => installed,
    require => Class['system::tools'],
  }
  
}
