#!/bin/env python3

# USAGE:
# ./analyze_crashes.py - Run from the crashers/ folder
# Will look at the gdb output files and print all the unique 
# Fucntions and lines where the crashes happend.

import os

crashes = []
for dirname, dirnames, filenames in os.walk('.'):
  for subdirname in dirnames:
    for f in os.listdir(subdirname):
      if "gdb" in f:
        f_path = os.path.join(dirname, subdirname, f)
        lines = list(open(f_path))
        words = lines[2].split(" ")
        if "raise" not in words:
          crashes.append("{} - {}".format(words[2], words[-1])
        break  # Skip the minimized.gdb file if .gdb is present

os.remove('./crashing_functions.txt')
out = open('./crashing_functions.txt', 'a')
for line in sorted(set(crashes)):
  out.write(line)
out.close()
