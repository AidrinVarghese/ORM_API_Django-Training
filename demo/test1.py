from flask import Flask
import test2.test2
app = Flask("myproject")
print("Test1 name: " , __name__)
if __name__ == '__main__':
    app.run()