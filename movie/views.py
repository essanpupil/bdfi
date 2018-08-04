from django.shortcuts import render

from movie.models import Movie


def home(request):
    feature_films = Movie.objects.order_by('?')[:3]
    context = {'feature_films': feature_films}
    return render(request, 'movie/index.html', context)
