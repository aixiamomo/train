#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    return app
