from db import db
from flask import abort, request, session
from datetime import datetime

def add(name, discription, date):
    user_id = session["user_id"]
    try:
        sql = "INSERT INTO workout (user_id, workout_name, discription, workout_date) VALUES (:user_id, :workout_name, :discription, :workout_date)"
        db.session.execute(sql, {"user_id":user_id, "workout_name":name, "discription":discription, "workout_date":date})
        db.session.commit()
    except:
        return False
    return True


def getWorkouts():
    user_id = session["user_id"]
    sql = "SELECT workout_name, discription, workout_date FROM workout WHERE user_id=:user_id"
    results = db.session.execute(sql, {"user_id":user_id})
    workout = results.fetchall()
    

    return workout

def getWorkoutToday():
    date = datetime.now().strftime('%Y-%m-%d')
    user_id = session["user_id"]
    sql = "SELECT workoutname, discription FROM workout WHERE user_id=:user_id AND workoutdate:=workoutdate"
    results = db.session.execute(sql, {"user_id":user_id, "workoutdate":date})
    workout = results.fetchall()
    name = workout[0]
    discription = workout[1]

    return (name, discription)