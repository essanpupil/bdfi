from django.conf.urls import url
from django.urls import path

from movie import views, autocompletes

app_name = 'movie'
urlpatterns = [
    url(r'^movie-title/$', autocompletes.MovieTitleAutocomplete.as_view(), name='movie_title_autocomplete'),
    path('<int:pk>/', views.FilmDetail.as_view(), name='detail'),
    path('new/', views.CreateMovie.as_view(), name='new_movie'),
    path('tv/', views.TVList.as_view(), name='tv_list'),
    path('actor/<int:pk>/', views.ActorDetail.as_view(), name='actor_detail'),
    path('actor/', views.ActorList.as_view(), name='actor_list'),
    path('', views.MovieList.as_view(), name='movie_list'),
]
