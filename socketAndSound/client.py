import socket 
import time
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '10.254.29.136'
port = 1688

s.connect((host,port))
while True:
	data = "hello Pi"
	s.sendall(data.encode('utf-8'))
	time.sleep(0.1)
