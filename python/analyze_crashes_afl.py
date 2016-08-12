#!/bin/env python3

import os
from collections import namedtuple

Crash = namedtuple('Crash', ['msg', 'count'])
crash_msgs = []

for dirname, dirnames, filenames in os.walk('.'):
  for fname in filenames:
    if ".gdb" in fname:
      f_path = os.path.join(dirname, fname)
      try:
        lines = list(open(f_path))
      except:
        print("Error reading {}".format(f_path))
        continue
      if len(lines) < 2:
        break
      words = lines[2].split("")
      if "0x0" in words[0]:
        words[0] = words[2]
      crash.msgs.append("{} - {}".format(words[0], words[-1]))
      
try:
  os.remove('./crashing_functions.txt')
except:
  pass
  
with open('./crashing_functions.txt') as out:
  counted_crashes = [ Crash(msg, crash_msgs.count(msg))
                      for msg in sorted(set(crash_msgs)) ]
  for crash in counted_crashes:
    out.write("{} - {}".format(crash.count, crash.msg))
