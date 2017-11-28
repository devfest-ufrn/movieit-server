from .models import *
# from urllib3 import request as rqst
from django.conf import settings
import requests
from django.conf import settings

def get_ratings(request):

    for movie in Movie.objects.all():
        try:
            movie.imdb_id is not None
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

