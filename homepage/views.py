from django.shortcuts import render, redirect
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import api.api_get as api
from .forms import SearchForm
from users.models import Profile, WatchLaterEntry
from django.http import HttpResponse
import logging
from django.contrib.auth.models import User
from users.forms import AddToMoviesForm, ProfileUpdateForm
from django.contrib import messages


logger = logging.getLogger("mylogger")
# Create your views here.
def homepage(request):
    
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            print(title)

            
    form = SearchForm()
    counter = 1
    context = {

        "info_url": 'more_info',
        'form':form, # *** if you change this: make sure the right side 
                                        # to match the first part of the more_info path in urls.py 

    }
    

    if request.user.is_authenticated:
        #get the reccomended movies
        profile = request.user.profile
        movies = profile.movies
        print(movies)
        movies = movies.replace(' ','').replace('[','').replace(']','').replace("'",'').split(',')
        print(movies)
        print(movies)
        del movies[-1]
        # print(movies)
        movies = [int(x) for x in movies]
        genres = profile.genre

        reco_movies = api.get_recommendation('movie',movies)
        counter = 1
        for i in reco_movies:
            curr_movie = api.get_details('movie',int(i))
            
            context[f'for_you{counter}'] = {
                "title": curr_movie['title'],
                "overview": curr_movie['overview'],
                "poster_path": curr_movie['poster_path'], 
                "id": curr_movie['id'], # get the movie's id so we can use it in our href later
            }
            counter = counter +1

    counter = 1
    for item in api.get_trending('movie', 'week')['results']:
        context[f'trending_movie{counter}'] = {
            "title": item['title'],
            "overview": item['overview'],
            "poster_path": item['poster_path'], 
            "id": item['id'], # get the movie's id so we can use it in our href later
        }
        counter = counter + 1

    counter = 1
    for item in api.get_popular('movie')['results']:
        context[f'popular_movie{counter}'] = {
            "title": item['title'],
            "overview": item['overview'],
            "poster_path": item['poster_path'],
            "id": item['id'],
        }
        counter = counter + 1
    
    counter = 1
    for item in api.get_upcoming()['results']:
        
        # if (api.get_details('movie', int (item['id']))['status']!='Released'): #checks to see if movie has been released 
        context[f'upcoming_movie{counter}'] = {
            "title": item['title'],
            "overview": item['overview'],
            "poster_path": item['poster_path'],
            "id": item['id'], 
                
        }
        counter = counter + 1

    return render(request, 'homepage/home.html', context)

def about(request):
    return render(request, 'homepage/about.html')


def faq(request):
    faqs=[
        {   
            'quest_num': 'question-1',
            'question': 'Q: Can I get a signed Fresh Potatoes poster?',
            'ans_num': 'answer-1',
            'answer': '''Unfortunately, we are out of stock of Fresh Potato posters at the moment. 
                         However, we are more than happy to send you a signed potato 
                        (your choice of sweet or regular) in the mail just for you!
                        ''',
            'target': '#answer-1' # this part must be the same as the 'ans_num' field with a # infront of it.
        },
        {
            'quest_num': 'question-2',
            'question': 'Q: Is it pronounced "po-tay-toe" or "po-tah-ta"?',
            'ans_num': 'answer-2',
            'answer': '''
                    Potato, potahto, tomato, tomahto.
                    Let's call the whole thing off.
                        ''',
            'target': '#answer-2'
        },
        {
            'quest_num': 'question-3',
            'question': 'Q: Why did you pick the name "Fresh Potatoes"?',
            'ans_num': 'answer-3',
            'answer': ''' Because we thought the name was SPUDtacular as we found it very aPEELing.
                        ''',
            'target': '#answer-3'
        },
        {
            'quest_num': 'question-4',
            'question': 'Q: What do you call a lazy baby kangaroo?',
            'ans_num': 'answer-4',
            'answer': ''' A POUCH-potato.
                        ''',
            'target': '#answer-4'
        }
    ] #end of faq dictionary

    context= {

        'faqs':faqs # we can use 'faqs' as a variable in our faq.html file now
    }

    return render(request, 'homepage/faq.html', context)


