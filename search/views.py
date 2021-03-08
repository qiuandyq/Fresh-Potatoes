from django.shortcuts import render
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import api.api_get as api

def search(request):
    query = request.GET.get('q')

    return render(request, 'search/search.html', api.search_movie_id(query))