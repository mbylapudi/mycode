#!/usr/bin/env python3
def main():

    netlist = [['ios', '10.0.2.1'], ['ios', '10.0.55.1'], ['ios-xr', '10.0.3.1'], ['junos', '10.0.10.1']]

    for dandip in netlist:
        print('SSH to ' + dandip[1] + ' using driver ' + dandip[0])
main()
