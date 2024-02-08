# app/user/user_logic.py
from flask import request
from flask_restful import Resource
from app.user.user_tables import User
from app import db
# from app import db

class GetUsers(Resource):
    def get(self):
        user = User.query.all()
        if user:
            return {'username': user.username, 'email': user.email}, 200
        else:
            return {'message': 'No user found'}, 404
        
    def post(self):
        try:
            data = request.get_json()
            new_user= User(
                username=data.get('username'),
                password=data.get('password'),
                email=data.get('email'),                
                mobile=data.get('mobile'),
                city=data.get('city'),
                designation=data.get('designation')
            )
            db.session.add(new_user)
            db.session.commit()
            return {'message': 'User added successfully'},201
        except Exception as e:
            print(e)
            return {'error': 'User registration failed!'}, 500
        
#logic for user login
class UserLogin(Resource):
    
    def post(self):
        try:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
            user = User.query.filter_by(username=username).first()
            if user:
                if user.password == password:
                    return {'message': 'User login successful!'}, 200
                else:
                    return {'message': 'User login failed!'}, 404
        except Exception as e:
            print(e)
            return {'error': 'User login failed!'}, 500
    