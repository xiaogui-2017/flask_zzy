#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo

# 返回一个 collection,
from app import db


class User(db.Document):
    name = db.StringField()
    email = db.StringField()

    """
        def get_coll():
            client = pymongo.MongoClient('127.0.0.1', 27017)
            db = client.test
            user = db.user_collection
            return user

        def __init__(self, name, email):
            self.name = name
            self.email = email

        def save(self):
            user = {"name": self.name, "email": self.email}
            coll = get_coll()
            id = coll.insert(user)
            print id
        def __str__(self):
            return "name:{} - email:{}".format(self.name, self.email)

        @staticmethod
        def query_users():
            users = get_coll().find()
            return users
    """
