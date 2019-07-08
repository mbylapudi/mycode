#!/usr/bin/env python3
import json

def main():
    with open("ciscoAPIC.json", "r") as jsonfile:
        fog = json.load(jsonfile)
        print("num of instances: " , len(fog['imdata']))
        for instances in fog['imdata']:
            print("FW ver running - ", instances.get('version'))
main()

