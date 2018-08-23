from dal import autocomplete

from movie.models import Movie


class MovieTitleAutocomplete(autocomplete.Select2ListView):
    def create(self, text):
        return text

    def get_list(self):
        title_list = Movie.objects.all().values_list('title', flat=True)
        return list(title_list)
