"""bdfi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie import views as movie_views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', movie_views.home, name='home'),
    path('left-sidebar', movie_views.left_sidebar, name='left'),
    path('right-sidebar', movie_views.right_sidebar, name='right'),
    path('no-sidebar', movie_views.no_sidebar, name='center'),
]
