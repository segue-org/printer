import sys
import codecs

from lib.badge import Badge

sys.stdout = codecs.open('/dev/stdout', 'w', 'utf8')

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print "USAGE: cat FILE | python expo.py <PREFIX> <SMALLTEXT> <STARTON>"
    sys.exit(1);

  prefix  = sys.argv[1];
  small   = sys.argv[2]
  starton = int(sys.argv[3])

  current = starton

  print 'AGUARDANDO ENTRADA...';
  while True:
    print "FORMATO: name,corp<enter>";
    line = sys.stdin.readline()
    if len(line.strip()) == 0:
      print '*** empty, quitting'
      break;
    if line.startswith("#"):
      print "*** pulando " + line;
      continue;
    if line.strip() == "exit":
      print "*** exit";
      break;

    line = line.decode('utf-8')
    print line
    if line.strip() == 'repeat':
      name, corp = last;
    else:
      items = line.strip().split(',')
      print items
      name, corp = items
      last = name, corp

    xid = "{}-{}".format(prefix, current)
    current += 1
    print xid, name, corp, small
    Badge(xid, name, corp, small)

