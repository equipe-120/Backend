from flask import Flask
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
from flask_mysqldb import MySQL

app = Flask(__name__)