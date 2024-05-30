#!/usr/bin/env python3

# "Author ID: Jihan Kariyawasam"


import subprocess

def free_space():
    free_space = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = free_space.communicate() 
    stdout = output[0].decode('utf-8').strip()
    return stdout

if __name__ == '__main__'
    print(free_space())


