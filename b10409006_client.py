from socket import *
import time

serverName = 'localhost'  #此為當時寫這份作業時先用ipconfig來看我的主機ip
serverPort = 10000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
msg = input("input lowercase msg:\n")
clientSocket.send(msg.encode())

get_msg = clientSocket.recv(2048)
print(get_msg.decode())

clientSocket.close()

time.sleep(2)