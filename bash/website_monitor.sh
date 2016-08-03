#!/bin/bash

#USAGE:
#./website_monitor "www.url.to.monitor"

#Monitors a webpage for change and notifies
#Run with 'nohup ./website_monitor.sh &
#to persist in the background

#SendEmail is a third party tool
#NOTE: password is a google app password

#Dependencies:
#	Curl
#	SendEmail
#	libio-socket-ssl-perl
#	libnet-ssleay-perl

USERNAME="cctechwiz@gmail.com"
PASSWORD="meiqmuljxgvzgofn"
URL=$1

echo "Monitoring changes in $URL"
echo "Will notify $USERNAME"

for (( ; ; )); do
	mv new.html old.html 2> /dev/null
	curl $URL -L --compressed -s > new.html
	DIFF_OUTPUT="$(diff new.html old.html)"
	if [ "0" != "${#DIFF_OUTPUT}" ]; then
		sendEmail -f $USERNAME -s smtp.gmail.com:587 \
			-xu $USERNAME -xp $PASSWORD -t $USERNAME \
			-o tls=yes -u "Web page changed" \
			-m "View changes at $URL\n\n Overview:\n$DIFF_OUTPUT"
		sleep 1h
	fi
done
