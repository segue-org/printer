from lib.label import Label

class Badge:
  def __init__(self, xid, name, company, city, copies=1):
    self.label = Label()

    self.barcode(xid)
    self.xid(xid)
    self.name(name)
    self.line()
    self.company(company)
    self.city(city)

    self.label.close(copies)

  def barcode(self, xid):
    prefix, number = xid.split('-')
    self.label.code(int(number), 280, 200, source=prefix, ori=3, size=4, height=30)

  def xid(self, xid):
    prefix, number = xid.split('-')
    prefix = prefix[0].upper()
    output = "-".join([prefix,number])
    self.label.text(output, 190, 205, size=1)

  def line(self):
    self.label.text("____________", 10, 105)

  def name(self, name):
    self.label.wrapped_and_adjusted_text(name, 10, 80, max_size=5)

  def company(self, company):
    self.label.wrapped_and_adjusted_text(company, 10, 140, max_size=2)

  def city(self, city):
    self.label.wrapped_and_adjusted_text(city, 10, 200, max_size=1, width=0.6)

