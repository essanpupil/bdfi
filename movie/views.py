from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView

from movie.models import Movie, Genre, Actor, Cast
from news.models import News


def home(request):
    feature_actor = Actor.objects.order_by('?').first()
    feature_news = News.objects.order_by('-id')[:3]
    feature_films = Movie.objects.order_by('?')[:3]
    genre_list = Genre.objects.order_by('?')
    context = {
        'feature_actor': feature_actor,
        'feature_films': feature_films,
        'feature_news': feature_news,
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

    def get_context_data(self, **kwargs):
        context = super(FilmDetail, self).get_context_data(**kwargs)
        casted_actor = Cast.objects.filter(movie=self.object).order_by('?').first()
        context['casted_actor'] = casted_actor.actor
        return context


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
