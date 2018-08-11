from django.urls import path

from movie import views

app_name = 'movie'
urlpatterns = [
    path('<int:pk>/', views.FilmDetail.as_view(), name='detail'),
    path('', views.MovieList.as_view(), name='list'),
]
