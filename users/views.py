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

def register(request):
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
    movies = profile.movies.replace(' ','').replace('[','').replace(']','').replace("'",'').split(',')
    poster = []
    for item in movies:
        poster_path = api.get_details("movie", int(item))
        poster.append(poster_path['poster_path'])
    genres = []
    for item in profile.genre.replace(' ','').replace('[','').replace(']','').replace("'",'').split(','):
        for genre in api.get_genre("movie")['genres']:
            if int(item) == int(genre['id']):
                genres.append(genre['name'])
    services = []
    for item in profile.stream.replace(' ','').replace('[','').replace(']','').replace("'",'').split(','):
        services.append(item)
    context = {

        'movies':poster,
        'genre':genres,
        'services':services,
    }
    return render(request, 'users/profile.html')

@login_required
def survey(request):
    # counter = 0
    # context = {}
    # for item in api.get_popular('movie')['results']:
    #     context[f'popular_movie{counter}'] = {
    #         "title": item['title'],
    #         "overview": item['overview'],
    #         "poster_path": item['poster_path'] 
    #     }
    #     counter = counter + 1

    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Updated')
            return redirect('home')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/survey.html', {'p_form': p_form})
