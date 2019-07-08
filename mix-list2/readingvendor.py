#!/usr/bin/env python3
"""using csv data"""
import csv

def main():
    with open ("vendor.csv", "r") as vendorfile:
        vendata = csv.reader(vendorfile, delimiter=",")
        count = list(vendata)
        rowCount = len(count)
#        print(count)
         for row in vendata:
            print("The IP address " + row[2] + " requires the driver " + row[3])
            #print(row[1], row[2], row[3])

main()
