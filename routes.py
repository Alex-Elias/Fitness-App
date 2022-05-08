from app import app
from flask import redirect, render_template, request, session
from os import getenv
import users
from datetime import datetime
import workout
import activity
import pr


@app.route("/")
def index():
    user_id = users.user_id()

    return render_template("index.html", workouts=workout.getWorkoutToday(user_id))

@app.route("/workouts")
def workouts():
    workout_list = workout.getWorkouts()
    return render_template("workouts.html", workouts=workout_list)
@app.route("/removeactivity", methods=["post"])
def removeActivity():
    if request.method == "POST":
        users.check_csrf()
        activity_id = request.form["activity_id"]
        activity.remove(activity_id)
        return activities()

@app.route("/removepr", methods=["post"])
def removePr():
    if request.method == "POST":
        users.check_csrf()
        pr_id = request.form["pr_id"]
        pr.remove(pr_id)
        return prs()

@app.route("/activities")
def activities():
    activities_list = activity.getActivities()
    
    return render_template("activities.html", activities=activities_list)

@app.route("/removeworkout", methods=["post"])
def removeWorkout():
    if request.method == "POST":
        users.check_csrf()
        workout_id = request.form["workout_id"]
        workout.remove(workout_id)
        return workouts()

@app.route("/prs")
def prs():
    pr_list = pr.getPrs()
    return render_template("prs.html", PRs=pr_list)

@app.route("/addpr", methods=["get", "post"])
def addPr():
    today = datetime.now().strftime('%Y-%m-%d')
    if request.method == "GET":
        pr_list = pr.getPrs()
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

        pr_list = pr.getPrs()
        return render_template("addpr.html", today = today, PRs = pr_list)



@app.route("/updatepr", methods=["post"])
def updatePr():
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
        pr.updatePr(user_id, distance, type, time_h, time_m, time_s, date, message)
    return redirect("/addpr")
    

@app.route("/addactivity", methods=["get", "post"])
def addActivity():
    today = datetime.now().strftime('%Y-%m-%d')
#    types = activity.getTypes()
#    types_id = []
#    types_name = []
#    for type in types:
#        types_id.append(type[0])
#        types_name.append(str(type.name))
#    print(types_name)
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
def addWorkout():
    today = datetime.now().strftime('%Y-%m-%d')
    if request.method == "GET":
        return render_template("addworkout.html",today=today)
    
    if request.method == "POST":
        users.check_csrf()
        name = request.form["workoutname"]
        description = request.form["workoutdescription"]
        date = request.form["workoutdate"]

        if not workout.add(name,description, date):
            # TO DO 
            print("could not add workout")
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