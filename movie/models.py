from django.contrib.auth.models import User
from django.db import models
from embed_video.fields import EmbedVideoField


class Location(models.Model):
    city = models.CharField(max_length=64)
    province = models.CharField(max_length=64)

    def __str__(self):
        return self.city


class Genre(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class ProductionHouse(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(models.Model):
    FILM = 'film'
    TV_SERIES = 'tv'
    FTV = 'ftv'
    CATEGORY_CHOICES = (
        (FILM, 'Film'),
        (TV_SERIES, 'TV'),
        (FTV, 'FTV')
    )
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    production_house = models.ForeignKey(ProductionHouse, on_delete=models.CASCADE)
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES, default=FILM)
    genre = models.ManyToManyField(Genre)
    video = EmbedVideoField(null=True)
    synopsis = models.TextField(null=True)

    def __str__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=128)
    fullname = models.CharField(max_length=255)
    birth_of_date = models.DateField()
    place_of_birth = models.ForeignKey(Location, on_delete=models.CASCADE)
    role = models.ManyToManyField(Role)
    biography = models.TextField()

    def __str__(self):
        return self.name


class Cast(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    play_as = models.CharField(max_length=128)

    def __str__(self):
        return self.play_as


class Credit(models.Model):
    name = models.CharField(max_length=128)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Trivia(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    info = models.CharField(max_length=255)
    link = models.URLField()
    source = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.info


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.rating
