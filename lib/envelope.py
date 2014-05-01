import textwrap

from lib.label import Label

class Envelope:
  def __init__(self, xid, name, company, city):
    self.label = Label()

    self.barcode(xid)
    self.xid(xid)
    self.name(name)
    self.company(company)

    self.label.close()

  def barcode(self, xid):
    prefix, number = xid.split('-')
    self.label.code(int(number), 280, 200, height=50, ori=3, size=15)

  def name(self, name):
    self.label.wrapped_and_adjusted_text(name, 10, 160, max_size=2, width=0.7)

  def company(self, company):
    self.label.wrapped_and_adjusted_text(company, 10, 200, max_size=1)

  def xid(self, xid):
    prefix, number = xid.split('-')
    prefix = prefix[0].upper()
    output = "-".join([prefix,number])
    self.label.text(output, 10, 100, size=8)
