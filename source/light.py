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
print(conn)
print(addr)
while True:
    data = conn.recv(1024)
    if data:
        print(data)
        recvdata = str(data.decode('utf-8'))
        if recvdata == "end":
            mu.showLeftToRight()
            stringing = "B"
            conn.send(stringing.encode('utf-8'))
        else:
            print("hi")
            mu.rhythm()


conn.close()
