#!/bin/env python3

# USAGE:
# ./analyze_crashes.py - Run from the crashers/ folder
# Will look at the gdb output files and print all the unique 
# Fucntions and lines where the crashes happend.

import os
from collections import namedtuple

Crash = namedtuple('Crash', ['msg', 'count'])
crash_msgs = []

for dirname, dirnames, filenames in os.walk('.'):
  for subdirname in dirnames:
    for f in os.listdir(subdirname):
      if "gdb" in f:
        f_path = os.path.join(dirname, subdirname, f)
        lines = list(open(f_path))
        words = lines[2].split(" ")
        if "raise" not in words:
          crash_msgs.append("{} - {}".format(words[2], words[-1])
        break  # Skip the minimized.gdb file if .gdb is present

# Clean up old file if any
try:
  os.remove('./crashing_functions.txt')
except:
  pass

with open('./crashing_functions.txt', 'a') as out:
  counted_crashes = [ Crash(msg, crash_msgs.count(msg))
                      for msg in sorted(set(crash_msgs)) ]
  for crash in counted_crashes:
    out.write("{} - {}".format(crash.count, crash.msg))
