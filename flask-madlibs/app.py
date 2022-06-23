from flask import Flask, request, render_template, redirect
from stories import story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def home():

    prompts = story.prompts

    return render_template("home.html", prompts=prompts)

@app.route("/story")
def response():

    response = story.generate(request.args)

    return render_template("response.html", response=response)
    