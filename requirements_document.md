## Description

Fresh potatoes provides a simplified and more efficient movie searching process for any users that watches movies and TV shows at any age range. Though the recommendation option has been implemented on most of the streaming services, many users still feel lost while searching for something new to watch due to the limited content and overly complicated designs on most of the modern streaming services and databases such as Netflix and IMDb. Our project aims to solve that problem by implementing more defined and detailed recommendation options as well as filtering the movies and shows based on the streaming platforms they are on and provide a link to that platform. In this iteration our website allows the user to sign up for an account, login, logout and presents popular movies; trending movies; and upcoming movies based on their ranking. to either a logged in user or a logged-out user on our homepage. It also allows a logged in user to visit their user profile.

### User Stories 1

**User story**: As a New movie watcher I want to sign up to get access to a profile
**Name**: Captain Hook
**Actors**: New movie watcher
**Precondition**: none
**Postcondition**: The user’s account information will be stored in the database.
**Iteration**: 1
**Scenario**:

Captain Hook goes to the Fresh Potatos website and is brought to the homepage where he can see a main featured movie. He clicks on the login button that can be found in the righthand corner of the website’s navigation bar. He is then brought to a register page where he adds his username, password, password confirmation, and email. He hits “Sign Up” and is redirected to the login page. He logs in with his new username and password and clicks on the profile button in the top right of the website. Here he is shown his email, username and can input his date of birth.

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
**Scenario**: 

Tony Stark goes to the Fresh Potatoes website and clicks on the “login” button located in the top right corner of the website. He is then taken to the homepage. He clicks the “profile” button located in the top right corner which takes him to his profile page. Clicking the “Complete our survey to get recommended movies!” link he enters his birthdate which is now displayed on his profile page.

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
**Scenario**:

James Bond wants to know what some popular, trending, and upcoming movies are. So he goes to the fresh potatoes website and scrolls down to check what movies are new, trendy and coming soon.

**Acceptance tests**:

1. When visiting Fresh Potatoes movies should be retrieved from the site’s API and displayed to me.
