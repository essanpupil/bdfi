from django.shortcuts import render

from movie.models import Movie, Genre


def home(request):
    newest_film = Movie.objects.last()
    feature_films = Movie.objects.exclude(id__in=[newest_film.id]).order_by('?')[:2]
    genre_list = Genre.objects.order_by('?')
    context = {
        'feature_films': feature_films,
        'genre_list': genre_list,
        'newest_film': newest_film,
    }
    return render(request, 'movie/index.html', context)
