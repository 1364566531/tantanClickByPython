# coding: utf-8
import os

import time

from auto_adb import auto_adb
'''
 adb shell input swipe 250 600 700 600
 adb shell input tap 440 1200
'''
def swip():
    cmd = 'shell input swipe {x1} {y1} {x2} {y2} {duration}'.format(
        x1=250,
        y1=600,
        x2=700,
        y2=600,
        duration=500
    )
    adb = auto_adb()
    adb.run(cmd)
 # swip()


def simpleSwip():
    for index in range(800):
        os.system("adb shell input swipe 250 600 700 600")
        time.sleep(1)
simpleSwip()