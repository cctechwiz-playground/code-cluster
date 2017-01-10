#!/bin/bash

# ./monitor_public_ip

# Periodically checks that the public IP address
# hasn't changed. If it has, then an email is sent
# notifying of the new public IP address

# Dependencies:
#   sendemail
#   libio-socket-ssl-perl
#   libnet-ssleay-perl

# Run with screen:
#   screen -d -m -S ip /monitor_public_ip.sh

USERNAME="cctechwiz@gmail.com"
PASSWORD="meiqmuljxgvzgofn"
RECV="cctechwiz@gmail.com, jam.maxwell@gmail.com"

touch new_ip
touch old_ip

for (( ; ; )); do
    cp new_ip old_ip 2> /dev/null
    PUBLIC_IP="$(wget http://ipinfo.io/ip -qO -)"
    echo $PUBLIC_IP > new_ip
    DIFF="$(diff new_ip old_ip)"
    if [ "0" != "${#DIFF}" ]; then
        sendEmail -f $USERNAME -s smtp.gmail.com:587 \
            -xu $USERNAME -xp $PASSWORD -t $RECV \
            -o tls=yes -u "Public IP address changed" \
            -m "Public IP: $PUBLIC_IP\nPort: 21337"
        sleep 1d
    fi
done
