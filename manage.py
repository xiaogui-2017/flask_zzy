#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_script import Manager
from app import app
from models import User

# 实例化
manager = Manager(app)


# 修饰器
@manager.command
def hello():
    print 'hello world'


@manager.option('-m', '--msg', dest='msg_val', default='张志原')
def hello_world(msg_val):
    print 'hello ' + msg_val


@manager.command
def save():
    user = User('ming', '110@qq.com')
    user.save()


@manager.command
def query_users():
    users = User.query_users()
    for user in users:
        print user


if __name__ == "__main__":
    manager.run()
