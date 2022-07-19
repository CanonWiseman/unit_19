from boggle import Boggle
from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = "1235"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/create-board')
def create_board():

    board = boggle_game.make_board()
    session["board"] = board

    return redirect('/play-game')

@app.route('/play-game', methods=['GET', 'POST'])
def play_game():
    
    board = session.get('board')

    return render_template('play-game.html', board=board)

@app.route('/check-word', methods=['GET'])
def check_word():
    board = session.get("board")
    
    word = request.args["word"]
    


    return jsonify(boggle_game.check_valid_word(board, word))