'''
Created on 4/08/2010 Using Python version 2.6.3 final on Windows XP
@author: hussain pardawalla

A simple UDP server program that receives a request from the
client prints out the request, and then send the client some 
sever information, and gracefully exits. 

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
This server is not designed to be robust, i.e. if correct information 
is not given it will result in unspecified actions, (most probably a crash)

'''

import socket
import sys
import platform


buf = 1024 #size of data we can read in at the socket

# create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# associate the socket with a port
host = '' # think that this field can be left blank on the server side
port = int(sys.argv[1]) # reading in the port from command line
srv_addr=(host,port)
udp_socket.bind(srv_addr) # binding the socket. 

# gathering information to send over to the client
server_info = ('\nSimple UDP server by Hussain using Python 2.6.3 and' + 
               '\nis running on '+ socket.gethostname()+
               ' a ' + platform.system()+ ' ' + platform.release() + ' machine ' )
python_ver_info = (str(sys.version_info[0]) + '.' + str(sys.version_info[1]) + '.' 
                   + str(sys.version_info[2]) + ' ' + sys.version_info[3])

server_data = (server_info + '\n' +
               'Python ' + python_ver_info + ' is being used to run this server')
print server_data

#getting the message from a client and printing it out
client_data, client_addr = udp_socket.recvfrom(buf)
print ('from ' + client_addr[0]+ ' ' + str(client_addr[1]) + 
       ' received ' + client_data + ' request\n')

# sending the client a message
udp_socket.sendto(server_data, client_addr)

# closing the socket connection and exiting
udp_socket.close()
