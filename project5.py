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
def accept_args():
    # args will be <host> <port>
    args = sys.argv[1:]
    for arg in args:
        # do something here with the args
        print("Argument:", arg )

# Description: 
# Parameters:  
# Returns:  
def connect_socket(host, port):
    # creation & connection of socket
    socket = socket.create_connection(host, port)


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
            print("Error trying to unpack bytes:", e.strerror)
            sys.exit(-1)
    else:
        print("Error: Byte data size does not match expected size.")
        sys.exit(-1)

    return integer


if __name__ == "__main__":
    print(bytes_to_int())
    