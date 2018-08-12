from django.views.generic import ListView, DetailView

from news import models


class NewsList(ListView):
    model = models.News
    template_name = 'news/news_list.html'


class NewsDetail(DetailView):
    model = models.News
    template_name = 'news/news_detail.html'
