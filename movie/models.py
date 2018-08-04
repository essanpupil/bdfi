from django.db import models
from embed_video.fields import EmbedVideoField


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    video = EmbedVideoField(null=True)

    def __str__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=255)
    birth_of_date = models.DateField()
    movie = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name
