from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # dob = forms.DateField(label="Date of Birth", widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))

    class Meta:
        model = User
        # fields = ['username', 'email', 'dob', 'password1', 'password2']
        fields = ['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
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

    dob = forms.DateField(label="Date of Birth", widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    genre = forms.MultipleChoiceField(label="Genre", widget=forms.CheckboxSelectMultiple, choices=GENRES)
    class Meta:
        model = Profile
        fields = ['dob', 'genre']