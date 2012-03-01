class system::tools {

  package {
    [
      "git-core",
      "mercurial",
      "curl",
      "yui-compressor"
    ]:
    ensure => "latest",
    require => Class['system::deps'],
  }
  
}
