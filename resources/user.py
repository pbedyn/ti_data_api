# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 20:28:40 2020

@author: pawel
"""
### userid and passwords are stored in an sqlite3 database
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required = True,
        help = "Username field cannot be blank."
        )
    
    parser.add_argument('password',
        type = str,
        required = True,
        help = "Password field cannot be blank."
        )
    
    ### create new user
    def post(self):
        data = UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists."}, 400
        
        user = UserModel(**data)
        user.save_to_db()
        
        return {"message": "User created successfully."}, 201