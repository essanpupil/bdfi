from dal import autocomplete
from django import forms

from movie.models import Movie


class MovieForm(forms.ModelForm):
    title = autocomplete.Select2ListCreateChoiceField(widget=autocomplete.ListSelect2(url='movie:movie_title_autocomplete'))

    class Meta:
        model = Movie
        fields = ('__all__')
