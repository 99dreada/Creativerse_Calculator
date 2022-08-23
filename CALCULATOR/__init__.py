from flask import Flask
#from flask.cli import AppGroup
#import click
#import os
#from CALCULATOR.model import db
#from CALCULATOR.login import login_init_app

app = Flask(__name__)
"""
def config_db(db_url='sqlite:///db/calculator.db'):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if app.config.get('PROFILE', False): # pragma: no cover
        from werkzeug.contrib.profiler import ProfilerMiddleware
        app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])
    app.secret_key = "#########"
    db.init_app(app)

def config_login():
    login_init_app(app)

config_db()
config_login()
from CALCULATOR import routes

#init the flask commands#

db_cli = AppGroup('db')

@db_cli.command('init')
def db_init():
    try: os.mkdir('calculator/db')
    except: pass
    from CALCULATOR.model import create_db
    create_db()

app.cli.add_command(db_cli)
"""