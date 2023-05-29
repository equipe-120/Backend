from flask import Flask
from .db import db
from .models import User
from .routes import bp



app = Flask(__name__)
