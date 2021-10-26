# server_tcp.py
# ----------------------------------------------------------------
# Douglas Yuan for CS176A HW3
# Adaptation of sample code 'tcp_server.py' 
# from discussion section by Atefeh.

import sys
# Socket programming library:
from socket import *

def sendMessage(s, m):
    outgoing = m.encode()
    s.send(str(len(m)).zfill(4).encode())
    s.send(outgoing)

# Set PORT and IP info
PORT = int(sys.argv[1])   # Port
HOST = "127.0.0.1"   
FORMAT = 'utf-8'
SIZE = 2048

# Initalize TCP socket
s = socket(AF_INET, SOCK_STREAM)

# For test purpose only, allow reuse addr
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Bind socket to port and connect
s.bind(("", PORT))

# Listen to the any requests might come from clients
s.listen()

# Accept TCP Client's Connection Request
connected = True

# Retrieve client message and send appropriate response
while connected:
	conn, addr = s.accept()
	message = conn.recv(SIZE)
	if message:
		modMessage = message.decode(FORMAT)
		# Check message
		if(not modMessage.isdigit()):
			responseMessage = "Sorry, cannot compute!"
			sendMessage(conn, responseMessage)
		else:
			while(len(modMessage) > 1):
				messageSum = str(sum(map(int, modMessage)))
				modMessage = messageSum
				sendMessage(conn, messageSum)

			sendMessage(conn, modMessage)	
	continue
