from django.test import TestCase
from .models import *


# Create your tests here.

class PartnersDataModelTest(TestCase):
    def setUp(self):
        self.partners_data = PartnersData(
            site_URL="https://www.ingresso.com/natal/movieit/filmes/thor-ragnarok?utm_source=api&utm_medium=link-filme&utm_campaign=movieit&utm_content=thor-ragnarok"
            , ticket_id=19730)

    def test_amount_model_partners_data(self):
        old_count = PartnersData.objects.count()
        self.partners_data.save()
        new_count = PartnersData.objects.count()
        self.assertEqual(old_count + 1, new_count)


class MovieModelTest(TestCase):
    def setUp(self):
        self.movie_name = "It - A coisa"
        self.movie = Movie(name=self.movie_name, description="Teste", genres="Terror")

    def test_amount_model_can_create_a_movie(self):
        old_count = Movie.objects.count()
        self.movie.save()
        new_count = Movie.objects.count()
        self.assertEqual(old_count + 1, new_count)


class MovieTheatherModelTest(TestCase):
    def setUp(self):
        self.movie_theather_name = "Cinemark"
        self.movie_theather = MovieTheather(name=self.movie_theather_name, location="Av. Bernardo Vieira")

    def test_amount_model_can_create_a_movie(self):
        old_count = MovieTheather.objects.count()
        self.movie_theather.save()
        new_count = MovieTheather.objects.count()
        self.assertEqual(old_count + 1, new_count)


class NowPlayingModelTest(TestCase):
    def setUp(self):
        self.movie_theather = MovieTheather(name="Cinemark", location="Av. Bernardo Vieira")
        self.movie_theather.save()
        self.movie = Movie(name="Up- Altas", description="Teste", genres="Terror")
        self.movie.save()
        self.nowplaying = NowPlaying(movie=self.movie, movie_theather=self.movie_theather)

    def test_amount_model_can_create_now_playing(self):
        old_count = NowPlaying.objects.count()
        self.nowplaying.save()
        new_count = NowPlaying.objects.count()
        self.assertEqual(old_count + 1, new_count)
