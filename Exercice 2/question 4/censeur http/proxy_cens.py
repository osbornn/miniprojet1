from socket import *
from pathlib import *

proxyPort = 6789
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.bind(('', proxyPort))

clientSocket.listen(1)

serverPort = 7891
serverName = "127.0.0.1"

print('Proxy')

def recv_until(cs, c):
    received = ""
    while True:
        new = cs.recv(4096).decode('utf-8')
        if not new:
            return received
        received += new
        if new.find(c):
            return received.split(c, 1)[0]

forbidden_files = ["test1.html", "test2.html"]

def isForbidden(filename):
    denied = False
    for f in forbidden_files:
        if f == filename:
            denied = True
    return denied

while True:
    connectionSocket, address = clientSocket.accept()
    print("OK")

    dataClient = recv_until(connectionSocket, '\n')
    filename = str(Path(dataClient.split(' ')[1].lstrip("/")))
    
    if isForbidden(filename):
        file = open("default.html", 'rb')
        print('Try this')
        file_data = file.read(4096)
        print(file_data)
        connectionSocket.sendall(b"HTTP/1.1 200 OK\nServer : Python HTTP Server\nConnection : close\r\n\r\n" + file_data)
    else:
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.connect((serverName, serverPort))
        serverSocket.send(dataClient.encode('utf-8'))
        dataServer = serverSocket.recv(4096)
        connectionSocket.sendall(dataServer)
        
    

