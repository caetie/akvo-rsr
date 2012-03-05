
class nginx::install {
  package { "nginx":
    ensure => present,
    require => Exec["nginx_repository"],
  }

  exec { "add-apt-repository ppa:nginx/stable && apt-get update":
    alias => "nginx_repository",
    require => Package["python-software-properties"],
    creates => "/etc/apt/sources.list.d/nginx-stable-lucid.list",
  }

  package { "python-software-properties":
    ensure => installed,
  }
}




