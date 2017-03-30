#!/bin/bash

open() {
    dolphin $1 > /dev/null 2>&1 &
    echo "Opened" $(readlink -f $1)
}
