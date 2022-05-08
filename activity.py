from db import db
from flask import session


def add(user_id, name, type, workout, time, distance, date, message):
    sql = """INSERT INTO activities (user_id, name, type_id, workout_id, time, distance, date, message, visible)
             VALUES (:user_id, :name, :type_id, :workout_id, :time, :distance, :date, :message, 1)"""
    db.session.execute(sql, {"user_id":user_id, "name":name, "type_id":type, "workout_id":workout, "time":time, "distance":distance, "date":date, "message":message})
    db.session.commit()

def get_types():
    sql = "SELECT id, name FROM types"
    results = db.session.execute(sql)
    return results.fetchall()

def remove(activity_id):
    user_id = session["user_id"]
    sql="UPDATE activities SET visible=0 WHERE id=:activity_id AND user_id=:user_id"
    db.session.execute(sql, {"activity_id":activity_id, "user_id":user_id})
    db.session.commit()


def get_activities():
    user_id = session["user_id"]
    sql = """SELECT name, type_id, workout_id, time, distance, date, message FROM activities WHERE user_id=:user_id
            AND visible=1 ORDER BY date DESC
        """
    sql = """SELECT a.id, a.name, t.name, a.workout_id, a.time, a.distance, a.date, a.message FROM activities a, types t
            WHERE t.id=a.type_id AND a.user_id=:user_id AND a.visible=1 ORDER BY a.date DESC"""
    results = db.session.execute(sql, {"user_id":user_id})
    return results.fetchall()