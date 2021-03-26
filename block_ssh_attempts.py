#!/usr/bin/python3.6

import fwblock

sshdlog_file = open('sshdlog', 'r')

FileLines = sshdlog_file.readlines()

InvalidList = []

for line in FileLines:
    if line.__contains__('Invalid user'):
        InvalidList.append(line)
        
IPList = []

for line in InvalidList:
    ItemsInList = line.split(" ")
    IP = ItemsInList[-3]
    IPList.append(IP)

IPs= set(IPList)

for i in IPs:
    aantal = 0
    for j in IPList:
        if i == j:
            aantal = aantal + 1
    if aantal >= 3:
        fwblock.block_ip(i)
        print(i,aantal)
        print('-'*70)
