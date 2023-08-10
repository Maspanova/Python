from app import app, model, repository
from flask import render_template, request  # обработка шаблона
from datetime import datetime
from .forms import UserNameForm  # импортирую объект UserNameForm из файла forms


@app.route("/", methods=["GET"])
@app.route("/index")
def index():
    form = UserNameForm()
    formDelete = UserNameForm()
    roles = repository.getRoles()
    return render_template("index.html", form=form, roles=roles, formDelete=formDelete)


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
    if form.validate_on_submit():
        text = form.userNameField.data

        repository.saveRole(text)
        roles = repository.getRoles()
        return render_template("index.html", form=form, user_name=text, roles=roles)
    else:
        return "Bad request"


@app.route("/delet_role", methods=["POST"])
def delete_role():
    delete_id = request.args.get("delete_id")
    repository.deleteRole(delete_id)
    form = UserNameForm()
    roles = repository.getRoles()
    return render_template("index.html", form=form, roles=roles)


@app.route("/user")
def userInfo():
    return "User"
