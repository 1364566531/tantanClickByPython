#!/bin/bash
while true
do
    adb shell input swipe 250 600 700 600
    sleep 1 
    adb shell input swipe 400 600 250 600 
    sleep 1 
done
