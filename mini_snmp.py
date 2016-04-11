#!/usr/bin/python
__author__ = 'Clay'

import claylib
from sys import argv, exit

if len(argv) < 3:
    print('HEY YOU!')
    print('Run it like this: python mini_snmp <fleet name> <target ip>')
    exit()

fleet = argv[1]
target_ip = argv[2]

snmp_prefix = 'snmpget -OvU -v 2c -c'

oids = {'uptime': '.1.3.6.1.2.1.1.3.0',
        'iclMeshPeerMAC': '.1.3.6.1.4.1.388.11.3.9.7.1.1.3.1',
        'iclRadioMAC': '.1.3.6.1.4.1.388.11.3.4.1.1.1.6.2',
        'sysLocation': '.1.3.6.1.2.1.1.6.0',
        'sysName': '.1.3.6.1.2.1.1.5.0'}

if 'acela' in fleet:
    community_string = '<SNIPPED>'
elif 'amfleet' in fleet:
    community_string = '<SNIPPED>'
elif 'cal' in fleet:
    community_string = '<SNIPPED>'
elif 'via' in fleet:
    community_string = '<SNIPPED>'
else:
    community_string = 'public'

for oid in oids:
    command_str = ' '.join([snmp_prefix, community_string, target_ip, oids[oid]])
    response = claylib.local_command(command_str)[0]
    #print(command_str)
    print('OID:%s  |  Result:%s' % (oid, response))
