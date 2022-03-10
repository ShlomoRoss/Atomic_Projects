#!/usr/bin/python
import os
import platform
import time

#Create a function to shutdown machine
def shutdown():
    if platform.system() == "Windows":
        os.system('shutdown -s')
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system('sudo shutdown -h now')
    else:
        print('ERROR: OS not supported!')

#Create a function to restart machine
def restart():
    if platform.system() == "Windows":
        os.system('shutdown -t 0 -r -f')
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system('sudo reboot now')
    else:
        print('ERROR: OS not supported!')

#define command
command = input("Use \'r\' for restart and \'s\' for shutdown: ")

#call function for restart
if command == "r":
    print("Restarting machine...")
    time.sleep(3)
    restart()
#call function for shutdown    
if command == "s":
    print("Shutting down...")
    time.sleep(3)
    shutdown()
#Give error for invalid input
else:
    print("ERROR: Invalid input")
