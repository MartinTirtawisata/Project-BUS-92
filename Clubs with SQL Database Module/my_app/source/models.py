from wtforms import Form, TextField, DecimalField, SelectField
from wtforms.validators import InputRequired, NumberRange
from decimal import Decimal

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

    user_review = TextField(
            label='User Review',
            validators=[InputRequired()])
