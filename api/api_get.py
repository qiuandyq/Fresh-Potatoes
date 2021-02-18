import json
import requests

api_key="0cda82335e834f31bcbc8a847a151fe5"
url_base = "https://api.themoviedb.org/3"

# get details of movies or tv shows
# param1: string, type of media (either 'tv' or 'movie')
# param2: string, title ID 
# return: JSON of movie or tv show details
def get_details(media_type, id):
    response = requests.get(f"{url_base}/{media_type}/{id}?api_key={api_key}")

    # check API request status code
    if response.status_code != 200:
        print(f"error: request error code {response.status_code}")
        return response.status_code

    details = response.json()

    # rename 'name' key to 'title'
    if media_type == 'tv':
        details['title'] = details.pop('name')

    return details

# get list of trending movies or tv shows
# param1: string, type of media ('all', 'movie', 'tv', 'person')
# param2: string,  time window ('day', 'week')
# return: JSON list of trending movies or tv shows
def get_trending(media_type, time_window):
    response = requests.get(f"{url_base}/trending/{media_type}/{time_window}?api_key={api_key}")

    # check API request status code
    if response.status_code != 200:
        print(f"error: request error code {response.status_code}")
        return response.status_code

    trending = response.json()
    
    # rename 'name' key to 'title'
    for result in trending['results']:
        if result['media_type'] == 'tv':
            result['title'] = result.pop('name')

    return trending

# get list of popular movies or tv shows
# param1: string, type of media ('movie', 'tv')
# return: JSON list of popular movies or tv shows
def get_popular(media_type):
    response = requests.get(f"{url_base}/{media_type}/popular?api_key={api_key}")

    # check API request status code
    if response.status_code != 200:
        print(f"error: request error code {response.status_code}")
        return response.status_code

    popular = response.json()

    # rename 'name' key to 'title'
    if (media_type == 'tv'):
        for result in popular['results']:
            result['title'] = result.pop('name')

    return popular

# get list of upcoming movies (only for movies)
# return: JSON list of upcoming movies
def get_upcoming():
    response = requests.get(f"{url_base}/movie/upcoming?api_key={api_key}")

    # check API request status code
    if response.status_code != 200:
        print(f"error: request error code {response.status_code}")
        return response.status_code

    upcoming = response.json()

    return upcoming

# get all genres associated with movie or tv show
# param1: string, type of media (either 'tv' or 'movie')
# param2: string, title ID 
# return: JSON list of genres for movie
def get_genre(media_type, id):
    response = requests.get(f"{url_base}/genre/{media_type}/list?api_key={api_key}")

    # check API request status code
    if response.status_code != 200:
        print(f"error: request error code {response.status_code}")
        return response.status_code

    genres = response.json()

    if (media_type == 'tv'):
        genres['title'] = genres.pop('name')

    return genres

#param1: string, the movie titles
#return: JSON, list of movies matching search title
# def search_movie(movie_title):
#   url_title = movie_title.replace(" ","%20")
#   print(url_title)
#   response = requests.get(f"{url_base}/search/movie?api_key={api_key}&query={url_title}")
#   search_result = response.json()
  
#   # for result in search_result['results']:
#     # if search_result['title'] != movie_title:
#     #   search_result.pop(result)
#   #   print(search_result[result])

#   print(search_result)
  

# print(get_genre('movie',458576))
# print(search_movie("Monster Hunter"))
# search_movie("Monster Hunter")
