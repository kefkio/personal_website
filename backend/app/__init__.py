from Flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config Development') # or 'config Production'   
CORS(app)                                       # enable CORS on all routes
app.config['CORS_HEADERS'] = 'Content-Type'     # set CORS headers
db = SQLAlchemy(app)                               # initialize SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    # silence the deprecation warning
from app import routes, models