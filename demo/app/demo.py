from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, socket
from datetime import datetime
app = Flask(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
db = SQLAlchemy(app)
hostname = socket.gethostname()

@app.route('/')
def index():
  return 'Hello, World!\n'

@app.route('/db')
def dbtest():
  try:
      db.create_all()
  except Exception as e:
      return e.message + '\n'
  return 'Database Connected Successfully!\n'
@app.route('/jtaher') 
def username_with_time():
    current_time = datetime.now().isoformat()
    return f'jather {current_time}\n'


if __name__ == '__main__':
  app.run()
