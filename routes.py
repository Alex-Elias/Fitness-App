from app import app
from flask import redirect, render_template, request, session
from os import getenv
import users
from datetime import datetime
import workout
import activity
import pr
import goals


@app.route("/")
def index():
    user_id = users.user_id()

    return render_template("index.html", workouts=workout.get_workout_today(user_id), goals=goals.get(user_id))

@app.route("/workouts")
def workouts():
    workout_list = workout.get_workouts()
    return render_template("workouts.html", workouts=workout_list)

@app.route("/removeactivity", methods=["post"])
def remove_activity():
    if request.method == "POST":
        users.check_csrf()
        activity_id = request.form["activity_id"]
        activity.remove(activity_id)
        return activities()

@app.route("/removepr", methods=["post"])
def remove_pr():
    if request.method == "POST":
        users.check_csrf()
        pr_id = request.form["pr_id"]
        pr.remove(pr_id)
        return prs()

@app.route("/removegoal", methods=["post"])
def remove_goal():
    if request.method== "POST":
        users.check_csrf()
        goal_id = request.form["goal_id"]
        goals.remove(goal_id)
        return goal()


@app.route("/addgoal", methods=["get", "post"])
def add_goal():
    if request.method == "GET":
        return render_template("addgoal.html")
    if request.method == "POST":
        users.check_csrf()
        name = request.form["name"]
        frequency = request.form["frequency"]
        message = request.form["message"]
        user_id = users.user_id()
        goals.add(user_id, name, frequency,message)
        return render_template("addgoal.html")

@app.route("/goal")
def goal():
    user_id = session["user_id"]
    goal_list = goals.get(user_id)
    return render_template("goal.html", Goals=goal_list)

@app.route("/activities")
def activities():
    activities_list = activity.get_activities()
    
    return render_template("activities.html", activities=activities_list)

@app.route("/removeworkout", methods=["post"])
def remove_workout():
    if request.method == "POST":
        users.check_csrf()
        workout_id = request.form["workout_id"]
        workout.remove(workout_id)
        return workouts()

@app.route("/prs")
def prs():
    pr_list = pr.get_prs()
    return render_template("prs.html", PRs=pr_list)

@app.route("/addpr", methods=["get", "post"])
def add_pr():
    today = datetime.now().strftime('%Y-%m-%d')
    if request.method == "GET":
        pr_list = pr.get_prs()
        return render_template("addpr.html", today = today, PRs = pr_list)
    if request.method == "POST":
        users.check_csrf()
        distance = request.form["distance"]
        type = request.form["type"]
        time_h = request.form["time-hours"]
        time_m = request.form["time-minutes"]
        time_s = request.form["time-seconds"]
        message = request.form["message"]
        date = request.form["date"]
        user_id = users.user_id()
        pr.add(user_id, distance, type, time_h, time_m, time_s, date, message)

        pr_list = pr.get_prs()
        return render_template("addpr.html", today = today, PRs = pr_list)



@app.route("/updatepr", methods=["post"])
def update_pr():
    if request.method == "POST":
        users.check_csrf()
        distance = request.form["distance"]
        type = request.form["type"]
        time_h = request.form["time-hours"]
        time_m = request.form["time-minutes"]
        time_s = request.form["time-seconds"]
        message = request.form["message"]
        date = request.form["date"]
        user_id = users.user_id()
        pr.update_pr(user_id, distance, type, time_h, time_m, time_s, date, message)
    return redirect("/addpr")
    

@app.route("/addactivity", methods=["get", "post"])
def add_activity():
    today = datetime.now().strftime('%Y-%m-%d')

    if request.method == "GET":
        return render_template("addactivity.html", today=today)
    
    if request.method == "POST":
        users.check_csrf()
        name = request.form["name"]
        type = request.form["type"]
        distance = request.form["distance"]
        time_hours = request.form["time-hours"]
        time_minutes = request.form["time-minutes"]
        time_seconds = request.form["time-seconds"]
        message = request.form["message"]
        date = request.form["date"]
        user_id = users.user_id()
        time = f"{time_hours}:{time_minutes}:{time_seconds}"
        activity.add(user_id,name,type,0,time,distance,date,message)
    
        return render_template("addactivity.html", today=today)


@app.route("/addworkout", methods=["get", "post"])
def add_workout():
    today = datetime.now().strftime('%Y-%m-%d')
    if request.method == "GET":
        return render_template("addworkout.html",today=today)
    
    if request.method == "POST":
        users.check_csrf()
        name = request.form["workoutname"]
        description = request.form["workoutdescription"]
        date = request.form["workoutdate"]

        workout.add(name,description, date)
            
        return render_template("addworkout.html", today=today)


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
            return render_template("register.html", usernameErrorMessage="The username must be no longer than 20 characters and at least one") 

        password1 = request.form["password"]
        password2 = request.form["repassword"]

        if password1 != password2:
            return render_template("register.html", passwordsDoNotMatchErrorMessage="The passwords do not match", reusername=username) 

        if password1 == "":
            return render_template("register.html", passwordLengthErrorMessage="The password must be at least one character long", reusername=username)

        if not users.register(username, password1):
            return render_template("register.html", registrationErrorMessage="Registration did not work, the username may not be available")
        return redirect("/login")


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/login")