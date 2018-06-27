from functools import wraps
from flask import request, Blueprint, render_template, redirect, url_for, flash, session
from my_app.models import cursor, conn

#---------- Login Wrapper ----------
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first", 'danger')
            return redirect(url_for('app.login'))
    return wrap

#---------- Logout Wrapper ----------
def logout_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' not in session:
            return f(*args, **kwargs)
        else:
            flash("You are already logged in", 'danger')
            return redirect(url_for('app.home'))
    return wrap
