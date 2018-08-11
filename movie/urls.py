from django.urls import path

from movie import views

app_name = 'movie'
urlpatterns = [
    path('<int:pk>/', views.FilmDetail.as_view(), name='detail'),
    path('tv/', views.TVList.as_view(), name='tv_list'),
    path('', views.MovieList.as_view(), name='movie_list'),
]
