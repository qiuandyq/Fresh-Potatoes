from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, AddToMoviesForm
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
    return render(request, 'users/profile.html')


@login_required
def survey(request):
    if request.method == 'POST':
        logger.info(request.POST)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Updated')
            return redirect('survey_movies')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/survey.html', {'p_form': p_form})

@login_required
def survey_movies(request):

    # defining the search and putting it into context
    query = request.GET.get('search')
    if query is None:
        query = ""

    if query != "" :
        # fill results in categories
        context = {
            "query": query,
            "movie_results": api.search_movie_id(query)['results'],
            "tv_results": api.search_tv_id(query)['results']
        }
    else :
        context = {
            "query": query,
            "movie_results": {},
            "tv_results": {}
        }

    for item in context['movie_results']:
        item['poster_path'] = api.get_details("movie", item['id'])['poster_path']
    for item in context['tv_results']:
        item['poster_path'] = api.get_details("tv", item['id'])['poster_path']
    
    # grabs old movie list however it fetches its string so need to remove these characters [] ' "
    profile = request.user.profile
    tv = profile.tv
    tv = tv.replace('\'', '').replace('[', '').replace(']', '')
    movies = profile.movies
    movies = movies.replace('\'', '').replace('[', '').replace(']', '')

    logger.info(request.POST)

    if request.method == 'POST':
        post_value = request.POST.copy()
        selectedValues = str(post_value)

        # finds string movies and returns index, if not found then return -1
        try:
            indMov = selectedValues.index('movies\':')
        except ValueError:
            indMov = -1
        # finds string tv and returns index, if not found then return -1
        try:
            indTV = selectedValues.index('tv\':')
        except ValueError:
            indTV = -1

        # if the index of string isnt one, then remove the following characters from the string []'"
        if indMov != -1:
            strMovie = selectedValues[indMov + 7:indTV].replace('\'', '').replace('[', '').replace(']', '').replace(':', '').replace('>', '').replace('}', '')
            logger.info(strMovie)
        if indTV != -1:
            strTV = selectedValues[indTV + 3:].replace('\'', '').replace('[', '').replace(']', '').replace(':', '').replace('>', '').replace('}', '')
            logger.info(strTV)

        # checks if a movie has been selected
        if indMov != -1:
            strMovie = strMovie + ', ' + movies
        else:
            strMovie = movies

        post_value['movies'] = strMovie
        
        #checks if a tv show has been selected
        if indTV != -1:
            strTV = strTV + ', ' + tv
            post_value['tv'] = strTV
        else:
            strTV = tv

        form = AddToMoviesForm(post_value, instance = request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Updated')
            return redirect('home')

    return render(request, 'users/survey_movies.html', {'context': context})