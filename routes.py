from app import app
from flask import redirect, render_template, request, session
from os import getenv
import users
from datetime import datetime
import workout


@app.route("/")
def index():
        return render_template("index.html")

@app.route("/workouts")
def workouts():
    workout_list = workout.getWorkouts()
    return render_template("workouts.html", workouts=workout_list)


@app.route("/addworkout", methods=["get", "post"])
def addWorkout():
    today = datetime.now().strftime('%Y-%m-%d')
    if request.method == "GET":
        return render_template("addworkout.html",today=today)
    
    if request.method == "POST":

        name = request.form["workoutname"]
        discription = request.form["workoutdiscription"]
        date = request.form["workoutdate"]

        if not workout.add(name,discription, date):
            # TO DO 
            print("could not add workout")
        return render_template("addworkout.html")


@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        

        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            return render_template("login.html", passwordErrorMessage="Incorrect username or password", reusername=username)
        return redirect("/")


@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    if request.method == "POST":
        

        username = request.form["username"]
        if len(username) < 1 or len(username) > 20:
            return render_template("register.html", usernameErrorMessage="The username must be no longer than 20 characters and at least one") #TO DO

        password1 = request.form["password"]
        password2 = request.form["repassword"]

        if password1 != password2:
            return render_template("register.html", passwordsDoNotMatchErrorMessage="The passwords do not match", reusername=username) # TO DO

        if password1 == "":
            return render_template("register.html", passwordLengthErrorMessage="The password must be at least one character long", reusername=username) # TO DO

        if not users.register(username, password1):
            return render_template("register.html", registrationErrorMessage="Registration did not work, the username may not be available") # TO DO
        return redirect("/login")


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/login")