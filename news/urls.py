from django.urls import path

from news import views

app_name = 'news'
urlpatterns = [
    path('<int:pk>/', views.NewsDetail.as_view(), name='detail'),
    path('', views.NewsList.as_view(), name='list'),
]
