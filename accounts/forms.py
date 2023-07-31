from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


from .models import CustomUser


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['first_name', 'username', 'password1', 'password2', 'email', 'date_of_birth']

