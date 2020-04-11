# -*- coding: utf-8 -*-

from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    
    ### look in the database and return the store if it's there else error message
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404
    
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A store with name '{}' already exists.".format(name)}, 404
        
        store = StoreModel(name)
        try:
            store.save_to_db()
            return {'message': "Store '{}' was created successfully.".format(name)}
        except:
            return {'message': "An error occured while creating the store."}, 500
    
    def delete(self, name):
        store  = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message': "Store deleted"}
    

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}