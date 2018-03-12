# coding: utf-8
import os

import time

'''
 adb shell input swipe 250 600 700 600
 adb shell input tap 440 1200
'''

def simpleSwip():
    for index in range(800):
        os.system("adb shell input swipe 250 600 700 600")
        time.sleep(1)
simpleSwip()