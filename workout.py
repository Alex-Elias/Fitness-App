from db import db
from flask import abort, request, session
from datetime import datetime

def add(name, description, date):
    user_id = session["user_id"]
    try:
        sql = "INSERT INTO workout (user_id, workout_name, description, workout_date, visible) VALUES (:user_id, :workout_name, :description, :workout_date, 1)"
        db.session.execute(sql, {"user_id":user_id, "workout_name":name, "description":description, "workout_date":date})
        db.session.commit()
    except:
        return False
    return True

def remove(workout_id):
    user_id = session["user_id"]
    sql="UPDATE workout SET visible=0 WHERE id=:workout_id AND user_id=:user_id"
    db.session.execute(sql, {"workout_id":workout_id, "user_id":user_id})
    db.session.commit()

def getWorkouts():
    user_id = session["user_id"]
    sql = "SELECT id, workout_name, description, workout_date FROM workout WHERE user_id=:user_id AND visible=1"
    results = db.session.execute(sql, {"user_id":user_id})
    workout = results.fetchall()
    

    return workout

def getWorkoutToday():
    date = datetime.now().strftime('%Y-%m-%d')
    user_id = session["user_id"]
    sql = "SELECT workoutname, description FROM workout WHERE user_id=:user_id AND workoutdate:=workoutdate AND visible=1"
    results = db.session.execute(sql, {"user_id":user_id, "workoutdate":date})
    workout = results.fetchall()
    name = workout[0]
    description = workout[1]

    return (name, description)