import sys
import traceback

from lib.badge import Badge
from lib.envelope import Envelope

from flask import Flask, jsonify, request, abort
app = Flask(__name__)

@app.route('/badge', methods=['POST'])
def badge():
  return print_with(Badge)

@app.route('/envelope', methods=['POST'])
def envelope():
  return print_with(Envelope)

@app.route('/both', methods=['POST'])
def both():
  return print_with(Badge, Envelope)

def print_with(*klasses):
  try:
    xid     = request.form['xid']
    name    = request.form['name']
    company = request.form.get('company')
    city    = request.form.get('city')

    messages = [];

    for klass in klasses:
      klass(xid, name, company, city)
      object_type = klass.__name__.split('.')[-1]
      messages.append("{} has been printed".format(object_type));

    return jsonify({ 'messages' : messages })

  except Exception, e:
    response = jsonify({ 'error': e.args, 'stack': traceback.format_exc() })
    response.status_code = 500
    return response

@app.route('/')
def index():
  return jsonify({
    'links': [
      { 'rel': 'badge',    'href': '/badge/',    'method': 'POST' },
      { 'rel': 'envelope', 'href': '/envelope/', 'method': 'POST' },
      { 'rel': 'simple',   'href': '/simple/',   'method': 'POST' }
    ]
  })

if __name__ == '__main__':
  if len(sys.argv) < 1:
    print "USAGE: python server.py <PORT> <ENV>"
  else:
    app.run(host  = "0.0.0.0",
            port  = int(sys.argv[1]),
            debug = sys.argv[2] == 'debug')

