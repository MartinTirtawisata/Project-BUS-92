from flask import request, Blueprint, render_template, redirect, url_for, flash
from my_app.models import cursor, conn
my_app = Blueprint('app', __name__)


def checkout():
    return render_template('checkout_form.html')
