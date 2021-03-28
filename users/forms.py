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

class AddToMoviesForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['movies', 'tv']

class SearchForm(forms.Form):
    title = forms.CharField()
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
            "poster_path": item['poster_path'],
            "id":item['id'],
        }
        counter = counter + 1

    

    MOVIES = (
        (context['popular_movie0']['id'], context['popular_movie0']['poster_path']),
        (context['popular_movie1']['id'], context['popular_movie1']['poster_path']),
        (context['popular_movie2']['id'], context['popular_movie2']['poster_path']),
        (context['popular_movie3']['id'], context['popular_movie3']['poster_path']),
        (context['popular_movie4']['id'], context['popular_movie4']['poster_path']),
        (context['popular_movie5']['id'], context['popular_movie5']['poster_path']),
        (context['popular_movie6']['id'], context['popular_movie6']['poster_path']),
        (context['popular_movie7']['id'], context['popular_movie7']['poster_path']),
        (context['popular_movie8']['id'], context['popular_movie8']['poster_path']),
    )

    GENRES = (
        (28, 'Action'),
        (12, 'Adventure'),
        (16, 'Animation'),
        (35, 'Comedy'),
        (80, 'Crime'),
        (99, 'Documentary'),
        (18, 'Drama'),
        (10751, 'Family'),
        (14, 'Fantasy'),
        (36, 'History'),
        (27, 'Horror'),
        (10402, 'Music'),
        (9648, 'Mystery'),
        (10749, 'Romance'),
        (878, 'Science Fiction'),
        (10770, 'TV Movie'),
        (53, 'Thriller'),
        (10752, 'War'),
        (37, 'Western'),
    )

    SERVICES = (
        ('Netflix', 'Netflix'),
        ("Prime Video", 'Prime Video'),
        ('Crave TV', 'Crave TV'),
        ('Hulu', 'Hulu'),
        ('Disney+', 'Disney+'),
        ('HBO Max', 'HBO Max'),
        ('Other', 'Other')
    )

    dob = forms.DateField(label="Date of Birth", widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    genre = forms.MultipleChoiceField(label="Genres", widget=forms.CheckboxSelectMultiple, choices=GENRES)
    stream = forms.MultipleChoiceField(label="What streaming services do you use?", widget=forms.CheckboxSelectMultiple, choices=SERVICES)
    # movies = forms.MultipleChoiceField(label="Select any movies that you like", widget=forms.CheckboxSelectMultiple, choices=MOVIES, required=False)
    class Meta:
        model = Profile
        fields = ['dob', 
                    'genre', 
                    'stream', 
                    # 'movies'
                    ]