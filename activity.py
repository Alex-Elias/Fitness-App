from db import db
from flask import abort, request, session
from datetime import datetime

def add(user_id, name, type, workout, time, distance, date, message):
    sql = """INSERT INTO activities (user_id, name, type_id, workout_id, time, distance, date, message, visible)
             VALUES (:user_id, :name, :type_id, :workout_id, :time, :distance, :date, :message, 1)"""
    db.session.execute(sql, {"user_id":user_id, "name":name, "type_id":type, "workout_id":workout, "time":time, "distance":distance, "date":date, "message":message})
    db.session.commit()

def getTypes():
    sql = "SELECT id, name FROM types"
    results = db.session.execute(sql)
    return results.fetchall()


def getActivities():
    user_id = session["user_id"]
    sql = """SELECT name, type_id, workout_id, time, distance, date, message FROM activities WHERE user_id=:user_id
            AND visible=1 ORDER BY date DESC
        """
    results = db.session.execute(sql, {"user_id":user_id})
    return results.fetchall()