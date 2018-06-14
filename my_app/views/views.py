from flask import request, Blueprint, render_template, redirect, url_for, flash, URL
from my_app.source.models import cursor, conn
my_app = Blueprint('app', __name__)
from my_app.source.models import ReviewForm
# from flask_bootstrap import Bootstrap

import my_app.views.views_organization as vo
import my_app.views.views_category as vc
import my_app.views.views_review as vr


#1 -------------------- Homepage Section --------------------
# ----- base handler -----
@my_app.route('/')
def base():
    return render_template("homepage.html")

# ----- homepage handler -----
@my_app.route('/home')
def homePage():
    return render_template("homepage.html")

#2 -------------------- Organization Section --------------------
# ----- Organization List Handler -----
@my_app.route('/organizations')
def organizations():
    return (vo.organizations())

# ----- Organization Detail Handler -----
@my_app.route('/organizations/organization_detail/<key>')
def organization_detail(key):
    return (vo.organization_detail(key))

# ----- Organization Search -----
@my_app.route('/organization_search', methods = ["GET","POST"])
def organization_search():
    return (vo.organization_search())

#3 -------------------- Category Section --------------------
# ----- Category List -----
@my_app.route('/category')
def category():
    return(vc.category())

# ----- Category Filtered -----
@my_app.route('/category/<key>')
def category_filtered(key):
    return(vc.category_filtered())

#4 -------------------- Review Section --------------------
# ----- Write Review (from homepage) Handler -----
@my_app.route ('/reviews-home', methods = ['GET','POST'])
def review_home():
    return(vr.review_home())

# ----- Write Review (from detail) Handler -----
#Parameters: Key
@my_app.route ('/reviews-detail/<key>', methods = ['GET','POST'])
def review_detail(key):
    return(vr.review_detail(key))

# ----- Review Edit Handler -----
@my_app.route('/review_edit/<key>', methods = ['GET','POST'])
def review_edit(key):
    return(vr.review_edit(key))

# ----- Review Delete Handler -----
@my_app.route('/reviews/delete/<key>', methods = ['GET','POST'])
def review_delete(key):
    return(vr.review_delete(key))
