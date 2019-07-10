#1/usr/bin/env python3
import yaml
def main():
    hit = [{"name":"Zaphod", "Species":"Betel"}, {"name": "Arthur dent", "Secies": "HUman"}]
    print(hit)
    yamstring = yaml.dump(hit)
    print("This is yaml file")
    print(yamstring)
   # zfile = open("galaxyguide.yaml", "w")
 #   yaml.dump(hit, zfile)
#    zfile.close()

main()    
