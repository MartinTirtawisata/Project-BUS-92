from flask import request, Blueprint, render_template, redirect, url_for, flash
from my_app.models import cursor, conn
my_app = Blueprint('app', __name__)
from my_app.models import ReviewForm
# from flask_bootstrap import Bootstrap

# -------------------- Review Page (from home) Function --------------------

def review_home():
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

    if form.errors:
        flash(form.errors, 'danger')
          # This request's syntax is the router.(html file)
        # The user will be directed to this URL. The database should already be inserted and able to be viewed once redirected

    return render_template('reviewpage.html', form=form, review_list=review_data)

# -------------------- Review Page (from detail) Function --------------------

def review_detail(key):
    command = """SELECT {a}.review_id, {a}.first_name, {a}.last_name,{a}.organization_name, {a}.user_review
                 FROM {a}
              """.format(a='review')
    cursor.execute(command)
    review_data = cursor.fetchall()

    # This queries the review_id and make it autoincrement
    command = """ SELECT MAX(review_id)
                    FROM review
              """
    cursor.execute(command)
    next_id = cursor.fetchone()
    if next_id[0] == None:
        review_id = 1
    else:
        review_id = next_id[0]+1

    command = """ SELECT {a}.organization_id
                  FROM {a}
                  WHERE {a}.organization_id = {id}
    """.format(a='organization', id = key )
    cursor.execute(command)
    selected_org_id = cursor.fetchone()

    form = ReviewForm(request.form, crsf_enabled=False)# This variable is linked to models.py

    command = """ SELECT organization_name, organization_name
                  FROM organization
                  WHERE {a}.organization_id = {id}
              """.format(a='organization', id = key)
    cursor.execute(command)
    org_name = cursor.fetchall()
    form.org_name.choices = org_name

    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data # This variable is linked to the models
        org_name = form.org_name.data
        user_review = form.user_review.data
        org_id = selected_org_id[0]

        command = """ INSERT INTO review (review_id, first_name, last_name, organization_name, user_review, organization_id)
                      VALUES ({i},'{f}','{l}','{n}','{r}',{o})
                  """.format(i=review_id, f=first_name, l=last_name, n=org_name, r=user_review, o=org_id) #This format matches the models and if POST statement
        cursor.execute(command)
        conn.commit()
        # flash is a pop up?
        flash('Your Review has been added','success')
        return redirect(url_for('app.organization_detail', key = org_id))

    if form.errors:
        flash(form.errors, 'danger')
          # This request's syntax is the router.(html file)
        # The user will be directed to this URL. The database should already be inserted and able to be viewed once redirected

    return render_template('reviewpage.html', form=form, review_list=review_data)

# -------------------- Review Edit Function --------------------

def review_edit(key):
    command = """ SELECT *
                  FROM review
                  WHERE review_id = {p1}
              """.format(p1=key)
    cursor.execute(command)
    single_review = cursor.fetchall()[0]
    org_id = single_review[5]

    form = ReviewForm(request.form, csrf_enabled=False, first_name=single_review[1], last_name=single_review[2],
                       organization_name=single_review[3], user_review=single_review[4])

    command = """ SELECT {a}.organization_name, {a}.organization_name
                  FROM {a} INNER JOIN {b} ON {a}.organization_id = {b}.organization_id
                  WHERE {b}.review_id = {id}
              """.format(a='organization',b='review', id = key)
    cursor.execute(command)
    org_name = cursor.fetchall()
    form.org_name.choices = org_name

    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data # This variable is linked to the models
        org_name = form.org_name.data
        user_review = form.user_review.data # This command only works when if request.method == POST

        command = """
            UPDATE review SET first_name='{f}', last_name='{l}',organization_name='{o}',user_review='{u}'
            WHERE review_id ={i}
            """.format(f=first_name, l=last_name, o=org_name, u=user_review, i=key)
        cursor.execute(command)
        conn.commit()

        flash('Your Review has been edited', 'success')
        return redirect(url_for('app.organization_detail', key = org_id))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('review-edit.html',form=form, review_id=key)

# -------------------- Review Delete --------------------
def review_delete(key):

    command = """ SELECT organization_id
                  FROM review
                  WHERE review_id = {id}
              """.format(id = key)
    cursor.execute(command)
    selected_org_id = cursor.fetchone()
    org_id = selected_org_id[0]

    command = """ SELECT *
                  FROM review
                  WHERE review_id = {id}
              """.format(id=key)
    cursor.execute(command)

    command = """ DELETE FROM review
                    WHERE review_id = {id}
            """.format(id=key)
    cursor.execute(command)
    conn.commit()



    flash('Your Review has been deleted')
    return redirect(url_for('app.organization_detail', key = org_id))
