# Fresh Potatoes

## Dependencies

Install dependencies with `requirements.txt`

```
pip install -r requirements.txt
```

Alternatively,

```
pip install django django-crispy-forms requests
```

## Instructions

```
git clone https://csil-git1.cs.surrey.sfu.ca/fresh-potatoes/fresh-potatoes.git
cd fresh-potatoes
python manage.py runserver
```

## Overview

![Demonstration Video](src/demo.mp4)

Fresh potatoes provides a simplified and more efficient movie searching process for any users that watches movies and TV shows at any age range. Though the recommendation option has been implemented on most of the streaming services, many users still feel lost while searching for something new to watch due to the limited content and overly complicated designs on most of the modern streaming services and databases such as Netflix and IMDb. Our project aims to solve that problem by implementing more defined and detailed recommendation options as well as filtering the movies and shows based on the streaming platforms they are on and provide a link to that platform. 

The main overarching features of this project consist of filter features, recommendations, as well as search functions. Some of our features can be classified as both filter features and recommendation features such as the search filter that can be used when searching the website for movies. 
The recommendations on the user’s homepage are optimized by filtering out the movie they might not enjoy as well as filtering out movies based on the user’s age in order to give them appropriate movie recommendations. For example a user who is 14 years old would not be recommended a movie that is rated for those who are 18+ ( the type of rating can be changed in the user’s preferences).
During the user’s initial signup we establish a basis for how movies should be filtered and recommended during the user’s first experience. We will have the user go through a survey to lay a foundation in order. The web site also has a recommendation feature where it recommends which streaming platform holds most of the movies it thinks the user would enjoy. From this information we can then further suggest what streaming platform might be best for the user. Each movie in the database would have a trailer, user rating, age rating, what platforms to watch it on, where a hardcopy can be found and a comment section where any (non banned) user can comment. A point for list of project features and subfeatures is listed below:

- Login system
- Get list of movies and show from an API
- Filtering based off what platform they appear on -- depends on API (2)- combine
    - Worry about overlapping API info
- Users can add movies and shows to a watch later list
- Feature to like and dislike movies -- user rating 
- Buy a hard copy -- if it's available for hard copy
- Upcoming movies feature (API)
- Recommend streaming services that has majority of their recommended movies
- Signup page -- filters users interests
- Changing recommendations based on watch later list -- Ratio 
    - 6 romance and 4 action movies
    - 12 romance and 8 action on homepage
- Search individual movies 
    - Trailer with movie
- A filter that restricts movies based on their rating
    - Filtered search
    - Account feature -- enable filter that is based on their age
    - You can go into your individual preferences
    - A survey to quickly pull recommendations that you might like given information you filled out in the survey
- Creating a mobile design (if we have extra time )
