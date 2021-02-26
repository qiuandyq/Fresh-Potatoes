# Fresh Potatoes

## Dependencies

***Python 3.6** or newer is required

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

Webpage can be accessed on the browser at [127.0.0.1:8000](127.0.0.1:8000/) while the web server is running.

## Current Feature Implemented (Update 02/23/2021)
Fresh Potatoes web application now contains a fully operated login and registered system. The system is able to store a user's username and password as they registered to become one of the members of Fresh Potatoes. Furthermore, a profile feature has been implemented for each user who registered. Any changes or updates on users’ profile information will be saved and presented every time they login.

Following the current progression speed of the project, the homepage for unregistered users is completed along with login, register, and profile pages. The body of the homepage has been seperated into 4 sections with one featured movie at the top and 3 categorized columns of movie showcases beneath. The 3 columns of movies are listed as popular movies, trending movies, and upcoming movies for unregistered users. Every movie present in the homepage is directly pulled from a third party database using application programming interface.

The application programming interface that is introduced in our project is TMDb. In current progress, we are able to retrieve movie information including movie genres, poster, overview, and details including title, rating, budget, popularity, production and more. More API features require further research and implementation.


## Overview

![Demonstration Video](src/demo.mp4)

Fresh potatoes provides a simplified and more efficient movie searching process for any users that watches movies and TV shows at any age range. Though the recommendation option has been implemented on most of the streaming services, many users still feel lost while searching for something new to watch due to the limited content and overly complicated designs on most of the modern streaming services and databases such as Netflix and IMDb. Our project aims to solve that problem by implementing more defined and detailed recommendation options as well as filtering the movies and shows based on the streaming platforms they are on and provide a link to that platform. 

The main overarching features of this project consist of filter features, recommendations, as well as search functions. Some of our features can be classified as both filter features and recommendation features such as the search filter that can be used when searching the website for movies. 
The recommendations on the user’s homepage are optimized by filtering out the movie they might not enjoy as well as filtering out movies based on the user’s age in order to give them appropriate movie recommendations. For example a user who is 14 years old would not be recommended a movie that is rated for those who are 18+ ( the type of rating can be changed in the user’s preferences).
During the user’s initial signup we establish a basis for how movies should be filtered and recommended during the user’s first experience. We will have the user go through a survey to lay a foundation in order. The web site also has a recommendation feature where it recommends which streaming platform holds most of the movies it thinks the user would enjoy. From this information we can then further suggest what streaming platform might be best for the user. Each movie in the database would have a trailer, user rating, age rating, what platforms to watch it on, where a hardcopy can be found and a comment section where any (non banned) user can comment. A point for list of project features and subfeatures is listed below:

- Forgot password:
Clicking the forgot password button sends an email link to the customer’s email and the customer can reset their password through the link in the email.
- Recommendation system:
The recommendation system will be an account specific system. It will allow the user to enter their own preferences and recommend entertainment to them based on those preferences. Once a user is logged in, their home screen will display personalized movies to their liking.
- More inputs for survey to show recommendations accurately
In future iterations we hope to improve upon the recommendation feature by fleshing out the registration survey. We also want to track what the user likes and doesn’t like to try and incorporate these things into the recommendation algorithm as well.
- Individual movie pages 
Individual movie pages display more details for the selected movie, including the release date, genre, rating, story overview, link to watch the movie and many more. 
- Registered user homepage 
This is the homepage that will display customized content based on the users preferences.
- About page
This will be a page in which we describe our team and how we have completed the project.
- Search feature
This will be a typical search feature. It will allow the user to search for entertainment and give recommendations based on what they searched. The user will be able to navigate from the search page to any individual movie page.
- Rating System
This will be a system where a user can leave a rating out of 10 on a movie/show and have it contribute to an aggregate rating that is kept on the site.

