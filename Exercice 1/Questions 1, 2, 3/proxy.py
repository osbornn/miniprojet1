from socket import *

proxyPort = 1234
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.bind(('', proxyPort))

clientSocket.listen(1)

serverPort = 5678
serverName = "127.0.0.1"

print('Proxy')

while True:
    connectionSocket, address = clientSocket.accept()
    print("Received")
    
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.connect((serverName, serverPort))
    dataClient = connectionSocket.recv(2048)
    serverSocket.send(dataClient)

    dataServer = serverSocket.recv(2048)
    connectionSocket.send(dataServer)

