from flask import Flask, request 
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from sqlalchemy.exc import IntegrityError
from sqlalchemy import exc

# initiate flask instance

app = Flask(__name__)
app.secret_key = 'Bxxcx_please'

#db connection string - DB Engine :// user:password@localhost/DB_name

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:experion%40123@localhost/pythonpractice"

#creating connection object to database

db = SQLAlchemy(app)

# creating table for string

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    msg = db.Column(db.String(255), unique=False, nullable=False)
    date = db.Column(db.Date, unique=False, nullable=True)
    print('table created')
      
    
    
# @app.route('/contacts', methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         try:
            # data = request.json
            # name = data.get('name')
            # email = data.get('email')
            # phone_number = data.get('phone_number')
            # msg = data.get('msg')
#             print("Data Received:", data) 
#             obj = Contacts(name=name, email=email, phone_number=phone_number, msg=msg, date=date.today())
#             db.session.add(obj)
#             print("Session:", db.session)
#             db.session.commit()        
#             last_id = obj.id
#             msg = Contacts.query.get(last_id)
#             result = {"id": msg.id, "name": msg.name, "phone_number": msg.phone_number, "msg": msg.msg, "date": msg.date}
#             return result,201
#         # from sqlalchemy.exc import IntegrityError
#         except IntegrityError as e:
#             print(e)
#             return{"error": "Mobile number already exists"}, 400
#         except Exception as e:
#             print(e)
#             return {"error": "Something went wrong!"}, 500
#     else:
#         messages = Contacts.query.filter_by().all() #select * from contacts, cursor.excenutes(sql)
#         result = []
#         for msg in messages:
#             result.append({"id": msg.id, "name": msg.name, "phone_number": msg.phone_number, "msg": msg.msg, "date": msg.date})
#         return {"data": result},201
# Run the application





#View by Id, Edit or  object using ID
@app.route('/contact/<int:pk>', methods=['GET', 'PUT', 'DELETE'])
def contact_bu_ind(pk):
    #Get object details by ID
    if request.method == 'GET':
        try:
            msg = Contacts.query.get(pk)
            if msg:
                result = {"id": msg.id, "name": msg.name, "phone_number": msg.phone_number, "msg": msg.msg, "date": msg.date}
                return result, 200
            return {"message": " Not found"}, 500
        except Exception as e:
            print(e)
            return {"error": "Something went wrong!"}, 500
    elif request.method == 'PUT':
        try:
            print('console.log')
            data = request.json
            name = data.get('name')
            email = data.get('email')
            mobile = data.get('phone_number')
            message = data.get('msg')
            
            msg = Contacts.query.get(pk)
            if msg:
                if name:
                    msg.name = name
                if email:
                    msg.email = email
                
                db.session.commit()
                
                result={"id":msg.id, "name":msg.name, "email":msg.email, "phone_number":msg.phone_number, "msg":msg.msg}
                return result, 200
            return{"message": "no object with that id"}
        except exc.IntegrityError as e:
            return {"error":"Something went wrong"},400
        except Exception as e:
            print(e)
            return {"error": "Something went wrong!"}, 500  
    elif request.method == 'DELETE':
        try:
            msg = Contacts.query.get(pk)
            if msg:
                db.session.delete(msg)
                db.session.commit()
                result={"id":msg.id, "name":msg.name, "email":msg.email, "phone_number":msg.phone_number, "msg":msg.msg}
                return result, 200
            return{"message": "no object with that id"}
        except Exception as e:
            print(e)
            return {"error": "Something went wrong!"}, 500      
    else:
        messages = Contacts.query.filter_by().all() #select * from contacts, cursor.excenutes(sql)
        result = []
        for msg in messages:
            result.append({"id": msg.id, "name": msg.name, "phone_number": msg.phone_number, "msg": msg.msg, "date": msg.date})
        return {"data": result},201
    
        

with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True)
    