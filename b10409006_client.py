from socket import *

serverName = '192.168.226.1'  #此為當時寫這份作業時先用ipconfig來看我的主機ip
serverPort = 10000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
msg = input("input lowercase msg:\n")
clientSocket.send(msg.encode())
get_msg = clientSocket.recv(2048)
print(get_msg)

clientSocket.close()