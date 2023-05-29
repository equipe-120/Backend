from flask import Flask
from .db import db
from .models import User
from flask_mysqldb import MySQL



app = Flask(__name__)
