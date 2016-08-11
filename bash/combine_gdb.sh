#!/bin/bash

# USAGE:
# ./combine_gdb.sh gdb_files.txt

# I get the gdb_files.txt with: 'ls ./crashes/*/*.gdb > gdb_files.txt'
# Then removing all the duplicates between the .gdb and minimized.gdb

while IFS='' read -r line || [[ -n "$line" ]]; do
    cat $line | head -n 3 | tail -n 1 >> "crash_locations.txt"
done < "$1"
