#!/usr/bin/env python3

# ###########################################################################
# NOTE: See setup_dlsource.py, that is the main file where this is imported
# ###########################################################################

import urllib.request

def download_archives():
	urllib.request.urlretrieve("http://mupdf.com/downloads/archive", "out")
	files = list()
	with open("out", "r") as f:
		for line in f:
		    if "source.tar.gz" in line:
		        tmp = line.split("\"")
		        files.append(tmp[7])

	for dlname in files:
		url = "http://mupdf.com/downloads/archive/" + dlname
		try:
		    urllib.request.urlretrieve(url, dlname)
		except:
		    print("{} not found".format(dlname))

def download_current():
	url = "http://mupdf.com/downloads/mupdf-1.9a-source.tar.gz"
	name = url.split("/")[-1]
	try:
		urllib.request.urlretrieve(url, name)
	except:
		print("ERROR: Cannot find current version ({}), please check url.", name)
