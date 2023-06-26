from app import app, model
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
    # ввод данных из modell.py
    Client1 = model.Clients()
    Client1.IdClient = "1"
    Client1.Surname = "Иванов"
    Client1.Name = "Иван"
    Client1.DateOfBirth = "1978-01-01"
    Client1.PhoneNumber = "+375296111111"
    Client1.Email = "Ivanov@mail.ru"

    Client2 = model.Clients()
    Client2.IdClient = "2"
    Client2.Surname = "Петров"
    Client2.Name = "Петор"
    Client2.DateOfBirth = "1988-02-02"
    Client2.PhoneNumber = "+375296111112"
    Client2.Email = "Petrov@mail.ru"

    Client3 = model.Clients()
    Client3.IdClient = "3"
    Client3.Surname = "Сидоров"
    Client3.Name = "Сергей"
    Client3.DateOfBirth = "1998-03-31"
    Client3.PhoneNumber = "+375296111113"
    Client3.Email = "Sidorov@mail.ru"
    Clients = [Client1, Client2, Client3]  # создаем список

    return render_template(
        "index.html", form=form, user_name=text, user_surname=text2, Clients=Clients
    )
