activate_this = '/var/www/demo/.venv/bin/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))

import os
os.environ['DATABASE_URI'] = 'mysql://demo:demo@127.0.0.1/demo'

import sys
sys.path.insert(0, '/var/www/demo')

from demo import app as application
