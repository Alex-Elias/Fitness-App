# Fitness-App

An application for the tsoha course in the University of Helsinki where the user can record their workouts, plan workouts, set goals, and save their PRs(personal records)

The application can be tested on [Heroku](https://tsoha-fitness-app.herokuapp.com/login).

## Implemented
* The user can create an account
* The user can log into an existing account
* The user can log out of their account
* The user can add and view activities in their account
*  The user Can add/remove and view planned workouts in their account
## TODO
* The user can remove activities from their account
* The user can add/remove goals to/from their account
* The user can add/remove their PRs to/from their account
* The user can view their daily/weekly/monthly stats
* The user can view their progress towards their goals
* The user can view their workouts
* Add comments to the code
* Make the pages look beautiful
* Let the user delete their account

My original idea for this project was to create an application where you could save all different types of workouts but after working on it a bit, I realized that it will be too extensive to finish during this class. So, I am just going to concentrate on exercises that are more enduranced focused so that I can use a basic template that saves only the distance and duration of the workout. The layout of the application is quite messy right now, I will need to spend some more time creating actuall classes in main.css and formating all of the text.

### Useful commands to run the application locally on flask

First create the virtual environment

>python3 -m venv venv 

Activate venv by typing the command

> source venv/bin/activate

Install the dependences

> pip install -r < requirements.txt

Create the tables

> psql < schema.sql

Run Flask

> flask run
