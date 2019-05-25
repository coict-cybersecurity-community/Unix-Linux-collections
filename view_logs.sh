#!/bin/sh

# @Author Frances Ruganyumisa
# fruganyumisa@gmail.com
# CoICT Udsm
# This is the bash script to view the logs 
# specifically the syslogs 
echo "Hi get ready to take logs and save to directory of your choice "
echo "Please enter your username"
read user

cd /home/$user/Desktop/

echo "Enter the name of directory you would like to save to"

read dir_name
mkdir $dir_name

tail -f /var/log/syslog >> /home/$user/Desktop/$dir_name/log