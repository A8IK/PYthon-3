import socket

c = socket.socket()

c.connect(('localhost',5555))


name = input("Enter your name :")  ##This line is ask for the user to enter your name
c.send(bytes(name,'utf-8'))     ##here we are taking name and send it to server


print(c.recv(1024).decode())