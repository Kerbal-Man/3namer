import colorama
from termcolor import colored
import urllib3
import certifi
import json

#MADE BY ETOG
colorama.init()

with open('names.txt') as f:
    for line in f:
        line = line.strip(' ').strip('\n')

        url = 'https://api.mojang.com/users/profiles/minecraft/'
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        try:
            r = http.request('GET', url + line)
            # print str(url + line)
        except urllib3.exceptions.SSLError as e:
          print(" ")

        try:
            r_data = json.loads(r.data.decode('utf-8'))

        except Exception as e:

            r_data = ""

        if r_data:
            print("Username: " + line + colorama.Fore.RED + " = Not Available" + colorama.Style.RESET_ALL)
            None
        else:
            print("Username: " + line + colorama.Fore.GREEN + " = Available" + colorama.Style.RESET_ALL)