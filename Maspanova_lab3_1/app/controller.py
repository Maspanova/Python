from app import app
from flask import render_template, request #обработка шаблона
from datetime import datetime
@app.route('/', methods=['GET'])
@app.route('/index')
def index ():
    now=datetime.now()
    cur_time=now.strftime('сегодня %D : %T')
    string = '''
    <html>
    <head>
    <title>Maspanova</title>
    </head>
    <body>
    <h1>Вы зашли на сайт дата, время:</h1> 
    ''' + cur_time + '''
    </body>
    </html>
    '''
    return render_template("index.html", time=cur_time)#вызов функции с шаблоном и переменымы

@app.route('/', methods=['POST']) #обработка post запроса
def index_post(): #функция для обратотки post запроса
    user_name=request.form['user_name']
    user_surname=request.form['user_surname']
    return render_template("index.html", user_name=user_name, user_surname=user_surname);
