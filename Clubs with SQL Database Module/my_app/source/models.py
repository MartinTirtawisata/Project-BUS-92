from wtforms import Form, TextField
from wtforms.validators import InputRequired

import sqlite3
sqlite_file = 'SJSU_Organizations.sqlite'

conn = sqlite3.connect(sqlite_file)
cursor = conn.cursor()


class ReviewForm(Form): #This is used in views.py
    first_name = TextField(
            label="First Name",
            validators=[InputRequired()])
    last_name = TextField(
        label="Last Name",
        validators=[InputRequired()])
    org_name = TextField(
        label="Organization Name",
        validators=[InputRequired()])
    user_review = TextField(
            label='User Review',
            validators=[InputRequired()])