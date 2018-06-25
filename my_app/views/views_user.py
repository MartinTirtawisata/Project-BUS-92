from flask import request, Blueprint, render_template, redirect, url_for, flash, session
from my_app.models import cursor, conn
my_app = Blueprint('app', __name__)
from my_app.models import LoginForm, RegisterForm

# --------------- Sign Up Function ---------------
def sign_up():
    # 1) Select the table to fetch all data from the database
    command = """SELECT {a}.user_id, {a}.email, {a}.username, {a}.password
                 FROM {a}
              """.format(a='User')
    cursor.execute(command)
    user_data = cursor.fetchall()

    # 2) Select the MAX(user_id) to make the id increment. If it's None then return 1.
    command = """ SELECT MAX(user_id)
                  FROM User
              """
    cursor.execute(command)
    next_user_id = cursor.fetchone()

    if next_user_id[0] == None:
        user_id = 1
    else:
        user_id = next_user_id[0]+1

    # 3) create the form function
    form = RegisterForm(request.form, crsf_enabled=False)

    # 4) creata an IF function if method = POST and create variable for form database
    if request.method == 'POST' and form.validate():
        email = form.email.data
        username = form.username.data
        password = form.password.data

        # 5) Insert data into database (INSERT INTO ... VALUES ...)
        command = """ INSERT INTO {a} (user_id, email, username, password)
                      VALUES ({id}, '{e}','{un}', '{p}')
                  """.format(a='User', id=user_id, e=email, un=username, p=password)
        cursor.execute(command)
        conn.commit()

        return redirect(url_for('app.home'))

    #5) Create an error form
    if form.errors:
        flash(form.errors, 'danger')

    return render_template('sign_up.html', form=form)

# -------------- Login Function ----------------
def login():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate:
        email = form.email.data
        password = form.password.data

        command = """ SELECT *
                      FROM User
                      WHERE User.email = "{e}"
        """.format(e=email)
        cursor.execute(command)
        login_verified = cursor.fetchone()

        if login_verified != None:
            if email == login_verified[1] and password == login_verified[3]:
                session['logged_in'] = True
                # session['email_address'] = email_address
                # flash('Loggin in as %s!' %(email_address), 'success')
                # return '<h1> Login Successful </h1>'
                return redirect(url_for('app.home'))
            else:
                # flash('Wrong Email Address','danger')
                return render_template('login.html', form=form)
        else:
            flash('Wrong Email Address','danger')
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)

# -------------- Login Function ----------------
def logout():
    session.clear()
    return redirect(url_for('app.home'))
