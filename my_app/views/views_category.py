from flask import request, Blueprint, render_template, redirect, url_for, flash, URL
from my_app.source.models import cursor, conn
my_app = Blueprint('app', __name__)
from my_app.source.models import ReviewForm
# from flask_bootstrap import Bootstrap

#1 -------------------- Category Function --------------------

def category():
    command = """SELECT {b}.category_id, {b}.category_name
                FROM {b}
                """.format(b='category')

    cursor.execute(command)
    club_data = cursor.fetchall()

    return render_template("category.html", club_category = club_data, URL = url_for('category'))

#2 -------------------- Category List Function --------------------
def category_filtered():
    command = """SELECT {a}.club_id, {a}.organization_name, {a}.president, {a}.number_of_members, {b}.category, {a}.rating
                      FROM {a} join {b} ON {a}.category_id = {b}.category_id
                      WHERE {b}.category_id = {k}
        """.format(a="organizations", b='category', k=key)

    cursor.execute(command)
    club_data = cursor.fetchall()

    return render_template("organization.html", club_list = club_data, URL = url_for('category_list'))
