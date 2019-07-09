#!/usr/bin/env python3
import urllib.request
import json
MAJORTOM = 'http://api.open-notify.org/astros.json'
def main():
    groundctrl = urllib.request.urlopen(MAJORTOM)
    helmet = groundctrl.read()
    helmetson = json.loads(helmet.decode('utf-8'))
    print("\n\nConverted python data")
    print(helmetson)

    print("\n\nPeople in space:", helmetson['number'])
    people = helmetson['people']
    print(people)

    print("\n\nPeople in space:", helmetson["number"])
    for instances in people:
        print(instances.get('name') + " on the " + instances.get('craft'))
main()
