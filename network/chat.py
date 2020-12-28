import socket
import os
import time
import threading

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

ip = "192.168.43.43"
ip1 = "192.168.43.158"
port = 1234

os.system("tput setaf 2")
print("\t\t\t\tPikachu Welcomes you...")
os.system("tput setaf 7")
print("\t\t\t\t---------------------")

s.bind((ip , port))
def a():
    while True:
        x = s.recvfrom(1024)
        clientip = x[1][0]
        data = x[0].decode()
        os.system("tput setaf 3")
        print("\n\t\t\t\t\t\t\t " + clientip + ":" + data)
        os.system("tput setaf 1")

        #time.sleep(120)
        #print(os.system(data))

def b():
    while True:
        x = s.recvfrom(1024)
        clientip = x[1][0]
        data = x[0].decode()
        os.system("tput setaf 3")
        print("\n\t\t\t\t\t\t\t " + clientip + ":" + data)
        os.system("tput setaf 1")
        #time.sleep(120)
        #print(os.system(data))

def c():
    while True:
        s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
        os.system("tput setaf 1")
        print()
        x = input()
        os.system("tput setaf 1")
        s.sendto(x.encode(),(ip1,port))


x1 = threading.Thread( target=a )
x2 = threading.Thread( target=b )
x3 = threading.Thread( target=c)

x1.start()
x2.start()
x3.start()

