#!/usr/bin/env python3

# ###########################################################################
# NOTE: See setup_dlsource.py, that is the main file where this is imported
# ###########################################################################

import urllib.request

def download_archives():
	for i in range(70, 100):
		url = "https://github.com/vrtadmin/clamav-devel/archive/clamav-0.{}.tar.gz".format(i)
		name = url.split("/")[-1]
		try:
		    urllib.request.urlretrieve(url, name)
		    # Try to get minor versions
		    for v in range(1, 10):
		        url = "https://github.com/vrtadmin/clamav-devel/archive/clamav-0.{}.{}.tar.gz".format(i, v)
		        name = url.split("/")[-1]
		        try:
		            urllib.request.urlretrieve(url, name)
		        except:
		            # Not found, safe to assume successors don't exist
		            break
		except:
		    print("{} not found, probably doesn't exist".format(name))

def download_current():
	url = "http://downloads.sourceforge.net/project/clamav/clamav/win32/0.99.1/clamav-0.99.1-win32.msi?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fclamav%2Ffiles%2Fclamav%2F&ts=1468343057&use_mirror=heanet"
	name = url.split("/")[-1]
	try:
		urllib.request.urlretrieve(url, name)
	except:
		print("ERROR: Cannot find current version ({}), please check url.".format(name))
