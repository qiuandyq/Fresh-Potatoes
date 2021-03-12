## Description

Fresh potatoes provides a simplified and more efficient movie searching process for any users that watches movies and TV shows at any age range. Though the recommendation option has been implemented on most of the streaming services, many users still feel lost while searching for something new to watch due to the limited content and overly complicated designs on most of the modern streaming services and databases such as Netflix and IMDb. Our project aims to solve that problem by implementing more defined and detailed recommendation options as well as filtering the movies and shows based on the streaming platforms they are on and provide a link to that platform. In this iteration our website allows the user to sign up for an account, login, logout and presents popular movies; trending movies; and upcoming movies based on their ranking. to either a logged in user or a logged-out user on our homepage. It also allows a logged in user to visit their user profile.

## User Stories

[Iteration 2](#iteration-2)

[Iteration 1](#iteration-1)

## Iteration 2

### User Stories 1

**User story**: As an eager fan I want to look up a movie to see when a movie will be released 

**Name**: Davy Jones

**Actors**: eager fan

**Precondition**: none

**Postcondition**: none

**Iteration**: 2

**Scenario**: Davy Jones is a fan of the Pirates of the Caribbean franchise and he has heard that there might be a Pirates of the Caribbean reboot. So he goes to fresh potatoes to check it out. When he finds the movie of “untitled Pirates of the Carribean reboot ” he clicks on  it and looks at the info icon in the top right corner and discovers that it’s status is “Rumored” 

**Acceptance tests**:

1. Given that the movie has been released, when the movie is clicked on the status of it will be displayed as ‘released’
2. Given that the movie/tv show is in post production (unreleased), when the movie is clicked on the status of it will be “Post Production”
3. Given that a tv show has aired and ended the status will be “Ended”
4. Given that a tv show/movie is in production, then the status will show “in production”
5. Given that a movie is only rumoured, then the status will show “Rumoured”

### User Stories 2

**User story**: As a client of netflix I want to see if a movie or tv show is available on that platform.

**Name**: Alexander Hamilton

**Actors**:  Netflix client

**Precondition**: none

**Postcondition**: none

**Iteration**: 2

**Scenario**: Alexander wants to see if the movie/play “Hamiltion” is on Netflix. He finds it through Fresh Potatoes, clicks on the poser, looks in the where to watch section and is disappointed to see that it is not available on Netflix. It is however, on Disney+.

**Acceptance tests**:

1. Given that the content is available to watch on netflix when I click on a movie poster to get more information then a netflix symbol will appear under the “where to watch” section.
2. Given that the content is not available on netflix, when I click on a movie poster to get more information then a netflix symbol won't appear under the “where to watch ” section

### User Stories 3

**User story**: As someone who only watches movies/tv shows with a 8.0 rating I want to check to a movie’s rating to see if it meets my standards

**Name**: Bonzu Pippinpaddleopsicopolis the Third

**Actors**: 8.0 rating movie watcher  

**Precondition**: none

**Postcondition**: none

**Iteration**: 2

**Scenario**: Bonzu wants to watch the tv series “Avatar: The Last Airbender” but needs to know what its rating is before watching it. So they find it in the website’s search ‘tv shows’ section. They click on the show’s poster and are able to see that it has a rating of 8.6.

**Acceptance tests**:

1. Given the site has the movie’s rating, when we click on a movie for more information the movie’s rating is displayed.
2. Given the site does not have the movie rating, when we click on a movie for more information the movie’s rating says “0.0”

### User Stories 4

**User story**: As a fan of Marvel movies I want to be able to search for Marvel movies to watch

**Name**: Robert Banner

**Actors**: Movie watchers who know what they want

**Precondition**: none

**Postcondition**: none

**Iteration**: 2

**Scenario**: Robert Banner is a fan of the Marvel Cinematic Universe films. He exclusively watches these films and nothing else. However, the films aren’t always trending or popular at any given moment so he needs to be able to search for them.

**Acceptance tests**:

1. Given a title when I search for it then a list of titles with similar or exact names show up
2. Given a title when I search for it I can find movie and TV show results

### User Stories 5

**User story**: As someone who doesn’t know I want to watch I want to be able to find new films

**Name**: Han Solo

**Actors**: Movie watchers who don’t know exactly what they want to watch but have an idea

**Precondition**: none

**Postcondition**: none

**Iteration**: 2

**Scenario**: Han is looking for a new film or TV show to watch but doesn’t know exactly what he’s looking for. However he has an idea of what he’s looking for, so given one or more keywords he wants to be able to find a film or TV show related to those keywords.

**Acceptance tests**:

1. Given a genre when I search for a film or TV show then I am presented with a list of films in that genre
2. Given some keyword(s) when I search for a film or TV show then I am presented with a list of films that are related to the keyword(s)

### User Stories 6

**User story**: As someone who doesn’t have time to find movies I want to have recommendations displayed for me

**Name**: Squilliam Fancyson

**Actors**: Movie watches who prefer the convenience of having movie recommendations display for them

**Precondition**: registered for a Fresh Potatoes accounts and have completed the survey

**Postcondition**: their account contains genres and movies they enjoy

**Iteration**: 2

**Scenario**: Squilliam Fancyson is an avid movie watcher who is always very busy with his work. After a long day of work he likes to relax with a movie or TV show. He prefers to have movie recommendations shown to him instead of browsing until something catches his eye.

**Acceptance tests**:

1. Given when I sign up I want to let the platform know my interests
2. Given when I log in to the website I am presented with recommendations that matches my interests



## Iteration 1

### User Stories 1

**User story**: As a New movie watcher I want to sign up to get access to a profile

**Name**: Captain Hook

**Actors**: New movie watcher

**Precondition**: none

**Postcondition**: The user’s account information will be stored in the database.

**Iteration**: 1

**Scenario**: Captain Hook goes to the Fresh Potatos website and is brought to the homepage where he can see a main featured movie. He clicks on the login button that can be found in the righthand corner of the website’s navigation bar. He is then brought to a register page where he adds his username, password, password confirmation, and email. He hits “Sign Up” and is redirected to the login page. He logs in with his new username and password and clicks on the profile button in the top right of the website. Here he is shown his email, username and can input his date of birth.

**Acceptance tests**:
1. Given that the confirmation password doesn’t match the password, when I click “sign up” the password confirmation box turns red and prompts “The two password fields didn’t match.”
2. Given the password is too similar to my personal information, when I click “sign up” red text below the fields appear “The password is too similar to the username.”
3. Given the password is too commonly used, when I click “sign up” red text below the fields appears “The password is too common.”
4. Given the password all numeric, when I click “sign up” red text below the fields appears “This password is entirely numeric”
5. Given there is a field not filled out, when I click “sign up” the field is highlighted in red and a prompt appears “Please fill out this field.”
6. Given the username is invalid, when I click  “sign up” red text below the fields appears  “Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.”
7. Given the password meets all specified criteria when I click on the “sign up” I am redirected to the login page. 

### User Stories 2

**User story**: As a regular movie watcher I want to log in to my profile to add my date of birth

**Name**: Tony Stark  

**Actors**: Regular movie watcher 

**Precondition**: already registered for a Fresh Potatoes account

**Postcondition**:  their account contains their date of birth information

**Iteration**: 1 

**Scenario**: Tony Stark goes to the Fresh Potatoes website and clicks on the “login” button located in the top right corner of the website. He is then taken to the homepage. He clicks the “profile” button located in the top right corner which takes him to his profile page. Clicking the “Complete our survey to get recommended movies!” link he enters his birthdate which is now displayed on his profile page.

**Acceptance tests**:
1. Given the correct username and password is given, when I hit “sign in” I get logged in and gain access to my profile
2. Given I do not have an account, when I hit “sign in” a red banner above the fields appears: “Please enter a correct username and password. Note that both fields may be case-sensitive.”
3. Given the incorrect password is entered, when I hit “sign in” a red banner above the fields appears: “Please enter a correct username and password. Note that both fields may be case-sensitive.”
4. Given the incorrect username is entered, when I hit “sign in” a red banner above the fields appears: “Please enter a correct username and password. Note that both fields may be case-sensitive.”

### User Stories 3

**User story**: As a movie buff I want to see what movies are popular, trending, and coming out to keep up to date.

**Name**: James Bond 

**Actors**: Movie Buff 

**Precondition**: none

**Postcondition**: none 

**Iteration**: 1

**Scenario**: James Bond wants to know what some popular, trending, and upcoming movies are. So he goes to the fresh potatoes website and scrolls down to check what movies are new, trendy and coming soon.

**Acceptance tests**:

1. When visiting Fresh Potatoes movies should be retrieved from the site’s API and displayed to me.
