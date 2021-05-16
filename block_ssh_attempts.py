#!/usr/bin/python3.6

import getopt
import sys
import fwblock

script_args = sys.argv[1:]
option_string = 'hvn:v'
try:
    opts, extra_args = getopt.getopt(script_args, option_string)
except getopt.GetoptError as e:
    sys.stderr.write(" doesn't exist for more information use option -h")
    sys.exit(1)


def get_ips(LogFile,options):
    try:
        log_file = open(LogFile,'r')
    except FileNotFoundErrot as err:
        sys.stderr.write(str(err))

    ips = []
    ItemsInLine = []
    IpsToBlock = []
    for line in log_file.readlines():
        if line.__contains__('Invalid user'):
            ItemsInLine = line.split(" ")
            ip = ItemsInLine[-3]
            ips.append(ip)
    IPList = set(ips)

    for i in IPList:
        amount = 0
        for j in ips:
            if i == j:
                amount = amount + 1
        if amount >= 3:
            IpsToBlock.append(i)
    return IpsToBlock

if opts == [] and extra_args != []:
    answer = get_ips(sys.argv[1],opts)
    for i in answer:
        fwblock.block_ip(i)

if len(opts) == 1:
    if '-h' in opts[0]:
        print('Your options are -h(for help)', '\n' ,'-v(shows ips that are getting blocked but a file needs to be loaded with -v "file name")','\n', "-n 'file name' doesn't block and doesn't show what would be blocked by adding de option -v  example -n 'file name' -v then it show what would be block but doesn't block it.)")
        sys.exit(1)

    if '-v' in opts[0]:
        answer = get_ips(sys.argv[2],opts)
        for i in answer:
            fwblock.block_ip(i)
            print('blocking',i)

    if '-n' in opts[0]:
        answer = get_ips(sys.argv[2],opts)

elif len(opts) == 2:
    if '-n' in opts[0] and '-v'in opts[1]:
        answer = get_ips(sys.argv[2],opts)
        for i in answer:
            print('blocking',i)
