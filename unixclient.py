import socket
import sys

def unixClient() :
	#set timeout
	socket.setdefaulttimeout(10)
	#create socket with TCP protocol
	unix_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
	#connect to target host and port
	unix_socket.connect("test.s")
	#send message to server
	unix_socket.send(b'hello')
	#recover message
	message_from_server = unix_socket.recv(4094)
	#close socket
	unix_socket.close()
	return message_from_server


if __name__ == '__main__':
	print(unixClient())