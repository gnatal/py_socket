#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
packet = "open"
sckt.connect((HOST, PORT))
while packet != "closed":
    packet = input("prompt: ")
    packet.strip()
    print(packet)
    sckt.sendall(str.encode(packet))
