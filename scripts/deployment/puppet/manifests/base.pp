
Exec { path => [ "/bin/", "/sbin/" , "/usr/bin/", "/usr/sbin/" ] }



include system::git

include python::deps
include python::python
include python::pip
include python::venv
