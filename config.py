# -*- coding: UTF-8 -*-
import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = '&*@^!#&@!^$&'

    @staticmethod
    def init_app(app):
        pass

