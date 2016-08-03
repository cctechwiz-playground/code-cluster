#!/usr/bin/python

import sys

print "Number of args: ", len(sys.argv), "\n"
print "Args: ", str(sys.argv)

#TODO: use switches for file vs list -> import getopt, getopt.getop()
#http://www.tutorialspoint.com/python/python_command_line_arguments.htm
#TODO: Verify the file opens

f = open(sys.argv[1], 'r')
for line in f.readlines():
    print "ping -c 1 ", line
f.close()
