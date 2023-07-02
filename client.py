import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('192.168.43.184',4444))

while True:
    sMassage = s.recv(2232154)
    print(sMassage.decode("utf-8"))

    massage = input("now you enter your massage: ")
    s.sendall(massage.encode("utf-8"))
