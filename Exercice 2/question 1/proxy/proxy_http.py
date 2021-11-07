from socket import *
from pathlib import *

proxyPort = 1234
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.bind(('', proxyPort))

clientSocket.listen(1)

serverPort = 5678
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


while True:
    connectionSocket, address = clientSocket.accept()
    print("OK")
    
    dataClient = recv_until(connectionSocket, '\n')
        
    filename = Path(dataClient.split(' ')[1].lstrip("/")) #fonctionnalité de cache du serveur
    print(filename)

    if(filename.is_file()):
        file = open(filename, 'rb')
        dataFile = file.read(4096)
        connectionSocket.sendall(dataFile)
        connectionSocket.close()
    else:
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.connect((serverName, serverPort))
        serverSocket.send(dataClient.encode('utf-8'))
        dataServer = serverSocket.recv(4096)
        print(dataServer)
        connectionSocket.sendall(dataServer)
        file = open(filename, 'wb')
        file.write(dataServer)
        file.close()



