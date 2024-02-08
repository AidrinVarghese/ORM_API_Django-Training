# app/user/__init__.py
from flask import Blueprint
from flask_restful import Api
from app.user.user_logic import GetUsers
from app.user.user_logic import UserLogic

user_bp=Blueprint( 'user_bp', __name__)
api = Api(user_bp)

api.add_resource(GetUsers,'/user')
api.add_resource(UserLogic,'/userLogin')

