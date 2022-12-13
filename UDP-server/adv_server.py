'''
Created on 4/08/2010 Using Python version 2.6.3 final on Windows XP
@author: hussain pardawalla

A mistakingly named advanced UDP server program capable of handling 
multiple client requests, and a kill request to terminate itself

USAGE on Windows
on ONE terminal start the SERVER
>python adv_server.py <server_port>
(i.e. > python adv_server 1313). 
---------------------------------------------------------------------
on the OTHER terminal start the client
>python adv_client.py <server_ip_addr> <server_port> 
(i.e. python adv_client.py 127.0.0.1 1313) - this will get the 
client to send numerous requests to the server for some server
information

OR... 
> >python adv_client.py <server_ip_addr> <server_port> kill
(i.e. python adv_client.py 127.0.0.1 1313 kill) - this will get the 
client to send a SINGLE request to the server for some server
information and then terminate itself after sending the info
---------------------------------------------------------------------

Notes: 
This will only work for UDP sessions, and IPv4
This program is not designed to be robust, i.e. if correct information 
is not given it will result in unspecified actions, (most probably a crash)



'''

import socket
import sys
import platform
import string
import time

buf = 1024 #size of data we can read in at the socket

# create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# storing server hostname and operating system info in the server_info variable
server_info = ('\nA Mistakingly named Advance UDP server by Hussain is running on\n'
               + socket.gethostname()+ ' a ' + platform.system()+ ' ' + platform.release() + ' machine ' )
python_ver_info = (str(sys.version_info[0]) + '.' + str(sys.version_info[1]) + '.' 
                   + str(sys.version_info[2]) + ' ' + sys.version_info[3])

server_data = (server_info + '\n' +
               'Python ' + python_ver_info + ' is being used to run this server')
print server_data

# associate the socket with a port
host = '' # think that this field can be left blank on the server side
port = int(sys.argv[1]) # reading in the port from command line
srv_addr=(host,port)
udp_socket.bind(srv_addr) # binding the socket. 

# keeping the socket alive until a 'kill' string is received to terminate it. 
alive = True
while alive:

  #getting the message from a client and printing it out
  client_data, client_addr = udp_socket.recvfrom(buf)
  print ('from ' + client_addr[0]+ ' ' + str(client_addr[1]) + 
       ' received \n"' + client_data + '" message'
       ' at ' +  time.strftime("%H:%M:%S", time.localtime()) + '\n')

  # sending the client server information
  udp_socket.sendto(server_data, client_addr)
  
  # checking to see if the kill request was sent
  if string.lower(client_data) == "kill":
    print 'Exiting server...'
    alive = False
  #END OF if string.lower(client_data) == "kill": STATEMENT 
  
#END OF while alive: LOOP

# closing the socket connection and exiting
print 'closing UPD socket'
udp_socket.close()