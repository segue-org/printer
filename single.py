import sys
import requests
import codecs

sys.stdout = codecs.open('/dev/stdout', 'w', 'utf8')
endpoint = "http://192.168.33.20:2000"

class RangerException(BaseException): pass
class PersonNotFound(RangerException): pass
class NoName(RangerException): pass
class NoTickets(RangerException): pass
class NoValidTickets(RangerException): pass

class Process:
  def __init__(self, id, printer, mode='both'):
    self.url = "{}/people/{}-{}".format(endpoint, source, id)

    self.locate_person(id)
    self.ensure_has_name()
    self.ensure_has_tickets()
    self.ensure_has_valid_tickets()
    if mode in ('badge','both'):
        self.print_badge(printer)
    if mode in ('envelope','both'):
        self.print_envelope(printer);

  def print_badge(self, printer):
    print 'hitting post print-badge'
    response = requests.post("{}/print-badge/{}".format(self.url, printer))
    print response.status_code

  def print_envelope(self, printer):
    print 'hitting post print-envelope'
    response = requests.post("{}/print-envelope/{}".format(self.url, printer))
    print response.status_code

  def locate_person(self, id):
    print "hitting GET", self.url
    response = requests.get(self.url)

    print response.status_code
    if response.status_code >= 400:
      print "PERSON NOT FOUND! skipping"
      raise PersonNotFound()
    self.person = response.json()

  def ensure_has_name(self):
    self.name = self.person['name']
    print u"person name '{}'".format(self.name)
    if len(self.name) == 0:
      raise NoName()

  def ensure_has_tickets(self):
    self.statuses = [ t.get('status') for t in self.person['tickets'] ]
    print "tickets' statuses:", self.statuses
    if len(self.statuses) == 0:
      raise NoTickets()

  def ensure_has_valid_tickets(self):
    def is_valid_status(status):
      return status in ('confirmed', 'paid', 'approved', 'accepted')

    self.is_valid = any(map(is_valid_status, self.statuses))
    if not self.is_valid:
      raise NoValidTickets()


if __name__ == "__main__":
  if len(sys.argv) < 5:
    print "USAGE: python single.py <SOURCE> <MODE> <PRINTER> [id, [id, [ ... ]]]"

  source  = sys.argv[1]
  mode    = sys.argv[2]
  printer = sys.argv[3]
  items   = sys.argv[4:]
  print sys.argv

  results = {'OK':0}

  for id in items:
    try:
      print "-------------------"
      print "iniciando id", id
      p = Process(id, printer, mode);
      results['OK'] += 1
    except RangerException, e:
      name = repr(e).split(".")[-1]
      print "*****", name
      if name not in results:
        results[name] = 0
      results[name] += 1
    except Exception, e:
      name = repr(e).split(".")[-1]
      print "**** ****", name, "**** ****"
      if name not in results:
        results[name] = []
      results[name].append(id)

  print results
