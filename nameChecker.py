import colorama
from termcolor import colored
import urllib3
import certifi
import time
import json
import keyboard
from art import *
from os import system, name
import threading
#MADE BY ETOG
colorama.init()

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
clear()

url = 'https://api.mojang.com/users/profiles/minecraft/'
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
tprint("made   by   etog   &")
tprint("CoolManTheCool")
print("Searching for names.txt...")



def checkNames(startingIndex, endingIndex):
    
    with open('names.txt') as f:
        totalIndex = 0
        f3 = f.readlines()
        print(startingIndex)
        index = startingIndex
        while(True):
            time.sleep(0.005)
            line = f3[index]
            line = line.strip(' ').strip('\n')
            #print(str(index) + ", " + str(startingIndex) + ", " + line)
            index += 1
            if index > int(startingIndex):
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
                    if(keyboard.is_pressed('q')):
                        print(line)
                    totalIndex += 1
                    None
                else:
                    f3.write(line)
                    print(colorama.Fore.GREEN +"Username: " + colorama.Style.RESET_ALL + line + colorama.Fore.GREEN + " = Available" + colorama.Style.RESET_ALL)
                if(startingIndex is endingIndex):
                    break
threadRange = int(input("How many GIGA thread you want yo? "))
for iIi in range(threadRange):
    thingy = int(50653/threadRange*(iIi))
    thingy2 = int(50653/threadRange*(iIi+1))
    
    threading.Thread(target=checkNames, args=[thingy, thingy2]).start()