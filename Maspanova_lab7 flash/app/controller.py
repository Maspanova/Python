from app import app, model, repository
from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
)  # обработка шаблона
from datetime import datetime
from .forms import (
    UserNameForm,
    RegistrationForm,
)  # импортирую объект UserNameForm из файла forms


@app.route("/registration", methods=["GET"])  # получаем страничку
def registration():
    form = RegistrationForm()
    return render_template("registration.html", form=form)


@app.route("/registration", methods=["POST"])  # отправка данных, добавление
def registration_post():
    form = RegistrationForm()
    if form.validate_on_submit():
        registration = model.Registration(
            login=form.loginField.data,
            password=form.passwordField.data,
            checkPassword=form.passwordFieldCheck.data,
        )
        if repository.checkLogin(registration.login):
            if registration.password == registration.checkPassword:
                repository.saveRegistration(registration)
                flash(
                    "Регистрация прошла успешно. Позравляю Вас пользователь  "
                    + registration.login
                )
                return redirect(url_for("index"))
            else:
                flash("Повторите пароль еще раз, вы где-то ошиблись :( ")
                return redirect(url_for("registration"))
        else:
            flash("Такой логин уже есть, попробуйте войти или введите другой логин ")
            return redirect(url_for("registration"))
    return render_template("registration.html", form=form)


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
