import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sckt.bind((HOST, PORT))
sckt.listen()
conn, addr = sckt.accept()
state = "open"
while state != "closed":
    data = conn.recv(1024)
    if(data):
        print("received data", data)
        state = data
    # conn.sendall(data)
