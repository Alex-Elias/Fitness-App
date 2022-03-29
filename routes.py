from app import app
from flask import redirect, render_template, request, session
from os import getenv
import users


@app.route("/")
def index():
        return render_template("index.html")


@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            return render_template("error.html", message="Incorrect username or password")
        return redirect("/")


@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 1 or len(username) > 20:
            return render_template("error.html", message="The username must be no longer than 20 characters and at least one") #TO DO

        password1 = request.form["password"]
        password2 = request.form["repassword"]

        if password1 != password2:
            return render_template("error.html", message="The passwords do not match") # TO DO

        if password1 == "":
            return render_template("error.html", message="The password must be at least one character long") # TO DO

        if not users.register(username, password1):
            return render_template("error.html", message="Registration did not work, the username may not be available") # TO DO
        return redirect("/login")
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/login")