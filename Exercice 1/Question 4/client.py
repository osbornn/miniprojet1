from socket import*

serverName = "127.0.0.1"
serverPort = 1234

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.connect((serverName, serverPort))

message = input("Que voulez-vous envoyer? ").encode('utf-8')
serverSocket.send(message)

response = serverSocket.recv(4096)
print(response.decode('utf-8'))

#serverSocket.close()