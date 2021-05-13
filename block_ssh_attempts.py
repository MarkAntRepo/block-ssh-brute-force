#!/usr/bin/python3.6

import getopt
import sys
import fwblock

script_args = sys.argv[1:]
option_string = 'hvn:v'
opts, extra_args = getopt.getopt(script_args, option_string)

for option, option_arg in opts:
    if option == '-h':
        print('Your options are -h(for help)', '\n' ,'-v(shows ips that would be blocked but a file needs to be loaded with -n "file name")','\n', "-n(reads file but doesn't call the block_ip function can be combined with -v to show what ips would be blocked)")
        sys.exit(1)
    elif option == '-v':
        ips = []
        ItemsInLine = []
        for line in log_file.readlines():
            if line.__contains__('Invalid user'):
                ItemsInLine = line.split(" ")
                ip = ItemsInLine[-3]
                ips.append(ip)
         
        IPList = set(ips)
         
        for i in IPList:
            aantal = 0
            for j in ips:
                if i == j: 
                    aantal = aantal + 1
            if aantal >= 3:
                fwblock.block_ip(i)
                print('Blocking',i,aantal)
                print('-' * 70)


    elif option == '-n':
        try:
            log_file = open(str(option_arg),'r')
        except FileNotFoundError as err:
            sys.stderr(str(err))
    else :
        sys.stderr(option, "doesn't exist for more information use option -h")
        sys.exit(1)
