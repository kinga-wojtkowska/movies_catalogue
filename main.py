from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = []
    for movie in range(0,8):
        string = 'film' + str(int(movie)+1)
        movies.append(string)
    return render_template("homepage.html", movies=movies)