from django.shortcuts import render
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import api.api_get as api

# Create your views here.
def homepage(request):
    counter = 1
    context = {

        "info_url": 'more_info' # *** if you change this: make sure the right side 
                                        # to match the first part of the more_info path in urls.py 

    }
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
        
        if (api.get_details('movie', int (item['id']))['status']!='Released'): #checks to see if movie has been released 
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

def more_info(request, movie_id): # takes in movie_id variable from the URL link (see the <> brackes in urls.py)
    
    item = api.get_details('movie', int(movie_id))
    trailer = api.get_trailer('movie', int(movie_id))['results'][0]
    

    context = {
        "id": item['id'],
        "title": item['title'],
        "overview": item['overview'],
        "poster_path": item['poster_path'], 
        "release_date": item['release_date'],
        "runtime": item['runtime'],
        "status":item['status'],
        "rating":item['vote_average'],
        "trailer":trailer['key'],
    }
    

    return render(request, 'homepage/more_info.html', context )