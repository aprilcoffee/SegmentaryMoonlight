import RPi.GPIO as GPIO
import time
import datetime
from random import randint
import sc2
import socket
import subprocess
import os
import signal
sc2.init()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket Created")

host = '127.0.0.1'
port = 12345
time.sleep(5)
s.connect((host,port))

i = 0
mode = 2

playing = 0 
while True:
    if mode == 0:
        data = s.recv(1024)
        if data:
            print("Receive Data: %s" % str(data.decode('utf-8')))
            mode=mode+1
    elif mode ==1:
        mode=mode+1
    elif mode ==2:
        data = "Hi"
        if playing == 0:
            #pro = subprocess.Popen(["omxplayer", "House.mp3", "-ss", "0"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
            #pro= subprocess.Popen(["omxplayer", "House.mp3", "-ss", "0"]    , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            pro = subprocess.Popen(['omxplayer', '-o', 'local', 'House.mp3'])
            playing = 1
        time.sleep(0.145)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.168)
        s.sendall(data.encode('utf-8'))
        time.sleep(1.514)
        #pro.kill()
        #pro = subprocess.Popen(['omxplayer', '-i', 'House.mp3'])

        s.sendall(data.encode('utf-8'))
        time.sleep(0.364)
        s.sendall(data.encode('utf-8'))
        time.sleep(1.052)
        s.sendall(data.encode('utf-8'))
        time.sleep(4.467)
        s.sendall(data.encode('utf-8'))
        time.sleep(1.511)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.367)
        s.sendall(data.encode('utf-8'))
        time.sleep(5.066)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.147)
        s.sendall(data.encode('utf-8'))
        time.sleep(3.088)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.462)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.936)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.96)
        s.sendall(data.encode('utf-8'))
        time.sleep(1.755)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.957)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.932)
        s.sendall(data.encode('utf-8'))
        time.sleep(1.387)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.48)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.938)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.912)
        s.sendall(data.encode('utf-8'))
        time.sleep(1.583)
        s.sendall(data.encode('utf-8'))
        time.sleep(1.137)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.939)
        s.sendall(data.encode('utf-8'))
        time.sleep(1.611)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.264)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.934)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.912)
        s.sendall(data.encode('utf-8'))
        time.sleep(2.196)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.526)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.924)
        s.sendall(data.encode('utf-8'))
        time.sleep(1.871)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.941)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.947)
        s.sendall(data.encode('utf-8'))
        time.sleep(2.726)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.936)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.314)
        s.sendall(data.encode('utf-8'))
        time.sleep(1.532)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.919)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.944)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.315)
        s.sendall(data.encode('utf-8'))
        time.sleep(2.401)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.94)
        s.sendall(data.encode('utf-8'))
        time.sleep(1.409)
        s.sendall(data.encode('utf-8'))
        time.sleep(1.833)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.454)
        s.sendall(data.encode('utf-8'))
        time.sleep(2.753)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.941)
        s.sendall(data.encode('utf-8'))
        time.sleep(1.824)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.941)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.933)
        s.sendall(data.encode('utf-8'))
        time.sleep(2.777)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.898)
        s.sendall(data.encode('utf-8'))
        time.sleep(1.609)
        s.sendall(data.encode('utf-8'))
        time.sleep(1.207)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.887)
        s.sendall(data.encode('utf-8'))
        time.sleep(2.758)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.947)
        s.sendall(data.encode('utf-8'))
        time.sleep(1.625)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.204)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.934)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.948)
        s.sendall(data.encode('utf-8'))
        time.sleep(2.717)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.927)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.372)
        s.sendall(data.encode('utf-8'))
        time.sleep(1.503)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.325)
        s.sendall(data.encode('utf-8'))
        time.sleep(1.519)
        s.sendall(data.encode('utf-8'))
        time.sleep(2.743)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.933)
        s.sendall(data.encode('utf-8'))
        time.sleep(1.624)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.208)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.943)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.935)
        s.sendall(data.encode('utf-8'))
        time.sleep(2.782)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.878)
        s.sendall(data.encode('utf-8'))
        time.sleep(3.718)
        s.sendall(data.encode('utf-8'))
        time.sleep(1.034)
        s.sendall(data.encode('utf-8'))
        time.sleep(0.367)
        s.sendall(data.encode('utf-8'))
        time.sleep(3.0)
        s.sendall(data.encode('utf-8'))
        time.sleep(3.0)
        s.sendall(data.encode('utf-8'))
        time.sleep(8.319)
        s.sendall(data.encode('utf-8'))
        time.sleep(5.027)
        data = "end"
        mode = 0
        playing = 0
        #os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
        #pro.kill()
        pro = subprocess.Popen(['omxplayer', '-i', 'House.mp3'])
        s.sendall(data.encode('utf-8'))
conn.close()
