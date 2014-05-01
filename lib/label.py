import sys
import textwrap
from lib.remove_accents import remove_accents

STX = chr(2);
CR  = chr(13);
LF  = chr(10);

DEFAULTS = {
  'ori':     4,
  'font':    9,
  'mh':      2,
  'mv':      2,
  'size':    5,
  'y':       0,
  'x':       0,
}


class Label:
  def __init__(self, device='/dev/usb/lp0'):
    self.device = open(device,'w');

    self.set_label_format()
    self.set_gap_detection()
    self.set_thermal_mode(0)
    self.set_resolution(11)
    self.set_temperature(9)
    self.set_print_speed('D')

  def send_raw(self, *parts, **opts):
    parts = [ str(p) for p in parts ]
    if opts.get('stx'): parts.insert(0,STX)

    data = "".join(parts)
    self.device.write(data+CR)
    self.device.flush()
    sys.stdout.write("[PRINTER] "+ repr(data+CR+LF) + CR+LF);
    sys.stdout.flush();

  def set_label_format(self):
    self.send_raw("L", stx=True)

  def set_gap_detection(self):
    self.send_raw("e", stx=True)

  def set_thermal_mode(self, value=0):
    self.send_raw("KI7", chr(0), stx=True)

  def set_resolution(self, value=11):
    self.send_raw("D", value)

  def set_temperature(self, value=9):
    self.send_raw("H", "%2d" % value)

  def set_print_speed(self, value='D'):
    self.send_raw("P", value)

  def close(self, copies = 1):
    self.send_raw("Q%04d" % (int(copies),) );
    self.send_raw("E");
    self.device.close();

  def code(self, id, y, x, size = 10, height = 15, ori = 4, codetype = 'C'):
    commands = [
      '%1d' % ori,
      '%1s' % codetype,
      '%02d' % size,
      '%03d' % height,
      '%04d' % y,
      '%04d' % x,
      '%06d' % id
    ]
    self.send_raw(*commands)


  def text(self, text, y, x, **args):
    text = remove_accents(text);
    parms = DEFAULTS.copy();
    parms.update(args);
    command = [
        "%1d"  % parms['ori'],
        "%1s"  % parms['font'],
        "%1d"  % parms['mh'],
        "%1d"  % parms['mv'],
        "%03d" % parms['size'],
        "%04d" % y,
        "%04d" % x,
        text[0:40]
    ]
    self.send_raw(*command)

  def wrapped_and_adjusted_text(self, text, y, x, max_size=5, width=1):
    limits = { 1: 30, 2: 21, 3: 19, 4: 17, 5: 15 }
    current = max_size;

    while current >= 1:
      limit = int(limits[current] * width)
      lines = textwrap.wrap(text, limit)
      if len(lines) <= 2:
        break
      current -= 1

    if len(lines) == 1:
      self.text(text, y, x, size=current)
    else:
      self.text(lines[0], y, x - 5 * current, size = current)
      self.text(lines[1], y, x + 5 * current, size = current)
