class nginx::conf {

  file { "/usr/local/nginx/conf/sites-enabled":
    ensure => "directory",
    owner  => "root",
    group  => "root",
    mode   => 644,
    require => Class['nginx::install'],
  }

  file { "/usr/local/nginx/conf/nginx.conf":
    ensure  => present,
    mode    => 644,
    owner   => "root",
    group   => "root",
    content => template("nginx/nginx.conf.erb"),
    # notify  => Service['nginx'],
    require => File["/usr/local/nginx/conf/sites-enabled"],
  }

  file { "/usr/local/nginx/conf/sites-enabled/akvo.org":
    ensure  => present,
    mode    => 644,
    owner   => "root",
    group   => "root",
    content => template("nginx/akvo.org.erb"),
    # notify  => Service['nginx'],
    require => File["/usr/local/nginx/conf/nginx.conf"],
  }

  file { "/var/www":
    ensure => "directory",
    owner  => "vagrant",
    group  => "vagrant",
    mode   => 644,
    require => File['/usr/local/nginx/conf/sites-enabled/akvo.org'],
  }

  file { "/var/www/akvo":
    ensure => "directory",
    owner  => "vagrant",
    group  => "vagrant",
    mode   => 644,
    require => File['/var/www'],
  }

  file { "/var/www/akvo/media":
    ensure => "directory",
    owner  => "vagrant",
    group  => "vagrant",
    mode   => 644,
    require => File['/var/www/akvo'],
  }

  file { "/var/www/akvo/static":
    ensure => "directory",
    owner  => "vagrant",
    group  => "vagrant",
    mode   => 644,
    require => File['/var/www/akvo'],
  }

}
