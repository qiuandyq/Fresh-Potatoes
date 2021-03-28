from django.contrib import messages
from django.contrib.auth.forms import UsernameField
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm
from .models import Profile
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import api.api_get as api
from .forms import SearchForm
import logging

logger = logging.getLogger("mylogger")


def register(request):
    post = request.POST.copy()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been create, please log in to complete your survey!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    movie_details = []
    for item in profile.movies.replace(' ','').replace('[','').replace(']','').replace("'",'').split(','):
        if item:
            temp = {
                'poster_path': api.get_details("movie", int(item))['poster_path'],
                'id': int(item)
            }
            movie_details.append(temp)
    genres = []
    for item in profile.genre.replace(' ','').replace('[','').replace(']','').replace("'",'').split(','):
        if item:
            for genre in api.get_genre("movie")['genres']:
                if int(item) == int(genre['id']):
                    genres.append(genre['name'])
    services = []
    for item in profile.stream.replace(' ','').replace('[','').replace(']','').replace("'",'').split(','):
        if item:
            services.append(item)

    context = {
        'movies':movie_details,
        'genre':genres,
        'services':services,
    }
    return render(request, 'users/profile.html', context)


@login_required
def survey(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        post = request.POST.copy()
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Updated')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/survey.html', {'p_form': p_form})

@login_required
def survey_movies(request):
    search = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            print(title)
            return redirect('home')

    return render(request, 'users/survey_movies.html', {'search': search})