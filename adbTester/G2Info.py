import os
import sys
import time
import GPU_Info
import CPU_Info
import myPrint

if __name__=='__main__':
    while 1:
        info = {}
        info.update(GPU_Info.getBusy())
        info["=============CPU温度"]="============="
        info.update(CPU_Info.getTemp())
                    
        os.system('clear')
        for key in info:
            print(key+":"+info[key])

        time.sleep(0.5)