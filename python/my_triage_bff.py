#!/bin/env python3

import os
import subprocess as proc
import shlex

gdb_cmd = "gdb --batch " +\
          "-ex \"set logging file {logfile}\" -ex \"set logging on\" " +\
          "-ex \"python import exploitable\" -ex \"file {cmd}\" " +\
          "-ex \"run {infile}\" -ex exploitable " +\
          "-ex \"set logging off\" -ex quit"

version = os.getcwd().split('/')[5][:-4]
jhead_path = "/home/fuzz/my_vagrant/vagrant/fuzz/jhead-sources/{}/jhead".format(version)

report = []

for path, dirnames, filenames in os.walk('.'):
  for dname in dirnames:
    for fname in os.listdir(dname):
      # skip non jpg-files
      if ".gdb" in fname:
        continue
      if ".stderr" in fname:
        continue
      if ".log" in fname:
        continue
      if "minimized" in fname:
        continue
        
      if ".jpg" in fname and "-" in fname:
        fpath = os.path.join(path, dname, fname)
        lfile = fpath + ".log"
        full_cmd = gdb_cmd.format(logfile=lfile, cmd=jhead_path, infile=fpath)
        with open("/dev/null", "w") as ofile:
          proc.call(shlex.split(full_cmd), stdout=ofile, stderr=ofile)
          
        for line in open(lfile):
          if "Classification" in line:
            report.append(line.split(" ")[-1])

rfname = "./exploitability.report"
if os.path.exists(rfname):
  os.remove(rfname)

with open(rfname, "a") as rfile:
  counted_report = [ (cls, report.count(cls)) for cls in sorted(set(report)) ]
  for item in counted_report:
    r = "{} - {}\n".format(item[0].split('\n')[0], item[1])
    print(r)
    rfile.write(r)
