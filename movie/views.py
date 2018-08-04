from django.shortcuts import render

from movie.models import Movie, Genre


def home(request):
    feature_films = Movie.objects.order_by('?')[:3]
    genre_list = Genre.objects.order_by('?')
    context = {'feature_films': feature_films, 'genre_list': genre_list}
    return render(request, 'movie/index.html', context)
