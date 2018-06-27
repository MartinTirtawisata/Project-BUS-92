from wtforms.fields.html5 import EmailField
from wtforms import Form, TextField, SelectField, PasswordField
from wtforms.validators import InputRequired, Email


import sqlite3
sqlite_file = "/home/martintirtawisata/sjsu-club-directory/SJSU_Organizations.sqlite"

conn = sqlite3.connect(sqlite_file)
cursor = conn.cursor()


class ReviewForm(Form): #This is used in views.py
    first_name = TextField(
        label="First Name",
        validators=[InputRequired()])
    last_name = TextField(
        label="Last Name",
        validators=[InputRequired()])
    org_name = SelectField(
        label="Organization Name",
        validators=[InputRequired()])
    user_review = TextField(
        label='User Review',
        validators=[InputRequired()])

class LoginForm(Form):
    email = EmailField(
        label='Email',
        validators=[InputRequired(), Email(message="Must be a valid email")])
    password = PasswordField(
        label='Password',
        validators=[InputRequired()])

class RegisterForm(Form):
    email = EmailField(
        label='Email',
        validators=[InputRequired(), Email(message="Must be a valid email")])
    username = TextField(
        label='Username',
        validators=[InputRequired()])
    password = PasswordField(
        label='Password',
        validators=[InputRequired()])
