#!/usr/bin/env python3
#   Author:		Venus Velazquez
#	Major:		CS
#	Due Date:	Oct. 31, 2023
#	Course:		CSC328 020
#	Assignment:	Socket programming
#	Filename:	project5.py
#	Purpose: 	This client program reads word data from a server

import struct
import sys
import socket

# Description: 
# Parameters:  
# Returns: 
def check_args():
    # check for number of arguments
    num_args = len(sys.argv)

    # args will be <host> <port>
    if num_args == 3:

        host = sys.argv[1]
        port = sys.argv[2]

        if not isinstance(host, str): 
            print("Error: expected string for <host>")
            sys.exit(-1)

        if not port.isdigit():
            print("Error: expected integer for <port>")
            sys.exit(-1)
        else:
            port = int(port)

        # if port < 10000 or port > 65535:
        #     print("Error: expected <port> from 10000 to 65535")
        #     sys.exit(-1)
    else:
        print("Error: expected 2 arguments\n")
        print("Usage: script <host> <port>")
        sys.exit(-1)

    return (host, port)

# Description: 
# Parameters:  
# Returns:  
def conn_socket(host, port):

    try:
        # creation & connection of socket
        client_socket = socket.create_connection((host, port))
        print("Socket connection successful\n")
        print("Local address: ", client_socket.getsockname())
        print("Remote address: ", client_socket.getpeername())

        # return socket object
        return (client_socket)
    
    except socket.error as e:
        print("Socket error: ", e)
        sys.exit(-1)
    except Exception as err:
        print("An error occurred: ", err)
        sys.exit(-1)


# Description: Converts 2 bytes to an integer
# Parameters:  n/a
# Returns:     int - the converted integer  
def bytes_to_int():
    # bytes
    byte_data = b'\x01\x02'

    if len(byte_data) == 2:
        try:
            # unpack the bytes as an integer
            integer = struct.unpack('>H', byte_data)[0]
        except struct.error as e :
            print("Error trying to unpack bytes: ", e.strerror)
            sys.exit(-1)
    else:
        print("Error: Byte data size does not match expected size.")
        sys.exit(-1)

    return integer

# Description: 
# Parameters:  
# Returns: 
def read_word_packets(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print("Received: ", data, "\n")


if __name__ == "__main__":

    # host and port 
    conn_data = check_args()

    print("Arguments: ", conn_data[0], conn_data[1])

    # socket connected to server
    client_socket = conn_socket(conn_data[0], conn_data[1])

    read_word_packets(client_socket)

    if client_socket:
        # client_socket.send(b'\x01\x02')
        # data = client_socket.recv(1024)
        client_socket.close()

    print(bytes_to_int())
    