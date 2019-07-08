#!/usr/bin/env python3

def main():
    networklists = []
    with open('driverip.txt', 'r') as driverip:
        for sline in driverip:
            networklists.append(sline.rstrip("\n").split(' '))
    print(networklists)
    for dandip in networklists:
        print('ssh to ' + dandip[1] + 'using driver' + dandip[0])
main()
