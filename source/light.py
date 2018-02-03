import RPi.GPIO as GPIO
import time
import datetime
from random import randint
import sc
import socket 

sc.init()
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
    
    #sc.reset(i+1,1)
    i=i+1
    i=i%9
    #time.sleep(0.2)
    time.sleep(0.05)
    """
    data = conn.recv(1024)
    if data:
        print("Receive Data: %s" % str(data.decode('utf-8')))
    else:
        break
    
    i += 1
    i %= 4
    sc.reset(i+1,1)
    time.sleep(0.3)
    """
    """
    if i < 200: 
        sc.showTime()
    else:
        print(i)
        i = 5
        sc.showLeftToRight()
    """
    sc.showLeftToRight()
conn.close()
