import socket
import os

if os.path.exists("test.s"):
	os.remove("test.s")
unix_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
unix_socket.bind("test.s")
unix_socket.listen(1)
while True:
	connection, address = unix_socket.accept()
	print("This is a client addres {0} ".format(address))
	data = connection.recv(1024)
	print(str(data))
	connection.send(data)
	connection.close()