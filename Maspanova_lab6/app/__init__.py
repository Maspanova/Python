from flask import Flask
from flask_login import LoginManager, current_user

app = Flask(__name__)
app.config.from_object("config")
from app import controller, model, repository

login_manager = LoginManager()
login_manager.add_view = "login"  # настройка, перебросит сюда, если не авторизованы
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return repository.load_user_by_id(user_id)
