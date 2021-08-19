from flask import render_template
from app import app
from .request import get_movies

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''

    #Getting popular movie
    title = 'Home - Welcome to the best Movie Review Website Online'
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing = get_movies('now_playing')
    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_playing = now_showing)

@app.route('/movie/<movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns the movie details page and its data.
    '''
    title = f'You are watching {movie_id}'
    return render_template('movie.html',title = title)