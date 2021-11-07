from socket import *
from pathlib import *
import time
import datetime
import sys

proxyPort = 5678
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.bind(('', proxyPort))

clientSocket.listen(1)

serverPort = 6789
serverName = "127.0.0.1"

def recv_until(cs, c):
    received = ""
    while True:
        new = cs.recv(4096).decode('utf-8')
        if not new:
            return received
        received += new
        if new.find(c):
            return received.split(c, 1)[0]

print('Proxy')

while True:
    connectionSocket, address = clientSocket.accept()
    print("OK")
    
    dataClient = recv_until(connectionSocket, '\n')
    now = datetime.datetime.now()
    currentTime = now.strftime("%H : %M : %S")

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.connect((serverName, serverPort))
    serverSocket.send(dataClient.encode('utf-8'))
    dataServer = serverSocket.recv(4096)
    connectionSocket.sendall(dataServer)

    file = open("log.txt", "a")
    contentsClient = "Request at " + str(currentTime) + "\n"
    print(contentsClient)
    file.write(contentsClient)
    file.write(dataClient)

    contentsServer = "Response is : " + "\n"
    sizeServer = "Size of the file : " + str(sys.getsizeof(dataServer)) + "\n"
    file.write(sizeServer)
    file.write(contentsServer)
    file.write(dataServer.decode('utf-8') + "\n\n")
    print(sizeServer)
    file.close()

