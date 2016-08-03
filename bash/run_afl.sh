#!/bin/bash

## Set environment variables for ImageMagick to use when running
export MAGICK_HOME=~/Documents/AFL_convert/ImageMagick-5.3.0
export LD_LIBRARY_PATH=~/Documents/AFL_convert/ImageMagick-5.3.0
## This next line was supposed to change the temp folder but did not
# export MAGICK_TEMPORARY_PATH=~/Documents/AFL_convert/temp

## Declare functions
# Runs a tests to verify that the environment variables are set correctly
# An error will be displayed if there is a problem, script must be stopped(^c)
test_workspace()
{
    echo "Testing convert with good input.bmp"
    ~/Documents/AFL_convert/ImageMagick-5.3.0/utilities/convert \
	    ~/Documents/AFL_convert/seedfiles/input.bmp /dev/null
    echo "Done"
}

# Loops forever clening up /tmp so the VM doesn't run out of space
clean_temp()
{
	echo "Cleanup running..."
	cd /tmp
	for (( ; ; ))
	do
		sleep 1m
		rm magic*
	done
}

# Run the afl-fuzz after 5 seconds (time to cancel(^c) if there was an error)
run_afl()
{
	echo "Starting AFL..."
	echo "^c to abort (5 seconds)"
	sleep 5

	afl-fuzz \
	    -i ~/Documents/AFL_convert/min_seeds/ \
	    -o ~/Documents/AFL_convert/out/ \
        ~/Documents/AFL_convert/ImageMagick-5.3.0/utilities/convert @@ \
        /dev/null
}

## main
test_workspace
run_afl & clean_temp

