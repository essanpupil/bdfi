from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from news import models
from news.models import News


class NewsList(ListView):
    model = models.News
    template_name = 'news/news_list.html'


class NewsDetail(DetailView):
    model = models.News
    template_name = 'news/news_detail.html'


class AddNews(CreateView):
    model = News
    fields = ('__all__')
    template_name = 'news/news_form.html'
    success_url = reverse_lazy('news:list')