def get_service_provider(service_type, provider_api_info): #service type will be either "flatrate", "rent" or "buy"
    country= 'CA'
    if service_type=='flatrate': # rename 'flatrate' to 'stream'
        kind='stream'
    else:
        kind= service_type #otherwise keep the original sertice type (i.e 'buy' or 'rent')

    service_providers={}
    if bool(provider_api_info) and country in provider_api_info: #check to see if information exists for the country
        if service_type in provider_api_info[country]:
            counter=1

            for stream_service in provider_api_info[country][str(service_type)]: # get all the providers for the service type

                service_providers[f"provider{counter}"]={ #collect providers info in a dictionary

                    'logo' : "https://image.tmdb.org/t/p/w45/"+stream_service["logo_path"],
                    'name' : stream_service["provider_name"],
                    'type' : kind,
                
                
                }    
                counter=counter+1
    

    else:
        service_providers=0 #if there is no info for the country set to false


    return service_providers

def more_info(request, media_type , movie_id): # takes in movie_id variable from the URL link (see the <> brackes in urls.py)
    
    item = api.get_details(media_type, int(movie_id))
    trailer = api.get_trailer( media_type, int(movie_id))['results']
    if bool(trailer):
        trailer = trailer[0]['key']
    else:
        trailer = 0

    provider= api.get_provider(media_type, int(movie_id))['results']
    stream= api.get_provider(media_type, int(movie_id))['results']
    if bool(provider) and 'CA' in provider:
        provider = provider['CA']['link']

        #provider_stream= provider_stream['flatrate']
    else:
        provider = 0
 
    #country= 'CA'
    stream_service_providers= get_service_provider('flatrate', stream)

    rent_service_providers = get_service_provider('rent', stream)

    buy_service_providers= get_service_provider('buy', stream)

    kinds=['stream','rent','buy']

    service_providers=-1
    if stream_service_providers or buy_service_providers or rent_service_providers:
        service_providers={

        'stream': stream_service_providers,
        'rent' : rent_service_providers,
        'buy': buy_service_providers,
        'kind': kinds,


        }
    else:
        service_providers=0

    


 #assigning correct name for titles
    if media_type=='movie':
        title=item['title']
        liked_list= "Liked Movies"

    if media_type=='tv':
        title=item['name']
        liked_list= "Liked TV Shows"

    #assigning correct name for release dates
    if media_type=='movie':
        release=item['release_date']

    if media_type=='tv':
        release=item['first_air_date']
    
      #assigning correct name for run time
    if media_type=='movie':
        runtime=item['runtime']

    if media_type=='tv':
        runtime=item['episode_run_time']
        if runtime==[]:
            runtime='?'
        else:
            runtime = str(runtime)[1:3]

    # check if movie is already added to watch later list
    exists_watchlater = False
    if request.user.is_authenticated:
        watchlater_list = Profile.objects.get(user=request.user).watchlater.all()
        for i in watchlater_list:
            if i.movie_id == movie_id:
                exists_watchlater = True

    # check if movie has just been added and display message
    action = False
    message = ""
    if request.GET.get('action') == "ADD":
        action = True
        print(f"Adding movie {item['id']} to watchlater list")
        message = """Movie successfully added, check it out <a href="/farm">here</a>"""
    elif request.GET.get('action') == "REMOVE":
        action = True
        print(f"Removing movie {item['id']} to watchlater list")
        message = """Movie successfully removed, check it out <a href="/farm">here</a>"""

    context = {
        "id": item['id'],
        "title": title,
        "overview": item['overview'],
        "poster_path": item['poster_path'], 
        "release_date": release,
        "runtime": runtime,
        "status":item['status'],
        "rating":item['vote_average'],
        "trailer":trailer,
        "provider_link":provider,
        'providers': service_providers,
        'genres':item['genres'],
        "media_type":media_type,
        "exists_watchlater": exists_watchlater,
        "action": action,
        "message": message,
        'liked_list': liked_list
    }   
    
    # grabs old movie list however it fetches its string so need to remove these characters [] ' "
    if request.method == 'POST':
        post_value = request.POST.copy()
        profile = request.user.profile

        tv = profile.tv
        tv = tv.replace('\'', '').replace('[', '').replace(']', '')

        if media_type=='tv':
            strTV = str(movie_id) + ', ' + tv
            post_value['tv'] = strTV
            #return redirect(f'/../FAQ/')
        else:
            tv = profile.tv 
            post_value['tv']= tv 

        movies = profile.movies
        movies = movies.replace('\'', '').replace('[', '').replace(']', '')  

        if media_type=='movie':
            strMovie = str(movie_id) + ', ' + movies
            post_value['movies'] = strMovie
        else:
            movies=profile.movies
            post_value['movies']=movies

        logger.info(request.POST)
        form = AddToMoviesForm(post_value, instance = request.user.profile)
     

        if form.is_valid():
            form.save()
            messages.success(request, f'Updated')
            return redirect(f'/../added_done/{media_type}/{movie_id}/')

        #for movie in post_value['tv']:
         #   print(movie)

        
    return render(request, 'homepage/more_info.html', context )



