#!/bin/bash

cd "`dirname $0`"

PIP_DIR="`pwd`"
CURRENT_USER="`whoami`"

# exit if not running with sudo or as root
if [ $CURRENT_USER != "root" ]; then
    printf ">> This script should be executed with sudo to facilitate installation of system Python packages\n"
    printf ">> Current user: $CURRENT_USER\n"
    exit -1
fi

cd "$PIP_DIR"

# exit if osx_system.config file does not exist
if [ ! -e osx_system.config ]; then
    printf "\n>> Expected osx_system.config file not found -- copy the osx_system.config.template file and edit as necessary\n"
    exit -1
fi

source osx_system.config
source osx_build_flags_env_64.config

PY_PATH="$PY_BIN_PATH/python"

function ensure_temp_dir_exists
{
    if [ ! -d "$PYTHON_TEMP_DIR" ]; then
        printf "\n>> Creating temp directory: $PYTHON_TEMP_DIR\n"
        mkdir -p "$PYTHON_TEMP_DIR"
    else
        printf "\n>> Using existing temp directory: $PYTHON_TEMP_DIR\n"
    fi
}

function install_distribute_package
{
    # See installation notes at http://pypi.python.org/pypi/distribute#distribute-setup-py
    printf "\n>> Installing distribute package\n"
    cd "$PYTHON_TEMP_DIR"
    curl -L -O http://python-distribute.org/distribute_setup.py
    $PY_PATH distribute_setup.py
}

function link_easy_install
{
    # This should ensure the installed easy_install is used rather than /usr/bin/easy_install
    # as long as the /usr/local/bin directory is before /usr/bin on the system path
    printf "\n>> Linking easy_install in /usr/local/bin\n"
    VERSIONED_EASY_INSTALL="easy_install-$PY_VERSION"
    cd /usr/local/bin
    ln -s "$PY_BIN_PATH/$VERSIONED_EASY_INSTALL" $VERSIONED_EASY_INSTALL
    ln -s $VERSIONED_EASY_INSTALL easy_install
    printf ">> Resulting easy_install links:\n"
    ls -la /usr/local/bin/easy*
}

function install_pip_package
{
    # See installation notes at http://www.pip-installer.org/en/latest/installing.html
    printf "\n>> Installing pip package\n"
    cd "$PYTHON_TEMP_DIR"
    curl -L -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
    $PY_PATH get-pip.py
}

function install_system_packages
{
    cd "$PIP_DIR"
    printf "\n>> Current system packages:\n"
    pip freeze

    printf "\n>> Installing/upgrading system packages: (with 64-bit architecture)\n"
    pip install -M -r requirements/0_system.txt

    printf "\n>> Installing/upgrading deployment packages: (with universal 32-bit & 64-bit architecture)\n"
    source osx_build_flags_env_intel.config
    pip install -M -r requirements/1_deployment.txt

    printf "\n>> Installed system packages:\n"
    pip freeze
}

function build_system_environment
{
    ensure_temp_dir_exists
    install_distribute_package
    link_easy_install
    install_pip_package
    install_system_packages
}


build_system_environment