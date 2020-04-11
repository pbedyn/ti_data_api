# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:36:59 2020

@author: pawel
"""

from db import db

class UserModel(db.Model):
    ### tell sqlalchemy which table to use
    __tablename__ = 'users'
    ### tell sqlalchemy which columns to use
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()