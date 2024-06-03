from flask import Flask, request, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import sqlalchemy
from flask_bcrypt import Bcrypt
import os

# stripe secret key #
# import stripe
# stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')


from models import db, User, Carts, Items

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

bcrypt = Bcrypt(app)

migrate = Migrate(app, db)

db.init_app(app)

URL_PREFIX = '/api'