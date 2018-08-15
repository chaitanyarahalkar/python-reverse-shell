# test comment
import socket
import os 
import sys 

host = ''
port = 3335

# Establishing a socket connection with the client 

global s
s = socket.socket() 
s.bind((host,port))

s.listen(5)
c,addr = s.accept()

while True:
	cmd = input("->")
	if cmd == "quit":
		c.send(str.encode("quit"))
		print("Closing connection ...")
		break 
	# Accepting a connection from the client socket 
	c.send(str.encode(cmd))
	get_resp = str(c.recv(4096), "utf-8")
	print(get_resp)

s.close()
	
	