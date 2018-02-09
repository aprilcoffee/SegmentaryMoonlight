import RPi.GPIO as GPIO
import time
import datetime
from random import randint
import sc
import socket 
import mu
sc.init()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
host = '127.0.0.1'
port = 12345
s.bind((host,port))
s.listen(5)
sc.reset(10,0)
conn,addr = s.accept()
while True:
    data = conn.recv(1024)
    if data:
        recvdata = str(data.decode('utf-8'))
        if recvdata == "end":
            mu.showLeftToRight()
            conn.send(stringing.encode('utf-8'))
            stringing = "B"
        else:
            mu.rhythem()


conn.close()
