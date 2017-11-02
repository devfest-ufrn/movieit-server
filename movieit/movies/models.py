from django.db import models


# Create your models here.

class PartnersData(models.Model):
    site_URL = models.TextField()
    ticket_id = models.IntegerField()

    def __str__(self):
        return self.site_URL

class Rating(models.Model):
    choice_of_avaliation = (
        ('%', 'Percentage'),
        ('10', 'Base_10')
    )

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=11, choices=choice_of_avaliation)
    value = models.FloatField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    genres = models.CharField(max_length=100)
    description = models.TextField()
    content_rating = models.CharField(max_length=10, blank=True)

    urlKey = models.SlugField(max_length=100)

    ratings = models.ManyToManyField(Rating)
    partners_data = models.ForeignKey(PartnersData, on_delete=models.CASCADE, blank=True, null=True)

    # director = models.ForeignKey(Director, on_delete=models.CASCADE)

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
        return self.movie.name + " ; " + self.movie_theather.name
