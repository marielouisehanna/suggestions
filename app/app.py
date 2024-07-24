from flask import Flask, render_template, redirect, url_for # type: ignore
import random
from books import books
from games import games
from movies import movies
from shows import shows
from songs import songs

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/suggest_song')
def suggest_song():
    suggestion = random.choice(songs)
    return render_template('songs.html', suggestion=suggestion)

@app.route('/suggest_show')
def suggest_show():
    suggestion = random.choice(shows)
    return render_template('shows.html', suggestion=suggestion)

@app.route('/suggest_movie')
def suggest_movie():
    suggestion = random.choice(movies)
    return render_template('movies.html', suggestion=suggestion)

@app.route('/suggest_book')
def suggest_book():
    suggestion = random.choice(books)
    return render_template('books.html', suggestion=suggestion)

@app.route('/suggest_game')
def suggest_game():
    suggestion = random.choice(games)
    return render_template('games.html', suggestion=suggestion)

if __name__ == '__main__':
    app.run(debug=True)