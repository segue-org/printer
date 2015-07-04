from lib.badge import Badge
from lib.envelope import Envelope

PREFIXES = {
    'speaker':           'P',
    'proponent':         'N',
    'normal':            'N',
    'promocode':         'N',
    'student':           'S',
    'caravan':           'N',
    'caravan-leader':    'N',
    'proponent-student': 'S'
}

def print_badge(value):
    prefix = PREFIXES.get(value.get('category','normal'),'X')
    xid = "{}-{}".format(prefix, value.get('xid', 0))
    name = value.get('name',None)
    company = value.get('organization',None)
    city = value.get('city', None)
    copies = value.get('copies', 1)
    badge    = Badge(xid, name, company, city, copies)
    envelope = Envelope(xid, name, company, city, 1)
    return badge, envelope;
