from flask import request, Blueprint, render_template, redirect, url_for, flash
from my_app.source.models import cursor, conn
my_app = Blueprint('app', __name__)
from my_app.source.models import ReviewForm
# from flask_bootstrap import Bootstrap

#1 -------------------- Organization List Function --------------------

def organizations():
    command = """SELECT {a}.organization_id, {a}.organization_name, {a}.president, {a}.number_of_members, {b}.category_name, {a}.rating
                 FROM {a} join {b} ON {a}.category_id = {b}.category_id
        """.format(a="organization", b='category')
    cursor.execute(command)
    org_data = cursor.fetchall()

    return render_template("organization.html",org_list=org_data)

#2 -------------------- Organization Detail Function --------------------

def organization_detail(key):

    command = """ SELECT {a}.organization_name, {a}.organization_id, {a}.description, {a}.location, {a}.president,
                         {a}.membership_cost, {a}.is_payment_required, {a}.rating, {a}.number_of_members, {a}.Image_URL
                         FROM {a}
                         WHERE {a}.organization_id = {p1}
    """.format(a="organization", p1=key)

    cursor.execute(command)
    club_data3 = cursor.fetchall()
    if len(club_data3) == 0:
        return "Page Error. The key " + key + " cannot be found"
    individual_club = club_data3[0]

    command_review = """SELECT {a}.review_id, {a}.first_name, {a}.last_name,{a}.organization_name, {a}.user_review
                        FROM {a}
                        WHERE {a}.organization_id = {id}
                      """.format(a='review', id = key)
    cursor.execute(command_review)
    review_data = cursor.fetchall()

    return render_template("organization_detail.html", org_detail = individual_club, review_list = review_data, URL = url_for('organization_detail', key = key))

#3 -------------------- Organization Search Function --------------------

def organization_search():
    org_name = request.args.get('search-name')
    condition = ""

    if org_name != None:
        condition += "organization.organization_name LIKE '%"+(org_name)+"%'"

    if condition == "":
        command = """SELECT {a}.organization_id, {a}.organization_name, {a}.president, {a}.number_of_members, {b}.category_name, {a}.rating
                     FROM {a} join {b} ON {a}.category_id = {b}.category_id
                  """.format(a="organization", b='category')
    else:
        command = """SELECT {a}.organization_id, {a}.organization_name, {a}.president, {a}.number_of_members, {b}.category_name, {a}.rating
                      FROM {a} join {b} ON {a}.category_id = {b}.category_id
                      WHERE {cond}
        """.format(a="organization", b='category', cond=condition)

    cursor.execute(command)
    org_data = cursor.fetchall()
    return render_template("organization.html", org_list = org_data, URL=url_for('organization_search'))
