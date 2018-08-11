from django.contrib import admin

from movie.models import Movie, Actor, Genre, Trivia, Review, Role, ProductionHouse, \
    Cast, Credit, Location

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Trivia)
admin.site.register(Review)
admin.site.register(Role)
admin.site.register(ProductionHouse)
admin.site.register(Cast)
admin.site.register(Credit)
admin.site.register(Location)

