import sys
import codecs

from lib.badge import Badge

sys.stdout = codecs.open('/dev/stdout', 'w', 'utf8')

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print "USAGE: cat FILE | python expo.py <PREFIX>"
    sys.exit(1);

  prefix = sys.argv[1];

  print 'AGUARDANDO ENTRADA...';
  while True:
    print "FORMATO: id,count,text,name<enter>";
    line = sys.stdin.readline()
    if len(line.strip()) == 0:
      print '*** empty, quitting'
      break;
    if line.startswith("#"):
      print "*** pulando " + line;
      continue;
    if line.strip() == u"exit":
      print "*** exit";
      break;
    if line.strip() == u'repeat':
      id, count, text = last;
    else:
      id, count, text = last = line.strip().split(",");

    xid = "{}-{}".format(prefix, id)
    count = int(count)

    for i in range(0,count):
      print "*** imprimindo copia 1"
      Badge(xid, text, 'expositor', '')
