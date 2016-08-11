#!/usr/bin/env python3
# USAGE: python3 setup_dlsource.py [working_dir]
# 'working_dir' is a path to an existing directory where the source for
# each program should be downloaded, default is current working directory

# ###########################################################################
# NOTE: Make sure to update any links in the impoted modules for each program
# ###########################################################################

import os, sys
from shutil import copyfile
# import download script for each program
import clamav_dlfiles as clamav
import file_dlfiles as filep
import jhead_dlfiles as jhead
import mupdf_dlfiles as mupdf
import vlc_dlfiles as vlc

if len(sys.argv) > 1:
    working_dir = sys.argv[1]
    print("Working directory: {}".format(working_dir))
    if not os.path.isdir(working_dir):
        print("Directory does not exist.")
        quit()
else:
    working_dir = "./"
    print("Working directory not supplied, using current directory...")

progs = {"clamav": clamav,
        "file": filep,
        "jhead": jhead,
        "mupdf": mupdf,
        "vlc": vlc}

os.chdir(working_dir)
for k in progs:
    # Make main folder for candidate program
    print("Starting {} >>>".format(k))
    os.mkdir("./" + k)
    # Make current subfolder, download current version
    print("Downloading current version...")
    os.mkdir("./" + k + "/current")
    os.chdir("./" + k + "/current")
    progs[k].download_current()
    os.chdir("../..")
    # Make archive subfolder, download archived versions
    print("Downloading archived versions...")
    os.mkdir("./" + k + "/archive")
    os.chdir("./" + k + "/archive")
    progs[k].download_archives()
    os.chdir("../..")
    print("<<< Finished with {}".format(k))
