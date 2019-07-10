#!/usr/bin/env python3
import urllib.request
import requests
import json
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
    startdate = 'start_date=2018-06-01'
    enddate = '&end_date=END_DATE'
    mykey = '&api_key=1TBGsSglJmeZEYaIAJtuwToehC4Rgv7lCZQjhjf5'
    neourl = neourl + startdate + mykey
    neojson=(requests.get(neourl)).json()
    print(neojson)
main()    
