# Script to print the SRX policies and address-book
from jnpr.junos import Device
from pprint import pprint
from lxml import etree
from copy import deepcopy

with Device(host='192.168.100.120', user='lab', password='c0ntrail123!') as devInode:
    pprint (devInode.facts)
    devName = devInode.facts.get('hostname')
    pprint (devName)
    full_cfg = etree.tostring(devInode.rpc.get_config(options={'inherit': 'inherit', 'database': 'committed','format': 'set'}))
    sec_cfg = etree.tostring(devInode.rpc.get_config(filter_xml=etree.XML('<security><policies/></security>'),options={'inherit': 'inherit', 'database': 'committed', 'format': 'set'}))
    addr_cfg = etree.tostring(devInode.rpc.get_config(filter_xml=etree.XML('<security><address-book/></security>'),options={'inherit': 'inherit', 'database': 'committed', 'format': 'set'}))
    dev_data = [sec_cfg, devName, full_cfg, addr_cfg]
    pprint (dev_data)
