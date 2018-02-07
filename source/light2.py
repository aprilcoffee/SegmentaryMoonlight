import RPi.GPIO as GPIO
import time
import datetime
from random import randint
import sc2
import socket 

sc2.init()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket Created")

host = '10.1.1.13'
port = 1688
time.sleep(5)
s.connect((host,port))

i = 0
mode = 0
while True:
    #sc2.reset(i,1)
    #i = i+1
    #i = i%10
    #sc2.starShine(10)
    """
    data = conn.recv(1024)
    if data:
        print("Receive Data: %s" % str(data.decode('utf-8')))
    else:
        break
    i += 1
    i %= 4
    sc2.reset(i+1,1)
    time.sleep(0.3)
    """
    if mins == 0:
        sc2.showTime()
    else:
        sc2.countDown()
    #time.sleep(0.5)
    #sc.showLeftToRight()
    
conn.close()
