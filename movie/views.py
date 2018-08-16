from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView

from movie.models import Movie, Genre, Actor


def home(request):
    feature_films = Movie.objects.order_by('?')[:3]
    genre_list = Genre.objects.order_by('?')
    context = {
        'feature_films': feature_films,
        'genre_list': genre_list,
    }
    return render(request, 'movie/index.html', context)


class UserProfile(UpdateView):
    fields = ['first_name', 'last_name', 'email']
    template_name = 'account/profile.html'
    success_url = reverse_lazy('account_profile')

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
