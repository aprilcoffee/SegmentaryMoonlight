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
host = '127.0.0.1'
port = 1234
s.bind((host,port))
s.listen(5)
"""
sc.reset(10,0)
while True:
    sc.showLeftToRight()

conn.close()
