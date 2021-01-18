#!/usr/bin/python

import socket,sys

host = ""
port = 9999

buffer = b"" # output of pattern create

payload = buffer + b'\r\n'

print("[+] Sending payload...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
s.send(payload)
s.close()
