from django.contrib import admin

from movie.models import Movie, Actor

admin.site.register(Movie)
admin.site.register(Actor)
