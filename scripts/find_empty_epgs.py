#!/usr/bin/python3

import requests
import json
import pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

APIC_URL = 'https://apic1.vismait.no'
CREDENTIALS = {
    "aaaUser": {"attributes": {"name": "admin", "pwd": "xxxxx"}}
}

try:
    LOGIN = requests.post(APIC_URL+'/api/aaaLogin.json', data=json.dumps(CREDENTIALS), verify=False)
    EPGS = requests.get(APIC_URL+'/api/node/class/fvAEPg.json', cookies=LOGIN.cookies, verify=False)
    ENDPOINTS = requests.get(APIC_URL+'/api/node/class/fvCEp.json', cookies=LOGIN.cookies, verify=False)
except Exception as E:
    print(E)

epgs = []
has_endpoints = []

for EPG in EPGS.json()['imdata']:
    #print(EPG['fvAEPg']['attributes']['dn'])
    epgs.append(EPG['fvAEPg']['attributes']['dn'])

for EP in ENDPOINTS.json()['imdata']:
    #clear mac addresses from output, last 22 characters
    epg = EP['fvCEp']['attributes']['dn'][:-22]
    if epg not in has_endpoints:
        has_endpoints.append(epg)

#Remove default epgs, no need to check epgs in tenant infra.
epgs.remove('uni/tn-infra/ap-ave-ctrl/epg-ave-ctrl')
epgs.remove('uni/tn-infra/ap-access/epg-default')

print('No mac addresses: ')
for epg in set(epgs) - set(has_endpoints):
    print(epg)
