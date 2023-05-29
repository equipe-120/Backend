from flask import Flask # Importe as configurações do arquivo config.py
from flask import Flask
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
from flask_mysqldb import MySQL
from flask import render_template 

app = Flask(__name__)

app.config['MYSQL_HOST'] = MYSQL_HOST
app.config['MYSQL_USER'] = MYSQL_USER
app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD
app.config['MYSQL_DB'] = MYSQL_DB

mysql = MySQL(app)

# Atribua as configurações ao aplicativo Flask

@app.route('/')
def index():
    return 'Hello, World!'

#def serve_pagina_react():
    #return render_template('../*frontend')

if __name__ == '__main__':
    app.run()
