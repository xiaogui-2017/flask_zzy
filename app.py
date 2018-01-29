#  -*- coding:utf-8 -*-
# from flask.ext.mongoengine import MongoEngine
from flask_mongoengine import MongoEngine
from flask import Flask

app = Flask(__name__)

# test 是链接的数据库
app.config['MONGODB_SETTINGS'] = {'db': 'test'}

# 实例化
db = MongoEngine(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
