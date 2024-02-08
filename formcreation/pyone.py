from flask import Flask, render_template, request, redirect, flash, jsonify
import pymysql.cursors

app = Flask(__name__)
app.secret_key="secret"

@app.route("/")
def home():
    return render_template("home.html", name="home", message="Home")

@app.route("/contact", methods=["GET", "POST"])
def contact_us():
    if request.method == "POST":
        try:
            name = request.form.get("name")
            email = request.form.get("email")
            mobile = request.form.get("mobile")
            city = request.form.get("city")
            message = request.form.get("message")
            int(mobile)
            if len((mobile))!=10:
                flash("Mobile number not having 10 digits", "warning")
                return render_template("formindex.html")
            print("Form data:", name, email, mobile, city, message)            
            return redirect("/")
        except Exception as e:
            print("Error:", e)  
            flash("Mobile number not having 10 digits", "danger")
            return render_template('formindex.html', message="Something went wrong!", error_data=str(e)) 
    return render_template("formindex.html")






@app.route("/contact-api", methods=['POST', 'GET'])
def contact_api():
    # data=request.form
    data=request.json
    print("Data:", data)    
    name = data.get('name')
    email = data.get('email')
    mobile = data.get('mobile')
    city = data.get('city')
    message = data.get('message')
    if not len(mobile) == 10 or not mobile.isdigit():
        return{"message": "Mobile number should be at least 10 digits"},400
    # implement a logic to insert data to database
    # DB and Table
    # connect ot db
    # query to execute 
    
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='experion@123',
                             database='pythonpractice',
                             cursorclass=pymysql.cursors.DictCursor)
    if request.method == 'POST':
        results = []
        with connection:
            with connection.cursor() as cursor:
            # Create a new record
                # sql = f"INSERT INTO `contact_details` (`customer_name`, `customer_email`, `customer_mobile`, `customer_city`, `customer_message`) VALUES ('{name}', '{email}','{mobile}', '{city}', '{message}')"
                # cursor.execute(sql)
                            
            # Read a single record
            
                sql = f"SELECT * FROM contact_details"
                cursor.execute(sql)
                results = cursor.fetchall()
            for result in results:
                print(result)
                print("\n")
                # connection.commit()
        return {"data": results},200
    
    
    
    
    
    
    
    
    
@app.route("/contact-api/<int:id>", methods=['GET', 'PUT'])
def contact_api_update(id):
    # data=request.form
    if request.method == 'PUT':
        data=request.json       
        name = data.get('name')
        email = data.get('email')
        mobile = data.get('mobile')
        city = data.get('city')
        message = data.get('message')
        
        connection = pymysql.connect(host='localhost',
                                user='root',
                                password='experion@123',
                                database='pythonpractice',
                                cursorclass=pymysql.cursors.DictCursor)
        with connection:
                with connection.cursor() as cursor:                
                    sql = f"UPDATE contact_details SET customer_name ='{name}', customer_email='{email}'WHERE customer_id ='{id}'"
                    print("SQL:", sql)
                    cursor.execute(sql)                   
                    connection.commit()
                    sql_fetch = f"SELECT * FROM contact_details WHERE customer_id = '{id}'"
                    cursor.execute(sql_fetch)
                    results = cursor.fetchone()
                    return {"Data": results},200
                    

@app.route("/contact-api/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def contact_api_delete(id):
    # data=request.form
    if request.method == 'DELETE':
        try:
            data=request.json       
            name = data.get('name')
            email = data.get('email')
            mobile = data.get('mobile')
            city = data.get('city')
            message = data.get('message')
            
            connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='experion@123',
                                    database='pythonpractice',
                                    cursorclass=pymysql.cursors.DictCursor)
            with connection:
                with connection.cursor() as cursor:                
                    sql_delete = f"DELETE FROM contact_details WHERE customer_id ='{id}'"
                    print("SQL:", sql_delete)
                    cursor.execute(sql_delete)                  
                    connection.commit()
                    return {"Data": "Deleted"},200
        except Exception as e:
            return("Error:", e)
app.run()
