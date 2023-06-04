from app import app
from flask import render_template, request #обработка шаблона
from datetime import datetime
from .forms import UserNameForm #импортирую объект UserNameForm из файла forms
@app.route('/', methods=['GET'])
@app.route('/index')
def index ():
    form = UserNameForm()
    return render_template("index.html", form=form);

@app.route('/', methods=['POST']) #обработка post запроса
def index_post(): #функция для обратотки post запроса
    form = UserNameForm()
   #if form.validate_on_submit():
    text=form.userNameField.data
    text2=form.userSurnameField.data
    return render_template("index.html", form=form, user_name=text, user_surname=text2);
#else:
    #return "bad form"
