from lib.badge import Badge
from lib.envelope import Envelope

def print_badge(value):
    prefix = value.get('prefix', None) or '?'
    xid = value.get('xid', None) or 0
    name = value.get('name',None)
    company = value.get('organization',None)
    city = value.get('city', None)
    copies = value.get('copies', 1)

    badge    = Badge(prefix, xid, name, company, city, copies)
    if prefix != "VVV":
        envelope = Envelope(prefix, xid, name, company, city, 1)
    return 'ok';
