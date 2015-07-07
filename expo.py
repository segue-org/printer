import sys
import codecs

from lib.badge import Badge

sys.stdout = codecs.open('/dev/stdout', 'w', 'utf8')

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print "USAGE: cat FILE | python expo.py <PREFIX> <SMALLTEXT>"
    sys.exit(1)

  prefix = sys.argv[1]
  small  = '' if len(sys.argv) == 2 else sys.argv[2]

  print 'AGUARDANDO ENTRADA...'
  while True:
    print "FORMATOS: id,count,text,name<enter>"
    print "          OU                       "
    print "          id,count,text<enter>     "

    line = sys.stdin.readline()
    if len(line.strip()) == 0:
      print '*** empty, quitting'
      break
    if line.startswith("#"):
      print "*** pulando " + line
      continue
    if line.strip() == "exit":
      print "*** exit"
      break

    line = line.decode('utf-8')
    print line
    if line.strip() == 'repeat':
      xid, count, text, name = last
    else:
      items = line.strip().split('\t')
      print items
      if len(items) == 3:
        xid, count, text, name = items + [None]
      else:
        xid, count, text, name = items
      last = xid, count, text, name


    count = int(count)

    for i in range(0,count):
      if name:
        print "*** imprimindo cracha com nome", name
        Badge(prefix, xid, name, text, small)
      else:
        print "*** imprimindo copia", i
        Badge(prefix, xid, text, small, '')

