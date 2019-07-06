
from flask import Flask
from flask_restplus import Api

from manage import init_db, init_testdb, drop_all
from app.config import Config

api = Api()

def create_app(config_class=Config):
    app = Flask(__name__)
    init_db()
    init_testdb()
    drop_all()
    api.init_app(app)

    return app