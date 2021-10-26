# client_udp.py
# ----------------------------------------------------------------
# Douglas Yuan for CS176A HW3
# Adaptation of sample code 'udp_client.py' 
# from discussion section by Atefeh, including 
# strategies to set up port and IP info, read user 
# input, open and close connections, and encode 
# and decode messages. 


#!/usr/bin/env python3
from os import CLD_EXITED
import sys
# Socket programming library:
from socket import *

# Set PORT IP
HOST = sys.argv[1]  # means "local host"
PORT = int(sys.argv[2]) # The port used by the server
FORMAT = 'utf-8'
SIZE = 2048

# Set up the socket
# Socket handler: Socket(family, socket type)
# Family: AF_INET IPv4 protocol, AF_INET6 IPv6 protocol
# Type: 
## SOCK_STREAM reliable, 2-way, connection-based service
## SOCK_DGRAM unreliable, connectionless

s = socket(AF_INET, SOCK_DGRAM)
# UDP does not need to ask for connect 

# Allow string input
message = input("Enter string: ")

# Send specified message to server (expect a response)
s.sendto(message.encode(FORMAT), (HOST, PORT))

# Receive Response back from Server
while(True):
    recvMessage, serverAddress = s.recvfrom(SIZE)
    if(recvMessage.decode(FORMAT).isdigit()):
        print("From server:", recvMessage.decode(FORMAT))
        if(len(recvMessage.decode(FORMAT)) == 1):
            s.close()
            break
    else: 
        print("From server:", recvMessage.decode(FORMAT))
        s.close()
        break
