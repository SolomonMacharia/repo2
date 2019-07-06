
from flask import Flask
from manage import init_db, init_testdb, drop_all

def create_app():
    app = Flask(__name__)
    init_db()
    init_testdb()
    drop_all()

    return app