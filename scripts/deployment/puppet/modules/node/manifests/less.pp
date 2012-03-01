class node::less {

  exec { "install-less":
    cwd => "/opt",
    command => "sudo /usr/local/bin/npm install less -g",
    creates => "/usr/local/bin/lessc",
    require => Class['node::npm'],
  }

}
