class nginx::conf {
  
  require => Class['nginx::install'],

}
