#!/bin/bash
users=$(sudo passwd -aS | awk '$2 == "P" { print $1 }')

SetPassword()
{
  local pass1 pass2
  echo -n "Type new password for $i: "
  read -s pass1
  echo ""
  echo -n "Re-type password: "
  read -s pass2
  echo ""
  if [ "$pass1" == "$pass2" ]; then
    echo "$i:$pass1" | sudo chpasswd
    echo "Password changed!"
  else
    echo "Passwords don't match. Try again."
    SetPassword
  fi
}

for i in $users; do
  if [ $i != "root" ]; then
    SetPassword
  fi
done

unset i users
