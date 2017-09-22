from django.test import TestCase
from movieit.movies.models import *

# Create your tests here.
class MovieModelTest(TestCase):

    def setUp(self):
        self.movie_name = "It - A coisa"
        self.movie = Movie(name=self.movie_name, rating=9, description="Teste", genres="Terror")

    def test_model_can_create_a_movie(self):
        old_count = Movie.objects.count()
        self.movie.save()
        new_count = Movie.objects.count()
        self.assertNotEqual(old_count, new_count)

class MovieTheatherModelTest(TestCase):
    def setUp(self):
        self.movie_theather_name = "Cinemark"
        self.movie_theather = MovieTheather(name=self.movie_theather_name, location="Av. Bernardo Vieira")

    def test_model_can_create_a_movie(self):
        old_count = MovieTheather.objects.count()
        self.movie_theather.save()
        new_count = MovieTheather.objects.count()
        self.assertNotEqual(old_count, new_count)

class NowPlayingModelTest(TestCase):
    def setUp(self):
        self.movie_theather = MovieTheather(name="Cinemark", location="Av. Bernardo Vieira")
        self.movie_theather.save()
        self.movie = Movie(name="Up- Altas", rating=9, description="Teste", genres="Terror")
        self.movie.save()
        self.nowplaying = NowPlaying(movie=self.movie, movie_theather=self.movie_theather)
    
    def test_model_can_create_now_playing(self):
        old_count = NowPlaying.objects.count()
        self.nowplaying.save()
        new_count = NowPlaying.objects.count()
        print(self.nowplaying)
        self.assertNotEqual(old_count, new_count)
