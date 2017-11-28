from django.shortcuts import render
from .models import *
# from urllib3 import request as rqst
from django.conf import settings
import requests
from django.conf import settings

def get_ratings(request):

    for movie in Movie.objects.all():
        try:
            if movie.imdb_id:
                r = requests.get('http://www.omdbapi.com/?apikey='+settings.OMDB_KEY+'&i='+movie.imdb_id)
                json = r.json()

                print(movie.imdb_id)

                movie.imdb_rating = json['imdbRating']
                movie.rotten_rating = 'N/A' if len(json['Ratings'])<2 else json['Ratings'][1]['Value']
                movie.metascore = json['Metascore']

                movie.save()
        except:
            movie.imdb_rating = 'N/A'
            movie.rotten_rating = 'N/A'
            movie.metascore = 'N/A'
            print("do something")

    return render(request)

def init_movies(request):
    r = requests.get('https://api-content.ingresso.com/v0/events/city/48/partnership/movieIT')
    movies_json = r.json()

    for m_j in movies_json['items']:
        movie = Movie()

        movie.title = m_j['title']
        movie.ingresso_id = m_j['id']
        movie.poster_portrait = m_j['images'][0]['url']
        movie.poster_horizontal = m_j['images'][1]['url']
        movie.synopsis = m_j['synopsis']
        movie.cast = m_j['cast']
        movie.director = m_j['director']
        movie.duration = m_j['duration']
        movie.content_rating = m_j['contentRating']
        movie.save()

    return render(request)