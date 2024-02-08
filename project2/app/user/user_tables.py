#app/user/user_tables.py
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=False, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)   
    mobile = db.Column(db.String(255), unique=False, nullable=False)
    city = db.Column(db.Date, unique=False, nullable=True)
    designation = db.Column(db.String(255), unique=False, nullable=False)