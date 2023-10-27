#!/usr/bin/env python3
#   Author:		Venus Velazquez
#	Major:		CS
#	Due Date:	Oct. 31, 2023
#	Course:		CSC328 020
#	Assignment:	Socket programming
#	Filename:	project5.py
#	Purpose: 	This client program reads word data from a server

import struct

# Description: Converts 2 bytes to an integer
# Parameters:  n/a
# Returns:     int - the converted integer  
def bytes_to_int():
    # bytes
    byte_data = b'\x01\x02'

    # unpack the bytes as an integer
    integer = struct.unpack('>H', byte_data)[0]

    return integer


if __name__ == "__main__":
    print(bytes_to_int())
    