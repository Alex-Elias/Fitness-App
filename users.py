from werkzeug.security import check_password_hash, generate_password_hash
from db import db
from flask import abort, request, session
import os


def login(username, password):
    sql = "SELECT password, id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    if not check_password_hash(user[0], password):
        return False
    session["user_id"] = user[1]
    session["username"] = username
    session["csrf_token"] = os.urandom(16).hex()
    return True

def register(username, password):
    hashed_password = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        db.session.execute(sql, {"username":username, "password":hashed_password})
        db.session.commit()
    except:
        return False
    return True

def logout():
    del session["user_id"]
    del session["username"]