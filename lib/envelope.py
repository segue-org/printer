import settings
import textwrap

from lib.label import Label

class Envelope:
  def __init__(self, prefix, xid, name, company, city, copies=1, device=settings.DEVICE):
    self.label = Label(device=device)

    self.barcode(prefix, xid)
    self.xid(prefix, xid)
    self.name(name)
    self.company(company)

    self.label.close(copies)

  def barcode(self, prefix, xid):
    self.label.code(int(xid), 280, 200, source=prefix, height=50, ori=3, size=15)

  def name(self, name):
    self.label.wrapped_and_adjusted_text(name, 10, 160, max_size=2, width=0.7)

  def company(self, company):
    self.label.wrapped_and_adjusted_text(company, 10, 200, max_size=1)

  def xid(self, prefix, xid):
    output = "{}-{}".format(prefix, xid)
    self.label.text(output, 10, 100, size=8)
