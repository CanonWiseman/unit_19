from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey, personality_quiz

app = Flask(__name__)
app.config['SECRET_KEY'] = "1234"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
survey = satisfaction_survey
RESPONSES_KEY = "responses"

@app.route("/")
def home_page():
    """ Returns the home page to the user"""
    return render_template("home.html", survey=survey)

@app.route("/start_survey", methods=["POST"])
def start_survey():
    session[RESPONSES_KEY] = []
    return redirect("/question/0")

@app.route("/question/<int:num_question>")
def question_page(num_question):
    """Returns the question page back to the user"""

    # some logic to not let the website bug out

    responses = session.get(RESPONSES_KEY)

    if session[RESPONSES_KEY] is None:
        return redirect("/")
    
    if  num_question != len(session.get(RESPONSES_KEY)):
        flash("You must complete the questions in order. Don't tinker with the URL")
        return redirect(f"/question/{len(session[RESPONSES_KEY])}") 

    if len(session[RESPONSES_KEY]) == len(survey.questions):
        return redirect("/completed")

    else:
        curr_question = survey.questions[num_question]
        return render_template("question.html", num_question=num_question, survey=survey)

@app.route("/answer", methods=["POST"])
def answer():
    """processes users choice and appends it to the responses list"""

    choice = request.form['answer']
    responses = session[RESPONSES_KEY]
    session[RESPONSES_KEY] = responses

    responses.append(choice)

    if len(responses) == len(survey.questions):
        return redirect("/completed")

    return redirect(f"/question/{len(responses)}")

@app.route("/completed")
def completed():
    """Returns thank you page to the user"""
    return render_template("completed.html")
