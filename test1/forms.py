from django import forms
from .models import CustomUser, Movie, Comment
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField

class CustomRegisterForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'birth_date', 'city', 'country', 'bio', 'avatar', 'captcha']

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'poster', 'youtube_trailer']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']