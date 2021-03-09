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
        ('28', 'Action'),
        ('12', 'Adventure'),
        ('16', 'Animation'),
        ('35', 'Comedy'),
        ('80', 'Crime'),
        ('99', 'Documentary'),
        ('18', 'Drama'),
        ('10751', 'Family'),
        ('14', 'Fantasy'),
        ('36', 'History'),
        ('27', 'Horror'),
        ('10402', 'Music'),
        ('9648', 'Mystery'),
        ('10749', 'Romance'),
        ('878', 'Science Fiction'),
        ('10770', 'TV Movie'),
        ('53', 'Thriller'),
        ('10752', 'War'),
        ('37', 'Western'),
    )

    dob = forms.DateField(label="Date of Birth", widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    genre = forms.MultipleChoiceField(label="Genre", widget=forms.CheckboxSelectMultiple, choices=GENRES)
    class Meta:
        model = Profile
        fields = ['dob', 'genre']