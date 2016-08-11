#!/usr/bin/env python3

# ###########################################################################
# NOTE: See setup_dlsource.py, that is the main file where this is imported
# ###########################################################################

import urllib.request

def download_archives():
	urllib.request.urlretrieve("http://download.videolan.org/pub/videolan/vlc/", "out")
	files = list()
	with open("out", "r") as f:
		for line in f:
		    tmp = line.split("\"")
		    if len(tmp) > 1:
		        if tmp[1][0].isdigit():
		            files.append(tmp[1])

	for dirname in files:
		url = "http://download.videolan.org/pub/videolan/vlc/" + dirname
		name = dirname.rstrip("/")
		# Names that don't follow the pattern, might as well still download
		if name == "0.2.0":
		    dlname = url + "vlc_" + name + ".tar.gz"
		elif name == "0.2.50":
		    dlname = url + "vlc_" + name + "-1.tar.gz"
		# No source associated with these names
		elif name in ["0.4.3-ac3", "1.1.10.1"]:
		    continue
		# Normal pattern of names
		else:
		    dlname = url + "vlc-" + name + ".tar.gz"

		try:
		    urllib.request.urlretrieve(dlname, name + ".tar.gz")
		except:
		    try:
		        # Some tarballs are sporadically .bz2 instead of .gz
		        dlname = url + "vlc-" + name + ".tar.bz2"
		        urllib.request.urlretrieve(dlname, name + ".tar.bz2")
		    except:
		        try:
		            # File format changed with version 2.0.0 and onward
		            dlname = url + "vlc-" + name + ".tar.xz"
		            urllib.request.urlretrieve(dlname, name + ".tar.xz")
		        except:
		            print("{} not found with either .gz, .bz2, or .xz".format(name))

def download_current():
	url = "http://get.videolan.org/vlc/2.2.4/vlc-2.2.4.tar.xz"
	name = url.split("/")[-1]
	try:
		urllib.request.urlretrieve(url, name)
	except:
		print("ERROR: Cannot find current version ({}), please check url.", name)
