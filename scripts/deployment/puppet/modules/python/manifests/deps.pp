
class python::deps {
  package {
    [
      "build-essential", 
      "libncursesw5-dev", 
      "libssl-dev", 
      "libsqlite3-dev", 
      "tk-dev", 
      "libgdbm-dev", 
      "libc6-dev", 
      "libbz2-dev"
    ]:
    ensure => installed, require => Exec['apt-get_update']
  }
  exec { 
    'apt-get_update': 
      command => '/usr/bin/apt-get -y update; echo $?',
  }
}
