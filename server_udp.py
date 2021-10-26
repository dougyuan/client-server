# server_udp.py
# ----------------------------------------------------------------
# Douglas Yuan for CS176A HW3
# Adaptation of sample code 'udp_server.py' 
# from discussion section by Atefeh, including 
# strategies to set up port and IP info, read user 
# input, open and close connections, and encode 
# and decode messages. 

import sys
# Socket programming library:
from socket import *

# Set PORT and IP info
PORT = int(sys.argv[1])
SERVER = "127.0.0.1"   
FORMAT = 'utf-8'
SIZE = 2048

#Initalize UDP socket
s = socket(AF_INET, SOCK_DGRAM) 

# Bind socket to port and connect
s.bind((SERVER, PORT))

# No need to accept any connection before receiving data from client 
connected = True

# Retrieve client message and send appropriate response
while connected:
    message, clientAddress = s.recvfrom(SIZE)
    if message:
        modMessage = message.decode(FORMAT)
        #Check message
        if(not modMessage.isdigit()):
            responseMessage = "Sorry, cannot compute!"
            s.sendto(responseMessage.encode(FORMAT), clientAddress)
        else:
            while(len(modMessage) > 1):
                messageSum = str(sum(map(int, modMessage)))
                modMessage = messageSum
                s.sendto(messageSum.encode(FORMAT), clientAddress)     
            s.sendto(modMessage.encode(FORMAT), clientAddress)  
    continue
