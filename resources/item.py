# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 23:33:07 2020

@author: pawel
"""

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

### Item Resource
### instance of class Resource with methods get and post supported by the API
class Item(Resource):
    ### parse the put request to make sure the price element is extracted
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type = float,
        required = True,
        help = "This field cannot be left blank!")
    
    parser.add_argument('store_id',
        type = int,
        required = True,
        help = "Every item needs a store id")
    
    ### we'll have to authenticate before using methods
    @jwt_required()
    ### get a specific item by the name
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404
      
    ### post new item with a specified name
    def post(self, name):
        ### Error first approach - check if item with that name already exists
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400 # bad request

        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred when inserting the item."}, 500 # internal server error
        return item.json(), 201
    
    ### delete an item with a specified name
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': "Item deleted"}
    
    ### change details of an item
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}