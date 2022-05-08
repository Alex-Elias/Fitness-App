from db import db
from flask import abort, request, session
from datetime import datetime

def add(user_id, distance, type, time_h, time_m, time_s, date, message):
    sql = """INSERT INTO prs (user_id, distance, type_id, time_h, time_m, time_s, date, message, visible)
            VALUES (:user_id, :distance, :type_id, :time_h, :time_m, :time_s, :date, :message, 1)"""
    db.session.execute(sql, {"user_id":user_id, "distance":distance, "type_id":type, "time_h":time_h,
                             "time_m":time_m, "time_s":time_s, "date":date, "message":message })
    db.session.commit()

def getPrs():
    user_id = session["user_id"]
    sql = """SELECT p.id, p.distance, t.name, p.time_h, p.time_m, p.time_s, p.date, p.message FROM prs p, types t
            WHERE t.id=p.type_id AND p.user_id=:user_id AND p.visible=1 ORDER BY p.type_id"""
    results = db.session.execute(sql, {"user_id":user_id})
    return results.fetchall()

def updatePr(user_id, distance, type, time_h, time_m, time_s, date, message):
    sql = """SELECT id FROM types WHERE name=:name"""
    type_id = db.session.execute(sql, {"name":type}).fetchone()[0]
    sql = """UPDATE prs SET time_h=:time_h, time_m=:time_m, time_s=:time_s, date=:date, message=:message
            WHERE user_id=:user_id AND distance=:distance AND type_id=:type_id"""
    db.session.execute(sql, {"time_h":time_h, "time_m":time_m, "time_s":time_s, "date":date, "message":message,
                            "user_id":user_id, "distance":distance, "type_id":type_id})
    db.session.commit()

def remove(pr_id):
    user_id = session["user_id"]
    sql="UPDATE prs SET visible=0 WHERE id=:pr_id AND user_id=:user_id"
    db.session.execute(sql, {"pr_id":pr_id, "user_id":user_id})
    db.session.commit()
