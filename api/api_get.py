import json
import requests

api_key="0cda82335e834f31bcbc8a847a151fe5"
url_base = "https://api.themoviedb.org/3"



# get details of title ERROR CHECKING NEEDS WORK
# param1: string, type of media (either 'tv' or 'movie')
# param2: string, title ID 
# return: JSON of movie details
def get_details(media_type, id):
    # check if valid media_type
    print((media_type != 'tv') and (media_type != 'movie'))
    if ((media_type != 'tv') and (media_type != 'movie')):
        print("error: invalid media_type")
        return 1

    response = requests.get(f"{url_base}/{media_type}/{id}?api_key={api_key}")

    # check API request status code
    print(response.status_code)
    if (response.status_code != 200):
        error_code = response.status_code
        print(f"error: error code {error_code}")
        return error_code

    details = response.json()

    if (media_type == 'tv'):
        details['title'] = details.pop('name')

    return details

# get list of trending titles
# param1: string, type of media ('all', 'movie', 'tv', 'person')
# param2: string,  time window ('day', 'week')
# return: JSON list of trending titles
def get_trending(media_type, time_window):
    trending_response = requests.get(f"{url_base}/trending/{media_type}/{time_window}?api_key={api_key}")
    trending = trending_response.json()
    
    for result in trending['results']:
        if (result['media_type'] == 'tv'):
            result['title'] = result.pop('name')

    return trending

# get list of titles
# param1: string, type of media ('movie', 'tv')
# param2: string, type of search ('popular', 'trending', 'upcoming')
# return: JSON list of titles
def get_list(media_type, search_type):
    titles_response = requests.get(f"{url_base}/{media_type}/{search_type}?api_key={api_key}")
    titles = titles_response.json()

    for result in titles['results']:
        if (result['media_type'] == 'tv'):
            result['title'] = result.pop('name')

    return titles

# param1: string, type of media (either 'tv' or 'movie')
# param2: string, title ID 
#return: JSON list of genres for movie
def get_genre(media_type, id):
  response = requests.get(f"{url_base}/genre/{media_type}/list?api_key={api_key}")
  genres = response.json()

  if (media_type == 'tv'):
    genres['title'] = genres.pop('name')

  return genres

#param1: string, the movie titles
#return: JSON, list of movies matching search title
def search_movie_id(movie_title):
  url_title = movie_title.replace(" ","%20")
  print(url_title)
  response = requests.get(f"{url_base}/search/movie?api_key={api_key}&query={url_title}")
  search_result = response.json()

  id_dict = {}
  result_num = 0
  for result in search_result['results']:
    # if result['title'] == movie_title:
    result_num += 1
    # movie_num  =  "Result " + str(result_num)
    id_dict[result['title']+" id"] = result["id"]
 
  return id_dict
  #print(search_result['results'])
  

#print(get_genre('movie',458576))
#print(search_movie("Monster Hunter"))
print(search_movie_id("Jurassic Park"))
#print(get_details('movie',458576))
#print(get_details('tv', '111111'))