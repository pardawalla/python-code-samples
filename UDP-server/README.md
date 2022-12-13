This code was written way back in 2010 as part of a test exercise. 


There is a simple and advance version. 

The simple version has the client print out the following information based on the 
communication it receives from the SERVER after sending it a request; 
1.	Who created the server 
2.	Hostname of the machine the server is running on 
3.	The OS on which the server is running on
4.	The python version the server machine is using to run the server
5.	 And finally the IP address and the port number of the server. 
In this version only one client can connect to the server

The advance version of the of the server to be able to handle multiple clients concurrently.

Thus you should be able to run the client from multiple terminals and they should all be able 
to connect at the same time and print out the information from the server.

