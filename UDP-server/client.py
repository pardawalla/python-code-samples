'''
Created on 4/08/2010 Using Python version 2.6.3 final on Windows XP
@author: hussain pardawalla

A simple UDP client program that sends a request to the
server, and the prints out the server information it 
receives from ther SERVER to the screen, and then exits.  

USAGE on Windows
First on one terminal type
>python server.py <server_port>
(e.g. >python server.py 2000), this will open and bind a socket 
for the server on port number 2000.  

Second on another terminal type
>python client.py <server_IP_addr> <server_port>
(e.g. >python client.py 127.0.0.1 2000), this tells the client the port #
that should be used to communicated with the server. Also make 
sure that the server is running, before starting the client. 

-------------------------------------------------------------------------------
Output Example on TERMINAL 1
D:\endace>python server.py 2000

Simple UDP server by Hussain using Python 2.6.3 and
is running on andromeda a Windows XP machine
Python 2.6.3 final is being used to run this server
from 127.0.0.1 1500 received send info request

=================================================================================
Output Example on TERMINAL 2 (CLIENT)
D:\endace>python client.py 127.0.0.1 2000


Simple UDP server by Hussain using Python 2.6.3 and
is running on andromeda a Windows XP machine
Python 2.6.3 final is being used to run this server
Server IP address is 127.0.0.1
Server Port number is 2000

--------------------------------------------------------------------------------

Notes: 
This will only work for UDP sessions, and IPv4
This program is not designed to be robust, i.e. if correct information 
is not given it will result in unspecified actions, (most probably a crash)
'''

import socket
import sys

# creating a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# storing the server host and port address
srv_ip = sys.argv[1] # server IP address
srv_port = int(sys.argv[2]) # server port
srv_addr = (srv_ip, srv_port)

#binding the socket to a port
udp_socket.bind(('',1500))

#sending a request message to the server
udp_socket.sendto("send info", srv_addr)

# receiving and printing out the data from the server
srv_data, srv_addr = udp_socket.recvfrom(1024)# receive data of 1024 bytes
print '\n' + srv_data
print 'Server IP address is ' + srv_addr[0]
print 'Server Port number is ' + str(srv_addr[1])
print '\n\n'
  
# closing the socket
udp_socket.close()