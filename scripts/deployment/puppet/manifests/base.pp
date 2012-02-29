
Exec { path => [ "/bin/", "/sbin/" , "/usr/bin/", "/usr/sbin/" ] } 

include python::deps
include python::python
include python::pip
include python::venv
