from socket import *
from pathlib import *
import time
import datetime
import sys

proxyPort = 1234
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.bind(('', proxyPort))

clientSocket.listen(1)

serverPort = 5678
serverName = "127.0.0.1"

print('Proxy')

while True:
    connectionSocket, address = clientSocket.accept()
    print("OK")
    
    dataClient = connectionSocket.recv(4096)
    now = datetime.datetime.now()
    currentTime = now.strftime("%H : %M : %S")

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.connect((serverName, serverPort))
    serverSocket.send(dataClient)
    dataServer = serverSocket.recv(4096)
    connectionSocket.sendall(dataServer)

    file = open("log.txt", "a")
    contentsClient = "Request at " + str(currentTime) + "\n"
    print(contentsClient)
    file.write(contentsClient)
    file.write(dataClient.decode('utf-8'))

    contentsServer = "Response is : " + "\n"
    sizeServer = "Size of the file : " + str(sys.getsizeof(dataServer)) + "\n"
    file.write(sizeServer)
    file.write(contentsServer)
    file.write(dataServer.decode('utf-8') + "\n\n")
    print(sizeServer)
    file.close()

