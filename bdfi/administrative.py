from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, PasswordInput


class SignupForm(ModelForm):
    password_again = CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_again']
        widgets = {
            'password_again': PasswordInput,
            'password': PasswordInput
        }
