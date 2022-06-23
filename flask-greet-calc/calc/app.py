# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }


app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h1>Welcome to Calc</h1>"

@app.route("/math/<operation>/")
def math(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return f"The result is {operators[operation](a,b)}"


