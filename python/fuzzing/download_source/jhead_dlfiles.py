#!/usr/bin/env python3

# ###########################################################################
# NOTE: See setup_dlsource.py, that is the main file where this is imported
# ###########################################################################

import urllib.request

def download_archives():
	for i in range(84, 98):
		url = "http://www.sentex.net/~mwandel/jhead/jhead-2.%02d.tar.gz" % i
		dlname = url.split('/')[-1]
		try:
		    urllib.request.urlretrieve(url, dlname)
		except:
		    print("{} not found, probably doesn't exist".format(dlname))

def download_current():
	url = "http://www.sentex.net/~mwandel/jhead/jhead-3.00.tar.gz"
	name = url.split("/")[-1]
	try:
		urllib.request.urlretrieve(url, name)
	except:
		print("ERROR: Cannot find current version ({}), please check url.", name)
