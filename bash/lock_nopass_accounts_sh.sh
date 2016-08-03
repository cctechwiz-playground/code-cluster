#!/bin/bash
sudo passwd -aS | awk '$2 == "NP" { print $1 }' > user_list
while read user; do
  if [ "$user" != "root" ]; then
    sudo passwd -l $user
    echo "$user has been locked."
  fi
done
rm user_list
