from flask import Flask

app = Flask("myproject")
print("Test2 name: " , __name__)
app.run()