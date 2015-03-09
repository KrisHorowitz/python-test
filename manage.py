#!/usr/bin/env python
# coding=utf-8

from flask.ext.script import Manager, Command, Server
from application import app


class Hello(Command):
    """ prints hello world """

    def run(self):
        print "hello world"


manager = Manager(app)
manager.add_command('hello', Hello())
manager.add_command('runserver', Server(host='0.0.0.0', port='8000'))


if __name__ == "__main__":
    manager.run()