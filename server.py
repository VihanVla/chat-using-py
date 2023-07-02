import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#the first one it means we want to use ipv4 and the second one means we use tcp 

s.bind(('',4444))
#sticking whit the IP address and the port

s.listen(1)
#now listen to it(handshake), and how many people to listen

client , address = s.accept()
#print(client)
#print(address)
while True:
    message = input("enter you massage: ")
    client.sendall(message.encode("UTF-8"))
    #getting the massage and send it for client

    cMassage = client.recv(213125)
    print(cMassage.decode("utf-8"))