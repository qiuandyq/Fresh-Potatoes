from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput
from .models import Profile
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import api.api_get as api

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    counter = 0
    context = {}
    for item in api.get_popular('movie')['results']:
        context[f'popular_movie{counter}'] = {
            "title": item['title'],
            "poster_path": item['poster_path'] 
        }
        counter = counter + 1

    MOVIES = (
        (context['popular_movie0']['title'], context['popular_movie0']['poster_path']),
        (context['popular_movie1']['title'], context['popular_movie1']['poster_path']),
        (context['popular_movie2']['title'], context['popular_movie2']['poster_path']),
        (context['popular_movie3']['title'], context['popular_movie3']['poster_path']),
        (context['popular_movie4']['title'], context['popular_movie4']['poster_path']),
        (context['popular_movie5']['title'], context['popular_movie5']['poster_path']),
        (context['popular_movie6']['title'], context['popular_movie6']['poster_path']),
        (context['popular_movie7']['title'], context['popular_movie7']['poster_path']),
        (context['popular_movie8']['title'], context['popular_movie8']['poster_path']),
    )

    GENRES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Animation', 'Animation'),
        ('Comedy', 'Comedy'),
        ('Crime', 'Crime'),
        ('Documentary', 'Documentary'),
        ('Drama', 'Drama'),
        ('Family', 'Family'),
        ('Fantasy', 'Fantasy'),
        ('History', 'History'),
        ('Horror', 'Horror'),
        ('Music', 'Music'),
        ('Mystery', 'Mystery'),
        ('Romance', 'Romance'),
        ('Science Fiction', 'Science Fiction'),
        ('TV Movie', 'TV Movie'),
        ('Thriller', 'Thriller'),
        ('War', 'War'),
        ('Western', 'Western'),
    )

    SERVICES = (
        ('Netflix', 'Netflix'),
        ('Prime Video', 'Prime Video'),
        ('Crave TV', 'Crave TV'),
        ('Hulu', 'Hulu'),
        ('Disney+', 'Disney+'),
        ('HBO Max', 'HBO Max'),
        ('Other', 'Other')
    )

    dob = forms.DateField(label="Date of Birth", widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    genre = forms.MultipleChoiceField(label="Genres", widget=forms.CheckboxSelectMultiple, choices=GENRES)
    stream = forms.MultipleChoiceField(label="What streaming services do you use?", widget=forms.CheckboxSelectMultiple, choices=SERVICES)
    movies = forms.MultipleChoiceField(label="Select any movies that you like", widget=forms.CheckboxSelectMultiple, choices=MOVIES, required=False)
    class Meta:
        model = Profile
        fields = ['dob', 'genre', 'stream', 'movies']