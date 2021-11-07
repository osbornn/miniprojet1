from socket import*

serverName = "127.0.0.1"
serverPort = 1234

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

message = input('Envoyer un message : ').encode('utf-8')
clientSocket.send(message)

response = clientSocket.recv(2048)
print(response.decode('utf-8'))

clientSocket.close()




