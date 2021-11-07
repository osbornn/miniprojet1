from socket import *
from pathlib import *

serverPort = 5678
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)

serverSocket.bind(('', serverPort))
serverSocket.listen(3)

print("Server is Ready")


def recv_until(cs, c):
    received = ""
    while True:
        new = cs.recv(4096).decode('utf-8')
        if not new:
            return received
        received += new
        if new.find(c):
            return received.split(c, 1)[0]


def handle_client(cs):
    received = recv_until(cs, '\n')
    filename = Path(received.split(' ')[1].lstrip("/"))
    print(f"{filename} was requested...")

    if not filename.is_file():
        print("... and not found")
        cs.sendall(b"HTTP/1.1 404 Not Found\nServer : Python HTTP Server\nConnection : close\r\n\r\n")
    else:
        print("...and sent successfully!!")
        file = open(filename, 'rb')
        file_data = file.read(4096)
        cs.send(b"HTTP/1.1 200 OK\nServer : Python HTTP Server\nConnection : close\r\n\r\n" + file_data)

        print(file_data)


while True:
    connectionSocket, address = serverSocket.accept()
    handle_client(connectionSocket)

