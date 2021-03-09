import json
import requests

api_key = "0cda82335e834f31bcbc8a847a151fe5"
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

    if details['poster_path'] != None:
        details['poster_path'] = "https://image.tmdb.org/t/p/w200" + details['poster_path']
    else:
        details['poster_path'] = "https://i.ibb.co/8KK48QG/image404.jpg"
    if details['backdrop_path'] != None:
        details['backdrop_path'] = "https://image.tmdb.org/t/p/w500" + details['backdrop_path']
    # rename 'name' key to 'title'


    return details

# get list of trending movies or tv shows
# param1: string, type of media ('all', 'movie', 'tv', 'person')
# param2: string,  time window ('day', 'week')
# return: JSON list of trending movies or tv shows
def get_trending(media_type, time_window, page=1):
    response = requests.get(f"{url_base}/trending/{media_type}/{time_window}?api_key={api_key}&page={page}")

    # check API request status code
    if response.status_code != 200:
        print(f"error: request error code {response.status_code}")
        return response.status_code

    trending = response.json()
    
    # replace with full url path
    update_urls(trending['results'])
    # rename 'name' key to 'title'
    for result in trending['results']:
        if result['media_type'] == 'tv':
            result['title'] = result.pop('name')

    return trending

# get list of popular movies or tv shows
# param: string, type of media ('movie', 'tv')
# optional param: page (pass as 'page=#', default=1)
# return: JSON list of popular movies or tv shows
def get_popular(media_type, page=1):
    response = requests.get(f"{url_base}/{media_type}/popular?api_key={api_key}&page={page}")

    # check API request status code
    if response.status_code != 200:
        print(f"error: request error code {response.status_code}")
        return response.status_code

    popular = response.json()

    # replace with full url path
    update_urls(popular['results'])
    # rename 'name' key to 'title'
    if (media_type == 'tv'):
        for result in popular['results']:
            result['title'] = result.pop('name')

    return popular

# get list of upcoming movies (only for movies)
# optional param: page (pass as 'page=#', default=1)
# return: JSON list of upcoming movies
def get_upcoming(page=1):
    response = requests.get(f"{url_base}/movie/upcoming?api_key={api_key}&page={page}")

    # check API request status code
    if response.status_code != 200:
        print(f"error: request error code {response.status_code}")
        return response.status_code

    # get results from API
    upcoming = response.json()
    
    # replace with full url path
    update_urls(upcoming['results'])

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

    # if (media_type == 'tv'):
    #     genres['title'] = genres.pop('name')

    return genres

#search for a movie in the API and give back all related searches and their id's
#param1: string, the movie titles
#return: JSON, list of movies matching search title
def search_movie_id(movie_title):
  url_title = movie_title.replace(" ","%20")
  response = requests.get(f"{url_base}/search/movie?api_key={api_key}&query={url_title}")
  search_result = response.json()

  id_dict = {}
  id_dict['results'] = []
  result_num = 0
  for result in search_result['results']:
    result_num += 1
    id_dict['results'].append(
        {
            "title": result['title'],
            "id": result["id"]
        }
    )
 
  return id_dict

#search for a tv in the API and give back all related searches and their id's
#param1: string, the titles
#return: JSON, list of movies matching search title
def search_tv_id(title):
  url_title = title.replace(" ","%20")
  response = requests.get(f"{url_base}/search/tv?api_key={api_key}&query={url_title}")
  search_result = response.json()

  id_dict = {}
  id_dict['results'] = []
  
  result_num = 0
  for result in search_result['results']:
    result_num += 1
    id_dict['results'].append(
        {
            "title": result['name'],
            "id": result["id"]
        }
    )
    #id_dict[result['name']+" id"] = result["id"]
 
  return id_dict


#get the movie/tv poster and other images given the movie/tv id
def get_images(media_type, id):
    response = requests.get(f"{url_base}/{media_type}/{id}/images?api_key={api_key}")
    result = response.json()

    return result

"""
HELPER FUNCTIONS
"""

def update_urls(results):
    for item in results:
        item['poster_path'] = "https://image.tmdb.org/t/p/w200" + item['poster_path']
        item['backdrop_path'] = "https://image.tmdb.org/t/p/w500" + item['backdrop_path']



