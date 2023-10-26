#!/usr/bin/env python3.2

bytes = b'\x00\x05'
integer = int.from_bytes(bytes, byteorder= 'big')
print(integer)