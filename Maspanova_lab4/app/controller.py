from app import app
from flask import render_template, request  # обработка шаблона
from datetime import datetime
from .forms import UserNameForm  # импортирую объект UserNameForm из файла forms


@app.route("/", methods=["GET"])
@app.route("/index")
def index():
    form = UserNameForm()
    return render_template("index.html", form=form)


@app.route("/tour")
def tour():
    return render_template("tour.html")


@app.route("/map")
def map():
    return render_template("map.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/", methods=["POST"])  # обработка post запроса
@app.route("/index", methods=["POST"])
def index_post():  # функция для обратотки post запроса
    form = UserNameForm()
    text = form.userNameField.data
    text2 = form.userSurnameField.data
    return render_template("index.html", form=form, user_name=text, user_surname=text2)
