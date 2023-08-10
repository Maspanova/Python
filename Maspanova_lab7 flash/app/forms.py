from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class UserNameForm(FlaskForm):
    userNameField = StringField("userNameField", validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    loginField = StringField("loginField", validators=[DataRequired()])
    passwordField = StringField("passwordField", validators=[DataRequired()])
    passwordFieldCheck = StringField("passwordFieldCheck", validators=[DataRequired()])
