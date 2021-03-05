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
    dob = forms.DateField(label="Date of Birth", widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    
    class Meta:
        model = Profile
        fields = ['dob']