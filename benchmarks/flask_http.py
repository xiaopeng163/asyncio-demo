from flask import Flask
app = Flask(__name__)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/<payload_size>')
def hello_world(payload_size):

    return 'X' * int(payload_size)

