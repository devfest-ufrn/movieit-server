from django.db import models


class Rating(models.Model):
    choice_of_avaliation = (
        ('%', 'Percentage'),
        ('10', 'Base_10')
    )

    name = models.CharField(max_length=100)
    #type = models.CharField(max_length=11, choices=choice_of_avaliation)
    value = models.FloatField()

    def __str__(self):
        return self.name


class MovieGenre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Movie(models.Model):
    ingresso_id = models.IntegerField()
    title = models.CharField(max_length=100)
    imdb_id = models.CharField(max_length=30, default="")
    posterPortrait = models.CharField(max_length=200, default="")
    posterHorizontal = models.CharField(max_length=200, default="")
    synopsis = models.CharField(max_length=400, default="")
    cast = models.CharField(max_length=200, default="")
    director = models.CharField(max_length=40, default="")
    duration = models.IntegerField(default=0)
    genres = models.ManyToManyField(MovieGenre)
    content_rating = models.CharField(max_length=10, blank=True)
    ratings = models.ManyToManyField(Rating)

    def __str__(self):
        return self.title

class MovieTheather(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
