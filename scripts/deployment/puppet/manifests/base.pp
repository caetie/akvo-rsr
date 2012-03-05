
Exec { path => [ "/bin/", "/sbin/" , "/usr/bin/", "/usr/sbin/", "/usr/local/bin/" ] }

include system::apt
include system::deps
include system::tools

include python::deps
include python::python
include python::pip
include python::venv

include nginx
# include nginx::deps
# include nginx::install
# include nginx::conf

include node::deps
include node::node
include node::npm
include node::less
