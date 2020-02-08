import sys
import logging
import json
from acitoolkit.acitoolkit import Session
from acitoolkit.aciphysobject import Node
CONFFILE = 'script-conf.json'
def main(): 
    with open(CONFFILE, 'r') as r:
        conf = json.loads(r.read())

    #login to apic
    session = Session(conf['url'],conf['login'],conf['password'])
    resp = session.login()
    if not resp.ok:
        print('%% Could not login to APIC')
        return
        sys.exit(0)

    nodes = Node.get(session)
    for node in nodes:
        print('=' * 50)
        print('Pod: {}'.format(node.pod))
        print('Node: {}'.format(node.node))
        print('Mode: {}'.format(node.mode))
        print('Model: {}'.format(node.model))
        print('Vendor: {}'.format(node.vendor))
        print('Serial: {}'.format(node.serial))
        
if __name__ == '__main__':
    main()