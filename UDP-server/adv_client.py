'''
Created on 4/08/2010 Using Python version 2.6.3 final on Windows XP
@author: hussain pardawalla

A UDP client for the adv_server.py , i.e. the mistakingly named 
advanced UDP server program. This CLIENT is capable of checking
whether a given port is free, and also sending a kill request 
in order to terminate the server. The Client either sends a kill 
message or multiple messages, and then receives a corresponding 
number of messages from the server, prints them out and exits. 

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
import string
import copy

# creating a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# storing the server host and port address
srv_ip = sys.argv[1] # server IP address
srv_port = int(sys.argv[2]) # server port
srv_addr = (srv_ip, srv_port)

#binding the socket to a port
client_port = 1500
while client_port < 2000:
    try:
        udp_socket.bind(('' , client_port))
        # You may want: serversocket.bind((socket.gethostname(), port))
    except socket.error as e:
        if e.errno == 10048: # believe that this error is given if socket is in use in case of UDP
            client_port = client_port+1
        else:
            raise
    else:
        break
# END OF while client_port < 2000: LOOP

print 'client socket bound to port number ' + str(client_port)

if len(sys.argv) > 3 and sys.argv[3] == "kill":
  udp_socket.sendto(sys.argv[3], srv_addr) # terminate server
  #receiving messages for the server
  srv_data, srv_addr = udp_socket.recvfrom(1024)# receive data of 1024 bytes
  print '\n' + 'CLIENT sending ' + sys.argv[3] + ' request from port number ' + str(client_port)
  print srv_data
  print 'Server IP address is ' + srv_addr[0]
  print 'Server Port number is ' + str(srv_addr[1]) + '\n\n'
else:
  for i in range(1001):
    #sending a message to the server
    server_request_msg = 'Pls send server info, this is Request number ' + str(i) 
    udp_socket.sendto(server_request_msg, srv_addr)
    
    #receiving messages for the server
    srv_data, srv_addr = udp_socket.recvfrom(1024)# receive data of 1024 bytes
    print '\n' + 'request number ' + str(i) + ' from CLIENT from port number for SERVER info' + str(client_port)
    print srv_data
    print 'Server IP address is ' + srv_addr[0]
    print 'Server Port number is ' + str(srv_addr[1])
    print '\n\n'
  #END OF for i in range(num): STATEMENT
#END OF if string.lowercase(sys.argv[3]) == 'q':, else STATEMENT
  
# closing the socket
udp_socket.close()