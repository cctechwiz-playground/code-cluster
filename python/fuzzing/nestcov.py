# Take from the work of Jonathan Foote
# https://insights.sei.cmu.edu/cert/2012/12/forking-and-joining-python-coroutines-to-collect-coverage-data.html

import re, os
from collections import namedtuple
FileCoverage = namedtuple("FileCoverage", ["filename", "percentage", "lines"])

def call(cmd):
  import subprocess, shlex
  return subprocess.check_output(shlex.split(cmd))

srcdir = os.getcwd()
coverage = []
gcda_filenames = call("find %s -name \"*.gcda\"" % srcdir)
for gcda_filename in gcda_filenames.splitlines():
  obj_filename = gcda_filename.replace(".gcda", ".o")
  instr = call("readelf --debug-dump %s" % obj_filename)

  # get filenames from readelf output
  outstr = instr[instr.find("The File Name Table"):]
  outstr = outstr[:outstr.find("\n\n")]
  outlines = outstr.splitlines()[2:]
  c_files = []
  for line in outlines:
    filename = line.split()[4]
    if re.match(".*\.c$|.*\.c..$", filename):
      src_filename = call("find %s -name %s" % (srcdir, filename)).splitlines()[0]
      gcov_out = call("gcov -no %s %s" % (gcda_filename, src_filename))
      filename = None
      for gline in gcov_out.splitlines():
        if filename:
          m = re.match("^Lines executed:(\d+\.\d\d)% of (\d+)$", gline)
          if not m:
            raise RuntimeError("Failure parsing gcov output; 'Lines' doesn't follow 'Files'")
          percent, lines = m.groups()
          coverage.append(FileCoverage(filename, float(percent), int(lines)))
          filename = None
          continue
        m = re.match("^File '(.*)'$", gline)
        if not m:
          filename = None
          continue
        filename = m.groups()[0]
total_lines = sum([fc.lines for fc in coverage])
total_covered = sum([fc.percentage*fc.lines/100 for fc in coverage])
total_percentage = total_covered / total_lines
print total_percentage
