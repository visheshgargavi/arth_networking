import socket
import os
import time
import threading

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

ip = "192.168.43.43"
port = 1234

s.bind((ip , port))
def a():
    while True:
        x = s.recvfrom(1024)
        clientip = x[1][0]
        data = x[0].decode()
        print(clientip + ":" + data)
        #time.sleep(120)
        #print(os.system(data))

def b():
    while True:
        x = s.recvfrom(1024)
        clientip = x[1][0]
        data = x[0].decode()
        print(clientip + ":" + data)
        #time.sleep(120)
        #print(os.system(data))


x1 = threading.Thread( target=a )
x2 = threading.Thread( target=b )

x1.start()
x2.start()

