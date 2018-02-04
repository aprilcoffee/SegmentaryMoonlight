import time
import datetime
from random import randint
import socket 


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

print("Socket Created")

host = '127.0.0.1'
port = 1688
s.bind((host,port))
s.listen(5)
conn,addr = s.accept()
i = 0

while True:
    
    data = conn.recv(1024)
    if data:
        print("Receive Data: %s" % str(data.decode('utf-8')))
        data = "receiced"
        time.sleep(3)
        conn.sendall(data.encode('utf-8'))
    else:
        conn,addr = s.accept()
        print("still waiting")
    time.sleep(0.5)   
    #sc.showLeftToRight()
    
conn.close()
