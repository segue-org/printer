import sys
import codecs

from lib.badge import Badge

sys.stdout = codecs.open('/dev/stdout', 'w', 'utf8')

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print "USAGE: cat FILE | python expo.py <PREFIX> <SMALLTEXT>"
    sys.exit(1);

  prefix = sys.argv[1];
  small  = '' if len(sys.argv) == 2 else sys.argv[2]

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
    if line.strip() == "exit":
      print "*** exit";
      break;

    line = line.decode('utf-8')
    print line
    if line.strip() == 'repeat':
      id, count, text, name = last;
    else:
      items = line.strip().split('\t')
      print items
      if len(items) == 3:
        id, count, text, name = items + [None]
      else:
        id, count, text, name = items
      last = id, count, text, name


    xid = "{}-{}".format(prefix, id)
    count = int(count)

    for i in range(0,count):
      if name:
        print "*** imprimindo cracha com nome", name
        Badge(xid, name, text, small)
      else:
        print "*** imprimindo copia", i
        Badge(xid, text, small, '')

