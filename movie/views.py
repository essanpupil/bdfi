from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from movie.models import Movie, Genre, Actor


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


class UserProfile(DetailView):
    template_name = 'account/profile.html'

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)


class FilmDetail(DetailView):
    model = Movie
    template_name = 'movie/movie_detail.html'


class ActorDetail(DetailView):
    model = Actor
    template_name = 'movie/actor_detail.html'


class MovieList(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'
    queryset = Movie.objects.filter(category=Movie.FILM)


class TVList(ListView):
    model = Movie
    template_name = 'movie/tv_list.html'
    queryset = Movie.objects.filter(category=Movie.TV_SERIES)


class ActorList(ListView):
    model = Actor
    template_name = 'movie/actor_list.html'
