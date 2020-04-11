# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:44:52 2020

@author: pawel
"""
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision = 2))
    
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')
    
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
    
    ### returns json version of the name and price tuple
    def json(self):
        return {'name': self.name, 'price': self.price}
    
    ### this is a class method to find item by name
    @classmethod
    def find_by_name(cls, name):
        ### SELECT * FROM items WHERE name = name LIMIT 1 i.e. returns first row
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