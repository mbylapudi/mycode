#!/usr/bin/env python3
def main():
    switch = {'hostname':'sw1', 'ip':'1.1.1.1', 'version':'1.2', 'vendor': 'Cisco'}
    print(switch['hostname'])
    print(switch['ip'])
    print("test # 1:" + str(switch.get('lynx')))
    print("test # 2:" + str(switch.get('lynx', "This is a big mess")))
    print("test # 3:" + str(switch.get('version')))
    #print(4th test - .keys()")
    print("test # 4 Keys-test:" + str(switch.keys()))
    print("test # 5 Values-test:" + str(switch.values()))
    print("test # 6 - popTest:" + str(switch.pop('version')))
    print("test # 7 - Add a new value")
    switch['adminLogin'] = 'admin'
    print(switch.keys())
    print(switch.values())
main()
