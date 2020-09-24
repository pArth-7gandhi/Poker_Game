import time
from tkinter import *
import socket
import pickle

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port=12345
mysock.bind(('',port))
mysock.listen(5)

client1,add1 =mysock.accept()
client1.send('Hello welcome!'.encode('utf-8'))
while 1:
    msg=client1.recv(1024).decode('utf-8')
    print(msg)