#!/usr/bin/python
import os
import platform

def shutdown():
    if platform.system() == "Windows":
        os.system('shutdown -s')
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system('sudo shutdown -h now')
    else:
        print('ERROR: OS not supported!')

def restart():
    if platform.system() == "Windows":
        os.system('shutdown -t 0 -r -f')
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system('sudo reboot now')
    else:
        print('ERROR: OS not supported!')

command = input("Use \'r\' for restart and \'s\' for shutdown: ")

if command == "r":
    restart()
if command == "s":
    shutdown()
else:
    print("ERROR: Wrong Letter")
