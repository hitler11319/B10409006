from socket import *

serverPort = 10000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("server start\n----------")

while 1:
	connectionSocket, addr = serverSocket.accept()
	msg = connectionSocket.recv(2048)
	deal_msg = msg.upper()
	connectionSocket.send(deal_msg)
	print("successful\n----------")
	connectionSocket.close()