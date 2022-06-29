from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World updated!!"

@app.route("/user")
def set_user():
    return "Hello, User!"
