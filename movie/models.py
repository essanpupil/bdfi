from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()

    def __str__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=255)
    birth_of_date = models.DateField()
    movie = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name
