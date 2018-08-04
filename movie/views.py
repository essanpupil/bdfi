from django.shortcuts import render

from movie.models import Movie


def home(request):
    feature_films = Movie.objects.all()[:3]
    context = {'feature_films': feature_films}
    return render(request, 'movie/index.html', context)


def left_sidebar(request):
    return render(request, 'movie/left-sidebar.html')


def right_sidebar(request):
    return render(request, 'movie/right-sidebar.html')


def no_sidebar(request):
    return render(request, 'movie/no-sidebar.html')
