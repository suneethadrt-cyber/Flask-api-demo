from flask import Flask, jsonify
import random

app = Flask(__name__)

movies = [
    'The Shawshank Redemption',
    'The Godfather',
    'The Dark Knight',
    'Pulp Fiction',
    'The Lord of the Rings: The Return of the King',
]

@app.route('/')
def home():
    return 'Welcome to the Movie Suggestion API! Use the /movie endpoint to get a random movie suggestion.'

@app.route('/movie')
def get_random_movie():
    random_movie = random.choice(movies)
    return jsonify({'movie': random_movie})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
