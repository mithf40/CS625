#!/usr/bin/python

from pwn import *

# check byte, by looking at parity bit
def is_valid(data, par):
    return not ((data.count('1') % 2 == 1) ^ (par == '0'))

r = remote("cseproj91.cse.iitk.ac.in", 8040)
print r.recvuntil("retransmit.\n")

flag = ""
while True:
        frame = r.recv()
        data = frame[1:-3]
        par = frame[-3:-2]

        if is_valid(data,par):
                flag += chr(int(data,2))
                print flag
                if chr(int(data,2)) == "}":
                        break
                r.send("1\n")
        else:
                r.send("0\n")
