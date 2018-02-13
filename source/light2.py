import RPi.GPIO as GPIO
import time
import datetime
from random import randint
import sc2
import socket
import subprocess
sc2.init()

i = 0
mode = 2

playing = 0 
while True:

    i=i+1
    i=i%10
    sc2.reset(i,1)
    sc2.showTime()

    time.sleep(0.5)
conn.close()
