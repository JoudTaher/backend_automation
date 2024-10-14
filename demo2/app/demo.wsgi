app_name="demo2"

activate_this = f'/var/www/{app_name}/.venv/bin/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))

import sys
sys.path.insert(0, f'/var/www/{app_name}')

from demo import app as application
