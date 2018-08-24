from django.urls import path

from news import views

app_name = 'news'
urlpatterns = [
    path('add/', views.AddNews.as_view(), name='add'),
    path('<int:pk>/', views.NewsDetail.as_view(), name='detail'),
    path('', views.NewsList.as_view(), name='list'),
]
