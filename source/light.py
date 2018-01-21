import RPi.GPIO as GPIO
import time
import datetime
from random import randint
import sc
import socket 

sc.init()
#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#host = '10.254.29.136'
#port = 8888
#s.bind((host,port))
#s.listen(5)
#conn,addr = s.accept()

while True:
    """
    data = conn.recv(1024)
    if data:
        print("Receive Data: %s" % str(data.decode('utf-8')))
    else:
        break
    """

    #sc.showTime()
    sc.showLeftToRight()
conn.close()
