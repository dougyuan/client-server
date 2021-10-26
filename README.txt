README.txt
---------------------------------------------------------
Douglas Yuan for CS176A HW3

This documentation is in accompaniment of four programs: 'server_udp.py', 
'client_udp.py', 'server_tcp.py', and 'client_tcp.py'.
It describes my approach to implementing both client/server pairs. Much of 
this code was adapted from Animesh's sample code from discussion section, 
including strategies to set up port and IP info, read user input, open and 
close connections, and encode and decode messages. This adaptation is clearly
visible in the general layout of each file. Also, I drew inspiration from Lucas
Lopilato's implementation of a TCP client-server. His program used a user-defined 
'sendMessage' function that I adapted for use in 'server_tcp.py'. Lucas' code is
viewable at https://github.com/lucaslopilato/Client-Server/blob/master/server_python_tcp.py

---------------------------------------------------------
UDP Client (client_udp.py)
---------------------------------------------------------
This file represents the client side of a UDP connection. Responsibilities begin
with the client, which first sets up a UDP socket for data transfer. As the UDP
client doesn't need to request a connection before transferring, it immediately 
reads in an input string, encodes it, and sends it to the server. The client then 
monitors for any response from the server. Upon receiving one, it decides whether
the decoded response is numeric or not. If it is numeric the client prints the 
incoming message, and all proceeding messages until the message is a single digit, 
upon which the client closes the socket. If the reponse isn't numeric, the client
prints the incoming message and promptly closes the socket, as it must be the case 
that an error message was communicated.

---------------------------------------------------------
UDP Server (server_udp.py)
---------------------------------------------------------
This file represents the server side of a UDP connection. The server initializes the
socket connection using a user-specified port number, binds the socket to said port,
and continually listens for incoming client messages. Upon receiving one, it decides 
whether the decoded message is numeric or not. If it isn't numeric, the server sends
an error message to the client. If it is numeric, the program determines if the message
string has length greater than 1. If so, it enters a while loop that forms a sum of the 
digits of the string, messageSum, and sends this sum to the client at each iteration. 
After it is sent, the message string takes the value of its sum, decreasing the length of
the string for the next iteration. Once the string is of single-digit length, it is sent 
to the client as the final response regarding the message string.

---------------------------------------------------------
TCP Client (client_tcp.py)
---------------------------------------------------------
This file represents the client side of a TCP connection. Responsibilities begin
with the client, which first sets up a TCP socket for data transfer. Then, it asks
for a connection with the TCP server, reads an input string, encodes it, and sends it
to the server. The client then monitors for responses from the server. Upon receiving one,
it first reads a string of 4 bits indicating how many bytes the incoming response contains. 
The client then reads in this exact amount from the input buffer, decodes the response, and
prints the response. It does this continually until either the response length is one digit 
or the response is non-numeric (which connotes an error message).

---------------------------------------------------------
TCP Server (server_tcp.py)
---------------------------------------------------------
This file represents the server side of a TCP connection. It begins with a sendMessage function.
It specifies that before a reponse message is sent to the client, the buffer size of the 
message is sent through a 4 digit string. Now, like the UDP server, the TCP server initializes 
the socket connection using a user-specified port number, binds the socket to said port,
and continually listens for incoming client communication. The initial communication is
the handshake, upon which the server accepts and establishes a connection. Upon receiving 
a client message, the server decides whether the decoded message is numeric or not. If it 
isn't numeric, the server sends an error message to the client. If it is numeric, the program 
determines if the message string has length greater than 1. If so, it enters a while loop that 
forms a sum of the digits of the string, messageSum, and sends this sum to the client at each 
iteration. After it is sent, the message string takes the value of its sum, decreasing the length
of the string for the next iteration. Once the string is of single-digit length, it is sent to 
the client as the final response regarding the message string. It is worth noting that the TCP 
server does not terminate after this one conversation, but continually monitors to accept any 
further requests by the client.

