import os
import sys
import time

def getBusy():
    gpubusy = os.popen('adb shell cat /sys/class/kgsl/kgsl-3d0/gpubusy').read() #GPU占用
    cpuRate = int(gpubusy[0:8])/int(gpubusy[8:16])*100
    cur_freq = os.popen('adb shell cat /sys/class/kgsl/kgsl-3d0/devfreq/cur_freq').read() #GPU频率
    dict = {'GPU占用率': 1, 'b': 2, 'b': '3'}
    #os.system('clear')
    gpubusy = "%.1f%%" % cpuRate
    cur_freq = "%s" % cur_freq[0:9]
    #print(gpubusy)
    #print(cur_freq)
    #print('\r',"GPU占用率：%.1f%%   GPU频率：%s" % (cpuRate, cur_freq[0:9]), end='')
    gpuInfo = {'GPU占用率': gpubusy, 'GPU频率': cur_freq}
    return gpuInfo