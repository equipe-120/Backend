from flask import Flask
from flask_mysqldb import MySQL
from flask import render_template 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

#def serve_pagina_react():
    #return render_template('../*frontend')

if __name__ == '__main__':
    app.run()
