class system::apt {

  exec { 'apt-update':
    command => 'sudo /usr/bin/apt-get -y update',
    # refreshonly => true; 
  }

  # exec { 'apt-upgrade':
  #   command => 'sudo /usr/bin/apt-get -y dist-upgrade',
  #   # refreshonly => true,
  #   timeout => 3600,
  #   require => [Exec["apt-update"]],
  # } 

  # exec { "apt-update":
  #    command => "sudo /usr/bin/apt-get update",
  #    refreshonly => true;
  #  } 
  
  # Ensure apt is setup before running apt-get update
  # Apt::Key <| |> -> Exec["apt-update"]
  # Apt::Source <| |> -> Exec["apt-update"]

  # Ensure apt-get update has been run before installing any packages
  # Exec["apt-update"] -> Package <| |>
}
