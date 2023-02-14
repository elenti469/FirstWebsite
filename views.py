from flask import Blueprint, render_template, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name = "Wolrd")

#/views/profile/YourNameHere
@views.route("/profile/<username>") 
def profile(username):
    return render_template("index.html", name = username)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))