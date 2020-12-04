## Server Creating

import socket
s = socket.socket()              ##creating socket
print('Socket Created')         ##We are making that's socket as server socket

s.bind(('localhost',5555))


s.listen(3)
print('waiting for connections')

while True:         ##This is continue process to client
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("Connected with", addr,name)

    c.send(bytes("Welcome to Fox Life",'utf-8'))

    c.close()


