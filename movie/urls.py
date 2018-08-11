from django.urls import path

from movie import views

app_name = 'movie'
urlpatterns = [
    path('<int:pk>/', views.FilmDetail.as_view(), name='detail'),
    path('tv/', views.TVList.as_view(), name='tv_list'),
    path('actor/<int:pk>/', views.ActorDetail.as_view(), name='actor_detail'),
    path('actor/', views.ActorList.as_view(), name='actor_list'),
    path('', views.MovieList.as_view(), name='movie_list'),
]
