import os
import sys
import time

def getTemp():
    cpuInfo = {}
    cpuTypeStr = os.popen('adb shell cat /sys/class/thermal/thermal_zone*/type').read()
    cpuTempStr = os.popen('adb shell cat /sys/class/thermal/thermal_zone*/temp').read()

    cpuType = cpuTypeStr.split('\n')
    cpuTemp = cpuTempStr.split('\n')
    
    #print(cpuType)
    #print(cpuType.index('limits_sensor-00'))
    
    del cpuType[cpuType.index('limits_sensor-00')]
    del cpuType[cpuType.index('limits_sensor-01')]
    
    for i in range(len(cpuType)-1):
        #print(cpuTemp[i])
        temp = int(cpuTemp[i])
        if temp>100 and temp<=10000:
            temp=temp/10

        if temp>10000:
            temp=temp/1000
        cpuTemp[i] = "%.1f" % temp

        cpuInfo[cpuType[i]] = cpuTemp[i]
    
    return cpuInfo