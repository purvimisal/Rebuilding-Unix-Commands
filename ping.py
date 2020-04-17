#ping [OPTIONS] DESTINATION 
# PING (Packet Internet Groper) command is used to check the network connectivity between host and server/host. 
# This command takes as input the IP address or the URL and sends a data packet to the specified address with the message “PING” 
# and get a response from the server/host this time is recorded which is called latency.


# This program supports:
# ping -c 4 ip_address (here -c is the option to select number of packets to send to server/host)
# ping ip_address 


import socket
import sys
import os


args = sys.argv[1:]
count = ''
if args[0] == '-c':
    count = '-c '
    count += args[1] + ' '
    server_ip = args[2]
else: 
    server_ip = args[0]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Creating a TCP/IP socket

rep = os.system('ping ' + count + server_ip)


if rep == 0 or rep == 2:
    print ('Server is up.')
else:
    print ('Server is down')
