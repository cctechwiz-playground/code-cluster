#!/usr/bin/env python3

# ###########################################################################
# NOTE: See setup_dlsource.py, that is the main file where this is imported
# ###########################################################################

import urllib.request

def download_archives():
	for i in range(0, 29):
		url = "ftp://ftp.astron.com/pub/file/file-5.%02d.tar.gz" % i
		dlname = url.split('/')[-1]
		try:
		    urllib.request.urlretrieve(url, dlname)
		except:
		    print("{} not found, probably doesn't exist".format(dlname))

def download_current():
	url = "ftp://ftp.astron.com/pub/file/file-5.28.tar.gz"
	name = url.split("/")[-1]
	try:
		urllib.request.urlretrieve(url, name)
	except:
		print("ERROR: Cannot find current version ({}), please check url.", name)
