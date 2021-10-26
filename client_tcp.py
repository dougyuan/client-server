# client_tcp.py
# ----------------------------------------------------------------
# Douglas Yuan for CS176A HW3
# Adaptation of sample code 'tcp_client.py' 
# from discussion section by Atefeh.

import sys
# Socket programming library:
from socket import *

# Set PORT IP
HOST = sys.argv[1]   # means "local host" (The server's hostname or IP address)
PORT = int(sys.argv[2])   # The port used by the server
FORMAT = 'utf-8'
SIZE = 2048

# Set up the socket
# Socket handler: Socket(family, socket type)
# Family: AF_INET IPv4 protocol, AF_INET6 IPv6 protocol
# Type: 
## SOCK_STREAM reliable, 2-way, connection-based service
## SOCK_DGRAM unreliable, connectionless

s = socket(AF_INET, SOCK_STREAM)
# TCP need to ask for connect first
s.connect((HOST, PORT))

# Send data to server
message = input("Enter string: ")
s.send(message.encode())

# Receive Response back from Server

while(True):
    bufsize = s.recv(4).decode()
    recvMessage = s.recv(int(bufsize))
    print("From server:", recvMessage.decode(FORMAT))
    if(len(recvMessage.decode(FORMAT)) == 1 or not recvMessage.isdigit()):
        break
    else: 
        continue
s.close()