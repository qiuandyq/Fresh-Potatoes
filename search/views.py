from django.shortcuts import render
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import api.api_get as api

def search(request):
    query = request.GET.get('q')
    context = {
        "movie_results": api.search_movie_id(query)['results'],
        "tv_results": api.search_tv_id(query)['results']
    }

    for item in context['movie_results']:
        item['poster_path'] = api.get_details("movie", item['id'])['poster_path']
    for item in context['tv_results']:
        item['poster_path'] = api.get_details("tv", item['id'])['poster_path']

    return render(request, 'search/search.html', context)