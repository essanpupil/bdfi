from django.db import models
from embed_video.fields import EmbedVideoField


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    video = EmbedVideoField(null=True)

    def __str__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=255)
    birth_of_date = models.DateField()
    movie = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name
