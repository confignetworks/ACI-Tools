import sys
import logging
import json
from acitoolkit.acitoolkit import Tenant, Context,BridgeDomain,AppProfile, NetworkPool
from acitoolkit.acitoolkit import L2Interface,Session,EPGDomain, PhysDomain, EPG, Interface
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
    tenants = Tenant.get(session)
    
    for tenant in tenants:
        print(tenant.name)
if __name__ == '__main__':
	main()
