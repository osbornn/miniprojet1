from socket import *

serverPort = 5678

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(1)

print("Server Ready")

while True:
    connectionSocket, address = serverSocket.accept()
    print("Connected to server")
    data = connectionSocket.recv(2048)
    print(data.decode('utf-8'))
    connectionSocket.close()