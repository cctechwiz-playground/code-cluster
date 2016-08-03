#/bin/bash

# drum_run, version 1
# Author: Josh Maxwell < cctechwiz@gmail.com >
# Date: Wednesday July 6th, 2016

# Description:
# Helps to setup environment securely for running Vagrant fuzzers on DRUMSTICK
# "Securely" is meant to mean 'without leaving password in history or env'

# Bug:
# You can pass "echo $DRUMSTICK_PASS" as the -c command and see the password,
# which defeats the intended purpose of this script


COMMAND=""
USERNAME="joshd@vullab.cert.org"
PASSWORD=""
HAS_CMD=0
PROG_NAME=$0

# Prints usage statement:
# Usage:
# usage $1=exit_code [$2=error_message]
usage() {
    # Print error_message if any
    if [ -n "$2" ]; then
        (>&2 echo $PROG_NAME: $2)
    fi

    # Print usage statement
    echo "Usage: $PROG_NAME -c <command> [-u <username>]"
    echo "Type '$PROG_NAME -h' to see this message again"
    echo "Defaults:
    <command>: NONE
    <username>: $USERNAME
    <password>: NONE"
    echo "NOTE: If <command> contains a space, please surroud with quotes"

    # exit with exit_code
    if [ -n $1 ]; then
        exit $1
    else
        exit 1
    fi
}

# Define options and gather them (: means argument is required)
while getopts "c:u:h" opt; do
    case $opt in
        c) # command flag present (-c:)
            COMMAND=$OPTARG
            HAS_CMD=1
            ;;
        u) # username flag present (-u:)
            USERNAME=$OPTARG
            ;;
        h) # Help flag present (-h)
            usage 0
            ;;
        \?) # Unknown option found
            usage 2
            ;;
        :) # Option is missing argument
            usage 2
            ;;
    esac
done

# Verify that command (-c) option was specified
if [ 0 -eq $HAS_CMD ]; then
    usage 2 "missing command, use -c to specify the command"
fi

# Ask user for password (-s prevents user input from being echo'ed to stdout)
read -s -p "Enter vSphere Password: " PASSWORD
echo " "

# Setup ENV and call command
export DRUMSTICK_USER=$USERNAME
export DRUMSTICK_PASS=$PASSWORD
eval $COMMAND

# Check exit status of command evaluated
CMD_EXIT=$?
if [ 0 -ne $CMD_EXIT ]; then
    echo "<<<<<<<<<< Error message from evaluated <command> >>>>>>>>>>"
    echo "Does the <command> you tried to call contain a space?"
    usage $CMD_EXIT "<command> returned an error."
fi

# No error detected, have a nice day...
exit 0

