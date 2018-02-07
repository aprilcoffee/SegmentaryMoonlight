import RPi.GPIO as GPIO
import time
import datetime
from random import randint
import sc
import mu
import socket 

sc.init()
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
host = '10.1.1.10'
port = 1688
s.bind((host,port))
s.listen(5)
sc.reset(10,0)
conn,addr = s.accept()
while True:
    data = conn.recv(1024)
    if data:
        print(data)
        recvdata = str(data.decode('utf-8'))
        if recvdata == "end":
            mu.showLeftToRight()
            stringing = "I'm Rpi"
            conn.send(stringing.encode('utf-8'))
        else:
            mu.rhythm()
    else:
        conn,addr = s.accept()
conn.close()
