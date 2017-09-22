from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    genres = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    #director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class MovieTheather(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class NowPlaying(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_theather = models.ForeignKey(MovieTheather, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.name+ ";"+ self.movie_theather.name
