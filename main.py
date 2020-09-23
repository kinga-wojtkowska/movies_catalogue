from flask import Flask, render_template, url_for, request
import tmdb_client

app = Flask(__name__)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}    

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', "popular")
    list_types = ['top_rated', 'upcoming', 'popular', 'now_playing'] 
    if selected_list not in list_types:
        movies = tmdb_client.get_random_eight(list_type='popular')
        return render_template("homepage.html", movies=movies, current_list='popular', list_types=list_types)
    else:        
        movies = tmdb_client.get_random_eight(list_type=selected_list)
        return render_template("homepage.html", movies=movies, current_list=selected_list, list_types=list_types)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_cast(movie_id, how_many = 4)
    backdrop = tmdb_client.get_random_backdrop_image(movie_id)
    return render_template("movie_details.html", movie=details, cast=cast, backdrop=backdrop)

@app.route("/movie/<movie_id>/full_cast")
def movie_full_cast(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    return render_template("full_cast.html", movie=details, cast=cast)        