import RPi.GPIO as GPIO
import time
import datetime
from random import randint
import sc2
import socket
import os
import subprocess

sc2.init()


playing = 0 
while True:
    if playing ==0:
        playing = 1
        player = subprocess.Popen(["omxplayer", "House.mp3", "-ss", "0"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    sc2.showTime()
conn.close()
