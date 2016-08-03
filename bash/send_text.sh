#!/bin/bash

#Sends a text message to a number

curl http://textbelt.com/text \
	-d number=$1 \
	-d "message=$2"
