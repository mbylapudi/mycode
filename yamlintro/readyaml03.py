#!/usr/bin/env python3
import yaml
def main():
    yammyfile = open("/home/student/mycode/yamlintro/myyaml.yml", "r")
    pyyammy = yaml.load(yamfile)
    yammyfile.close()
    print(pyyammy)
    pyyammy[0]['apps'].append('minecraft')
    print(pyyammy)
    yamlfile2 = open("/home/student/mycode/yamlintro/myyaml.yml.updated", "w")
    yaml.dump(pyyammy, yamlfile2)
    yamlfile2.close()
main()    


