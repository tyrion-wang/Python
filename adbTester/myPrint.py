import os
import sys
import time

def dic(dic):
    while 1:
        os.system('clear')
        for key in dic:
            print(key+":"+dic[key])

        time.sleep(0.5)