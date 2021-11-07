from socket import *
from threading import *

proxyPort = 1234
clientSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 5678
serverName = "127.0.0.1"

clientSocket.bind(('', proxyPort))

clientSocket.listen(1)

def handle_client(clientSocket):
    while True:
        receivedClient = clientSocket.recv(4096)
        if not receivedClient:
            clientSocket.close()
        if receivedClient:
            serverSocket = socket(AF_INET, SOCK_STREAM)
            serverSocket.connect((serverName, serverPort))
            serverSocket.send(receivedClient)
            dataServer = serverSocket.recv(4096)
            clientSocket.send(dataServer)


print('Proxy ready')

while True:
    connectionSocket, address = clientSocket.accept()
    print("Received")

    Thread(target=handle_client, args=(connectionSocket, )).start()
