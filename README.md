# Fitness-App

An application for the tsoha course in the University of Helsinki where the user can record their workouts, plan workouts, set goals, and save their PRs(personal records)

The application can be tested on [Heroku](https://tsoha-fitness-app.herokuapp.com/login).

## Functionality
* The user can create an account
* The user can log into an existing account
* The user can log out of their account
* The user can add and view activities in their account
* The user Can add/remove and view planned workouts in their account
* The user can remove activities from their account
* The user can add/remove goals to/from their account
* The user can add/remove their PRs to/from their account



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
