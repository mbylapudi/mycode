#!/usr/bin/env python3
ipchk = input('Apply an IP address')
if ipchk == '1.1.1.1':
    print('IP was set:' + ipchk + 'This is not receomended')
elif ipchk:
    print('IP was set: '+ ipchk )
else:
    print('No input')

