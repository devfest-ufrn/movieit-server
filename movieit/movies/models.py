from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class MovieTheather(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    now_playing = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name