import RPi.GPIO as GPIO
import time
import datetime
from random import randint
import sc2
import socket 

sc2.init()
"""
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
print("Socket Created")

host = '10.254.29.136'
port = 1688
s.bind((host,port))
s.listen(5)
conn,addr = s.accept()
"""
i = 0
while True:
    
    sc2.reset(i,1)
    i = i+1
    i = i%10
    time.sleep(0.5)
    sc2.starShine(10)
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
    #sc2.showTime()
    
    #sc.showLeftToRight()
    
conn.close()
