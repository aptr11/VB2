#!/usr/bin/python3

import requests
import json
import pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

APIC_URL = 'https://apic1.vismait.no'
CREDENTIALS = {
    "aaaUser": {"attributes": {"name": "readonly", "pwd": "u4nDs2AAtq91x"}}
}


try:
    LOGIN = requests.post(APIC_URL+'/api/aaaLogin.json', data=json.dumps(CREDENTIALS), verify=False)
    physL3outs = requests.get(APIC_URL+'/api/node/class/l3extRsPathL3OutAtt.json', cookies=LOGIN.cookies, verify=False)
    vmmL3outs = requests.get(APIC_URL+'/api/node/class/l3extVirtualLIfP.json', cookies=LOGIN.cookies, verify=False)
except Exception as E:
    print(E)

print('\nInterfaces facing vmware: ')
for interface in vmmL3outs.json()['imdata']:
    tenant = interface['l3extVirtualLIfP']['attributes']['dn'].split('/')[1]
    l3out = interface['l3extVirtualLIfP']['attributes']['dn'].split('/')[2]
    vlan = interface['l3extVirtualLIfP']['attributes']['encap']
    ip = interface['l3extVirtualLIfP']['attributes']['addr']
    print(f'{tenant},\t{l3out},\t{vlan},\t{ip}')


#/api/node/class/l3extRsPathL3OutAtt.json
#print('\nInterfaces facing physical routing elements: ')
#for interface in physL3outs.json()['imdata']:
#    tenant = interface['l3extRsPathL3OutAtt']['attributes']['dn'].split('/')[1]
#    l3out = interface['l3extRsPathL3OutAtt']['attributes']['dn'].split('/')[2]
#    vlan = interface['l3extRsPathL3OutAtt']['attributes']['encap']
#    ip = interface['l3extRsPathL3OutAtt']['attributes']['addr']
#    print(f'{tenant},\t{l3out},\t{vlan},\t{ip}')




    