def farm(request):
    # get user data and watch later list
    profile = Profile.objects.get(user=request.user)
    watchlater_list = []
    
    # get details for each item
    for item in profile.watchlater.all():
        entry = {
            'title': item.title,
            'media_type': item.media_type,
            'id': item.movie_id,
            'poster_path': api.get_details(item.media_type, item.movie_id)['poster_path']
        }
        watchlater_list.append(entry)
    
    context = {
        'watchlater_list': watchlater_list
    }
    
    return render(request, 'homepage/potato_farm.html', context)

def farmedit(request):
    # get user data and watch later list
    profile = Profile.objects.get(user=request.user)
    watchlater_list = []
    
    # get details for each item
    for item in profile.watchlater.all():
        entry = {
            'title': item.title,
            'media_type': item.media_type,
            'id': item.movie_id,
            'poster_path': api.get_details(item.media_type, item.movie_id)['poster_path']
        }
        watchlater_list.append(entry)
    
    context = {
        'watchlater_list': watchlater_list
    }
    
    return render(request, 'homepage/potato_farm_edit.html', context)

def add_watch_later(request, media_type, movie_id):
    profile = Profile.objects.get(user=request.user)
    entry = WatchLaterEntry(title=api.get_details(media_type, movie_id)['title'], media_type=media_type, movie_id=movie_id)
    entry.save()
    duplicate = False
    for item in profile.watchlater.all():
        if item.movie_id == entry.movie_id:
            duplicate = True

    if duplicate == False:
        profile.watchlater.add(entry)
    else:
        entry.delete()
    context = {
        'media_type': media_type,
        'movie_id': movie_id,
    }
    return HttpResponse(""f"<html><script>window.location.replace('/more_info/{media_type}/{movie_id}/?action=ADD');</script></html>""")

def remove_watch_later(request, media_type, movie_id, source):
    profile = Profile.objects.get(user=request.user)
    if media_type == "all":
        profile.watchlater.all().delete()
        return HttpResponse(""f"<html><script>window.location.replace('/farm/');</script></html>""")
    else:
        exists = False
        for item in profile.watchlater.all():
            if item.movie_id == movie_id:
                item.delete()
                exists = True
    context = {
        'media_type': media_type,
        'movie_id': movie_id,
    }
    if source == "farmedit":
        return HttpResponse(""f"<html><script>window.location.replace('/farmedit/');</script></html>""")
    return HttpResponse(""f"<html><script>window.location.replace('/more_info/{media_type}/{movie_id}/?action=REMOVE');</script></html>""")
    




def movie_added(request, media_type , movie_id):
    item = api.get_details(media_type, int(movie_id))

    if media_type=='movie':
        title=item['title']
        header="Movie"

    if media_type=='tv':
        title=item['name']
        header= "TV show"

    context = {

        "title": title,
        "poster_path": item['poster_path'], 
        "id":movie_id,
        "type":media_type,
        "header":header,

    }

    return render(request, 'homepage/added_movie_done.html', context)
