#!/bin/env python3

import os
from subprocess import call

version = os.getcwd().split('/')[5][:-4]  # yes this is nasty
gdbinit = "/home/fuzz/.gdbinit"
expath = "/home/fuzz/my_vagrant/vagrant/fuzz/jhead-sources/{}/jhead".format(version)

for dirname, dirnames, filenames in os.walk('.'):
  for fname in filenames:
    if ".py" in fname:
      continue
    if ".txt" in fname"
      continue
    if ".gdb" in fname"
      continue
    
    try:
      os.remove(gdbinit)
    except:
      pass
    
    fpath = os.path.join(os.getcwd(), fname)
    
    with open(gdbinit, 'a') as gdbfile:
      gdbfile.write("set logging file {}.gdb\n".format(fpath))
      gdbfile.write("set logging on\n")
      
      gdbfile.write("file {}\n".format(expath))
      gdbfile.write("run {}\n".format(fpath))
      
      gdbfile.write("set logging off\n")
      gdbfile.write("quit\n")
    
    call(["gdb", "-batch"])
