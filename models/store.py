# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:44:52 2020

@author: pawel
"""
from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    
    ### create a relationship between the store and items in the store
    items = db.relationship('ItemModel', lazy = 'dynamic')
    
    def __init__(self, name):
        self.name = name
    
    ### returns json version of the name and price tuple
    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}
    
    ### this is a class method to find item by name
    @classmethod
    def find_by_name(cls, name):
        ### SELECT * FROM stores WHERE name = name LIMIT 1 i.e. returns first row
        return cls.query.filter_by(name = name).first()
    
    ### this is a class method to upsert an item
    def save_to_db(self):
        ### save the model to the database
        db.session.add(self)
        db.session.commit()
    
    ### delete item from the database
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()