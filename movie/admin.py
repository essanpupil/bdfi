from django.contrib import admin

from movie.models import Movie, Actor, Genre, Category, Trivia, Review

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Trivia)
admin.site.register(Review)

