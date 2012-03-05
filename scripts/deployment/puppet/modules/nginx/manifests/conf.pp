class nginx::conf {
  
  file { "/usr/local/nginx/conf/sites-enabled":
    ensure => "directory",
    owner  => "root",
    group  => "root",
    mode   => 750,
    require => Class['nginx::install'],
  }

  file { '/etc/nginx/nginx.conf':
    ensure  => present,
    mode    => '0644',
    owner   => 'root',
    group   => 'root',
    content => template('nginx/nginx.conf.erb'),
    # notify  => Service['nginx'],
    require => File['/usr/local/nginx/conf/sites-enabled'],
  }
  

}
