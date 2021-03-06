
from flask import render_template, url_for, Blueprint
from my_app.models import cursor, conn
from my_app import app
my_app = Blueprint('app', __name__)

import my_app.views.views_organization as vo
import my_app.views.views_category as vc
import my_app.views.views_review as vr
import my_app.views.views_user as vu
import my_app.views.views_decorator as vd
import my_app.views.views_misc as vm


#1 -------------------- Base Section --------------------
# ----- base handler -----
@my_app.route('/')
def base():
    return render_template("homepage.html")

@my_app.route('/contact_us')
def contact_us():
    return render_template("contact_us.html")
#1 -------------------- Homepage Section --------------------
# ----- homepage handler -----
@my_app.route('/home')
def home():
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
    return(vc.category_filtered(key))

#4 -------------------- Review Section --------------------
# ----- Write Review (from homepage) Handler -----
@my_app.route ('/reviews-home', methods = ['GET','POST'])
@vd.login_required
def review_home():
    return(vr.review_home())

# ----- Write Review (from detail) Handler -----
#Parameters: Key
@my_app.route ('/reviews-detail/<key>', methods = ['GET','POST'])
@vd.login_required
def review_detail(key):
    return(vr.review_detail(key))

# ----- Review Edit Handler -----
@my_app.route('/review_edit/<key>', methods = ['GET','POST'])
@vd.login_required
def review_edit(key):
    return(vr.review_edit(key))

# ----- Review Delete Handler -----
@my_app.route('/reviews/delete/<key>', methods = ['GET','POST'])
@vd.login_required
def review_delete(key):
    return(vr.review_delete(key))

#5 -------------------- Sign Up Section --------------------
@my_app.route('/sign_up', methods = ['GET','POST'])
@vd.logout_required
def sign_up():
    return(vu.sign_up())

#6 -------------------- Login Section --------------------
@my_app.route('/login', methods=['GET','POST'])
@vd.logout_required
def login():
    return(vu.login())

#6 -------------------- Logout Section --------------------
@my_app.route('/logout', methods=['GET','POST'])
@vd.login_required
def logout():
    return(vu.logout())

#7 ------------------- Checkout Form --------------------
@my_app.route('/checkout', methods=['GET','POST'])
def checkout():
    return(vm.checkout())
 #8 ----------------- Profile Page --------------------
@my_app.route('/profile_page', methods=['GET','POST'])
def profile_page():
    return(vu.profile_page())

@my_app.route('/organization/cms', methods=['GET','POST'])
def club_cms():
    return(vu.club_cms())
