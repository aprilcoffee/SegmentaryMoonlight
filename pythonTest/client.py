import socket 
import time
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
port = 1688

s.connect((host,port))
while True:
	#data = "hello Pi"
	#s.sendall(data.encode('utf-8'))
	time.sleep(0.5)

        data = s.recv (1024)
        print("Receive Data: %s" % str(data.decode('utf-8')))

