#!/usr/bin/env python
import urllib.request
import json
import webbrowser
import pprint
def main():
    NASAAPI = 'https://api.nasa.gov/planetary/apod?'
    MYKEY = 'api_key=1TBGsSglJmeZEYaIAJtuwToehC4Rgv7lCZQjhjf5'
    nasaapiobj = urllib.request.urlopen(NASAAPI+MYKEY)
    nasaread = nasaapiobj.read()
    convertedjson =  json.loads(nasaread.decode('utf-8'))
    print(convertedjson)
    input('This is converted json. Press to continue')
    #pp(convertedjson)
    pprint.pprint(convertedjson)
    print(convertedjson['explanation'])
#    print("\nPress Enter to open NASA")
    webbrowser.open(convertedjson['url'])
main()    
