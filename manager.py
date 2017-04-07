#!/usr/bin/python
# -*- coding: UTF-8 -*-
from app import create_app
from flask_script import Manager, Server, Shell

app = create_app()
manage = Manager(app)


def make_shell_context():
    return dict(app=app)

manage.add_command('shell', Shell(make_context=make_shell_context))
manage.add_command('runserver', Server('127.0.0.1', port=5000))

if __name__ == '__main__':
    manage.run()