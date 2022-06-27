from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey, personality_quiz

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)
survey = satisfaction_survey

responses = []

@app.route("/")
def home_page():
    """ Returns the home page to the user"""
    return render_template("home.html", survey=survey)

@app.route("/question/<int:num_question>")
def question_page(num_question):
    """Returns the question page back to the user"""

    # some logic to not let the website bug out

    if responses is None:
        return redirect("/")
    
    if  num_question != len(responses):
        flash("You must complete the questions in order. Don't tinker with the URL")
        return redirect(f"/question/{len(responses)}") 

    if len(responses) == len(survey.questions):
        return redirect("/completed")

    else:
        curr_question = survey.questions[num_question]
        return render_template("question.html", num_question=num_question, survey=survey)

@app.route("/answer", methods=["POST"])
def answer():
    """processes users choice and appends it to the responses list"""

    choice = request.form['answer']

    responses.append(choice)

    if len(responses) == len(survey.questions):
        return redirect("/completed")

    return redirect(f"/question/{len(responses)}")

@app.route("/completed")
def completed():
    """Returns thank you page to the user"""
    return render_template("completed.html")
