from socket import *
from threading import Thread

serverPort = 5678

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.bind(('', serverPort))

clientSocket.listen(1)

print("Server Ready")


while True:
    connectionSocket, address = clientSocket.accept()
    print("Connected to server")
    data = connectionSocket.recv(4096)
    print(data.decode('utf-8'))
    connectionSocket.send("test".encode('utf-8'))
    #connectionSocket.send("Ok got your thing".encode('utf-8'))