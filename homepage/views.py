from django.shortcuts import render
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import api.api_get as api

# Create your views here.
def homepage(request):
    counter = 0
    context = {}
    for item in api.get_trending('movie', 'week')['results']:
        context[f'trending_movie{counter}'] = {
            "title": item['title'],
            "overview": item['overview'],
            "poster_path": item['poster_path'] 
        }
        counter = counter + 1

    counter = 0
    for item in api.get_popular('movie')['results']:
        context[f'popular_movie{counter}'] = {
            "title": item['title'],
            "overview": item['overview'],
            "poster_path": item['poster_path'] 
        }
        counter = counter + 1

    counter = 0
    for item in api.get_upcoming()['results']:
        context[f'upcoming_movie{counter}'] = {
            "title": item['title'],
            "overview": item['overview'],
            "poster_path": item['poster_path'] 
        }
        counter = counter + 1
    return render(request, 'homepage/home.html', context)

def about(request):
    return render(request, 'homepage/about.html')