from flask import Flask, request

app = Flask(__name__)

@app.route("/welcome")

def welcome():
    return "<h1>Welcome</h1>"

@app.route("/")
def root():
    return "<h1>root Page</h1>"

@app.route("/welcome/home")
def welcome_home():
    return "<h1>Welcome Home</h1>"

@app.route("/welcome/back")
def welcome_back():
    return "<h1>Welcome Back</h1>"

