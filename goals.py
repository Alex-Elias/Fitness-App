from db import db
from flask import session


def add(user_id, name, frequency, message):
    sql = """INSERT INTO goals (user_id, name, frequency, message, visible) VALUES 
            (:user_id, :name, :frequency, :message, 1)"""
    db.session.execute(sql,{"user_id":user_id, "name":name, "frequency":frequency, "message":message})
    db.session.commit()

def get(user_id):
    
    sql = """SELECT id, name, frequency, message FROM goals WHERE user_id=:user_id AND visible=1"""

    results = db.session.execute(sql, {"user_id":user_id})
    return results.fetchall()

def remove(goal_id):
    user_id = session["user_id"]
    sql = """UPDATE goals SET visible=0 WHERE id=:goal_id AND user_id=:user_id"""
    db.session.execute(sql, {"goal_id":goal_id, "user_id":user_id})
    db.session.commit()
