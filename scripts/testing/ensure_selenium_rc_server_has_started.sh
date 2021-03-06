#!/bin/bash

# Parameters:
# $1: rc_server_log_path
# $2: xvfb_log_path (optional)
# $3: xvfb_display (optional)


SCRIPT_FILE_DIR="`dirname $0`"
TESTING_SCRIPTS_DIR="`cd $SCRIPT_FILE_DIR; pwd`"

function display_usage_and_exit
{
    echo "Usage: ensure_selenium_rc_server_has_started <rc_server_log_path> [xvfb_log_path] [xvfb_display]"
    echo "Optionally specify an xvfb_log_path to start the Selenium RC server in headless mode"
    echo "Additionally specify an xvfb_display to start in headless mode on a specific display"
    exit -1
}

function verify_script_parameters
{
    # warn if extraneous parameters exist
    if [ -n "$4" ]; then
        echo ">> Unexpected number of parameters: $*"
        display_usage_and_exit
    fi

    # check if rc_server_log_path parameter exists
    if [ -z "$1" ]; then
        echo ">> Missing rc_server_log_path parameter"
        display_usage_and_exit
    fi
}

function ensure_xvfb_is_running_and_set_display
{
    # Parameters:
    # $1: xvfb_log_path
    # $2: xvfb_display

    XVFB_LOG_PATH="$1"

    # start Xvfb if the Xvfb process files does not exist
    if [ ! -e "$XVFB_LOG_PATH/xvfb.pid" ]; then
        XVFB_DISPLAY=":$$" # use the current process ID to avoid clashes if Xvfb is being used elsewhere

        # otherwise use the specified display value
        if [ -n "$2" ]; then
            XVFB_DISPLAY="$2"
        fi

        "$TESTING_SCRIPTS_DIR/start_xvfb.sh" $XVFB_LOG_PATH $XVFB_DISPLAY
    fi

    export DISPLAY="`cat $XVFB_LOG_PATH/xvfb_display.txt`"
}

function ensure_selenium_rc_server_is_running
{
    # Parameters:
    # $1: rc_server_log_path
    # $2: xvfb_log_path
    # $3: xvfb_display

    RC_SERVER_LOG_PATH="$1"

    # check if the Selenium RC server is already running
    if [ ! -e "$RC_SERVER_LOG_PATH/rc_server.pid" ]; then
        # check if the xvfb_log_path parameter was also provided
        if [ -n "$2" ]; then
            XVFB_LOG_PATH="$2"
            ensure_xvfb_is_running_and_set_display "$XVFB_LOG_PATH" "$3"

            "$TESTING_SCRIPTS_DIR/start_selenium_rc_server.sh" "$RC_SERVER_LOG_PATH" "$XVFB_LOG_PATH"
        else
            "$TESTING_SCRIPTS_DIR/start_selenium_rc_server.sh" "$RC_SERVER_LOG_PATH"
        fi    
    fi
}

verify_script_parameters $*
ensure_selenium_rc_server_is_running "$1" "$2" "$3"
