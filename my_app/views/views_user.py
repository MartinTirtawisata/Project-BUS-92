from flask import request, Blueprint, render_template, redirect, url_for, flash
from my_app.models import cursor, conn
my_app = Blueprint('app',__name__)
from my_app.models import UserForm

# --------------- Sign Up Function ---------------

def sign_up():
    # 1) Select the table to fetch all data from the database
    command = """SELECT {a}.user_id, {a}.email_address, {a}.password
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
    form = UserForm(request.form, crsf_enabled=False)

    # 4) creata an IF function if method = POST and create variable for form database
    if request.method == 'POST' and form.validate()
        email_address = form.email_address.data
        password = form.password.data

        # 5) Insert data into database (INSERT INTO ... VALUES ...)
        command = """ INSERT INTO {a} (user_id, email_address, password)
                      VALUES ({id}, '{ea}', '{p}')
                  """.format(a='User', id=user_id, ea=email_address, p=password)
        cursor.execute(command)
        conn.commit()

        return (redirect(url_for('app.home')))

    #5) Create an error form
    if form.errors:
        flash(form.errors, 'danger')

    return render_template('sign_up.html', form=form)

# -------------- Login Function ----------------

command = """SELECT {a}.review_id, {a}.first_name, {a}.last_name,{a}.organization_name, {a}.user_review
             FROM {a}
          """.format(a='review')
cursor.execute(command)
review_data = cursor.fetchall()

# This queries the review_id and make it increment
command = """ SELECT MAX(review_id)
                FROM review
          """
cursor.execute(command)
next_id = cursor.fetchone()
if next_id[0] == None:
    review_id = 1
else:
    review_id = next_id[0]+1

form = ReviewForm(request.form, crsf_enabled=False)# This variable is linked to models.py

command = """ SELECT organization_name, organization_name
              FROM organization
          """
cursor.execute(command)
org_name = cursor.fetchall()
form.org_name.choices = org_name

if request.method == 'POST' and form.validate():
    first_name = form.first_name.data
    last_name = form.last_name.data # This variable is linked to the models
    org_name = form.org_name.data
    user_review = form.user_review.data

    command = """ SELECT {a}.organization_id
                  FROM {a}
                  WHERE {a}.organization_name = '{n}'
    """.format(a='organization', n=org_name)
    cursor.execute(command)
    selected_org_id = cursor.fetchone()
    org_id = selected_org_id[0]

    command = """ INSERT INTO review (review_id, first_name, last_name, organization_name, user_review, organization_id)
                  VALUES ({i},'{f}','{l}','{n}','{r}',{o})
              """.format(i=review_id, f=first_name, l=last_name, n=org_name, r=user_review, o=org_id) #This format matches the models and if POST statement
    cursor.execute(command)
    conn.commit()
    # flash is a pop up?
    flash('Your Review has been added','success')
    # return redirect(url_for('app.insert_review'))

    return redirect(url_for('app.organization_detail', key = org_id))

if form.errors:
    flash(form.errors, 'danger')
      # This request's syntax is the router.(html file)
    # The user will be directed to this URL. The database should already be inserted and able to be viewed once redirected

return render_template('reviewpage.html', form=form, review_list=review_data)
