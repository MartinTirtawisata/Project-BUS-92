from flask import request, Blueprint, render_template, redirect, url_for, flash
from my_app.source.models import cursor, conn

my_app = Blueprint('app', __name__)

from my_app.source.models import ReviewForm


#-------------Function for printing all Organizations (Main Table)---------

def print_maintable(SJSU_Organizations):
    CLUB_ID = 0
    ORGANIZATION_NAME = 1
    PRESIDENT = 2
    NUMBER_OF_MEMBERS = 3
    CATEGORY = 4
    RATING = 5


    footer = """
    </table></body>
    """
    message_out = ''

    key = 0
    for item in SJSU_Organizations:
        message_out += '<tr>'+\
                       '<td align="center">'+str(item[CLUB_ID])+'</td>'+ \
                       '<td align="center">''<a class="two" href="http://127.0.0.1:5000/show/' + str(item[CLUB_ID]) + '">' + str(item[ORGANIZATION_NAME]) + '</a></td>' + \
                       '<td align="center">'+str(item[PRESIDENT])+'</td>'+\
                       '<td align="middle">'+str(item[NUMBER_OF_MEMBERS])+'</td>'+\
                       '<td align="middle">'+str(item[CATEGORY])+'</td>'+\
                       '<td align="middle">'+str(item[RATING])+'</td>'+'</tr>'

        key += 1
    
    return (render_template("main_table.html")+message_out+footer)



#----------Function to change boolean to yes or no in sub-table---------

def yesORno(boolean):
    if (boolean == "TRUE"):
        return "Yes"
    elif (boolean == "FALSE"):
        return "No"
    

#----------Funciton to print sub-table ------------------------------

def print_subtable(SJSU_Organizations):
    CLUB_ID = 0
    ORGANIZATION_NAME = 1
    NUMBER_OF_MEMBERS = 2
    NUMBER_OF_REVIEWS = 3
    PAYMENT_REQUIRED = 4
    MEMBERSHIP_COST = 5

    

    footer = """
    </table></body>
    """
    message_out = ''

    key = 0
    for item in SJSU_Organizations:
        message_out += '<tr>' + \
                       '<td align="center">' + str(item[CLUB_ID]) + '</td>' + \
                       '<td align="center">''<a class="two" href="http://127.0.0.1:5000/show/' + str(item[CLUB_ID]) + '">' + str(item[ORGANIZATION_NAME]) + '</a></td>' + \
                       '<td align="center">' + str(item[NUMBER_OF_MEMBERS]) + '</td>' + \
                       '<td align="middle">' + str(item[NUMBER_OF_REVIEWS]) + '</td>' + \
                       '<td align="middle">' + yesORno(str(item[PAYMENT_REQUIRED])) + '</td>' + \
                       '<td align="middle">' + str(item[MEMBERSHIP_COST]) + '</td>' + '</tr>'

        key += 1
        

    return (render_template("sub_table.html") + message_out + footer)


#---------------------- Function to print categories table  -------------------

def print_categories(Cat_Data):
    CAT_ID = 0
    CATEGORY = 1
    
    footer = """
    </table></body>
    """
    message_out = ''
    
    for item in Cat_Data:
        message_out += '<tr>' + \
                        '<td align="center">' + str(item[CAT_ID]) + '</td>' + \
                        '<td align="center">''<a class="three" href="http://127.0.0.1:5000/category/' + str(item[CAT_ID]) + '">' + str(item[CATEGORY]) + '</a></td>' + '</tr>'
    
    return (render_template("categories.html") + message_out + footer)


#-------------------- Home Page Handler --------------------

@my_app.route('/')
@my_app.route('/home')
def homePage():
    return render_template("Homepage.html")

#-------------------- Show All Handler --------------------

@my_app.route('/showall')

def organizations():
    command = """SELECT {a}.club_id, {a}.organization_name, {a}.president, {a}.number_of_members, {b}.category, {a}.rating
                      FROM {a} join {b} ON {a}.category_id = {b}.category_id
        """.format(a="organizations", b='category')
    cursor.execute(command)
    club_data = cursor.fetchall()

    return (print_maintable(club_data))
 
#-------------------- Further Details Handler --------------------

@my_app.route('/details')

def details():
    command = """SELECT {c}.club_id, {a}.organization_name, {c}.location, {c}.number_of_reviews, {c}.payment_required, {c}.membership_cost
                          FROM {c} join {a} ON {c}.club_id = {a}.club_id
            """.format(a="organizations", c='details')
    cursor.execute(command)
    club_data2 = cursor.fetchall()

    return (print_subtable(club_data2))




#-------------------- Show Key Handler --------------------

#Parameters: Key, integer
@my_app.route('/show/<key>') #Ways to control the parameter

def get_message(key):    
    ORGANIZATION_NAME = 0
    CLUB_ID = 1
    DESCRIPTION = 2
    LOCATION = 3
    PRESIDENT = 4
    MEMBERSHIP_COST = 5
    PAYMENT_REQUIRED = 6
    RATING = 7
    NUMBER_OF_MEMBERS = 8
    URL = 9
    
    
    command = """ SELECT {a}.Organization_name, {a}.club_id, {a}.description, {c}.Location, {a}.President, 
                         {c}.membership_cost, {c}.payment_required, {a}.rating, {a}.number_of_members, {c}.Image_URL
                         FROM {a} join {c} ON {a}.club_id = {c}.club_id
    """.format(a="Organizations", c='details')
    
    cursor.execute(command)
    club_data3 = cursor.fetchall()                           
    club = club_data3

    index = int(key)

    if (len(club) == 0 or key == "0"):
        return "The key "+ key + " was not found"
    if index > 160:
        return "The key "+ key + " was not found"

        
  
    
    total = int(key)
    INDEX = (total - 1)
    
    
    message = '<table><col width="315">'
    message += '<td><img src="'+str(club[INDEX][URL])+'"style="width:280px;height:320px" id="logo2"></td>'
    message += '<td><p class="right"><b>Organization Name: </b>'+str(club[INDEX][ORGANIZATION_NAME])+'</p>'
    message += '<p class="right"><b>ID: </b>'+str(club[INDEX][CLUB_ID])+'</p>'
    message += '<p class="right"><b>Description: </b>'+str(club[INDEX][DESCRIPTION])+'</p>'
    message += '<p class="right"><b>Location: </b>   '+str(club[INDEX][LOCATION])+ '</p>'
    message += '<p class="right"><b>President: </b>   '+str(club[INDEX][PRESIDENT])+'</p>'
    message += '<p class="right"><b>Membership Fee: </b>   $'+str(club[INDEX][MEMBERSHIP_COST])+ '</p>'
    message += '<p class="right"><b>Fee required to join? </b>   '+yesORno(club[INDEX][PAYMENT_REQUIRED])+ '</p>'
    message += '<p class="right"><b>Rating: </b>   '+str(club[INDEX][RATING])+'</p>'
    message += '<p class="right"><b>Number Of Members: </b>   '+str(club[INDEX][NUMBER_OF_MEMBERS])+'</p></td>'
    
    footer3 = """ </table> </body> """
                                                        
    return (render_template("show_one.html")+message+footer3)



# --------------- Category Handler ------------------#

@my_app.route('/category')
def show_categories():
    command = """SELECT {b}.category_id, {b}.category
                FROM {b}
                """.format(b='category')

    cursor.execute(command)
    club_data = cursor.fetchall()

    return print_categories(club_data)


#------------------ Individual Category Pages Handler ----------------

@my_app.route('/category/<key>')

def one_category(key):
    
    command = """SELECT {a}.club_id, {a}.organization_name, {a}.president, {a}.number_of_members, {b}.category, {a}.rating
                      FROM {a} join {b} ON {a}.category_id = {b}.category_id
                      WHERE {b}.category_id = {k}
        """.format(a="organizations", b='category', k=key)
        
    cursor.execute(command)
    club_data = cursor.fetchall()

    return (print_maintable(club_data))
    
    


#------------------ Club Search ----------------
@my_app.route('/club-search')
def club_search ():
    club_ID = request.args.get('club_id')
    club_ID_greater_equal = request.args.get('club_ge')
    club_ID_smaller_equal = request.args.get('club_se')
    orgName = request.args.get('org_name')
    president = request.args.get('president')
    category = request.args.get('category')
    rating = request.args.get('rating')
    rating_greater_equal = request.args.get('rating_ge')
    rating_smaller_equal = request.args.get('rating_se')
    
    validation = ""
    
    if club_ID != None:
        validation += "organizations.club_id = "+str(club_ID)
        
    if club_ID_greater_equal != None:
        if validation != "":
            validation += " AND "
        validation  += "organizations.club_id >= " + str(club_ID_greater_equal)
        
    if club_ID_smaller_equal != None:
        if validation != "":
            validation += " AND "
        validation  += "organizations.club_id <= " + str(club_ID_smaller_equal)
        
    if orgName != None:
        if validation != "":
            validation += " AND " 
        validation += "organizations.organization_name LIKE '%"+orgName+"%'"
        
    if president != None:
        if validation != "":
            validation += " AND "
        validation += "organizations.president LIKE '%"+president+"%'"
        
    if category != None:
        if validation != "":
            validation += " AND "
        validation += "category.category LIKE '%"+category+"%'"  
        
    if rating != None:
        if validation !="":
            validation += " AND "
        validation += "organizations.rating= "+ str(rating)
        
    if rating_greater_equal != None:
        if validation != "":
            validation += " AND "
        validation  += "organizations.rating >= " + str(rating_greater_equal)
        
    if rating_smaller_equal != None:
        if validation != "":
            validation += " AND "
        validation  += "organizations.rating <= " + str(rating_smaller_equal)
        
    if validation == "":
        command = """SELECT {a}.Club_id, {a}.Organization_name, {a}.President, {a}.number_of_members, {b}.Category, {a}.Rating
                      FROM {a} join {b} ON {a}.category_id = {b}.category_id
        """.format(a="organizations", b='category')
    else:
        command = """SELECT {a}.Club_id, {a}.Organization_name, {a}.President, {a}.number_of_members, {b}.Category, {a}.Rating
                      FROM {a} join {b} ON {a}.category_id = {b}.category_id 
                      WHERE {val}
        """.format(a="organizations", b='category', val=validation)
    
    cursor.execute(command)
    club_data = cursor.fetchall()
    return (print_maintable(club_data))


        



#--------------------Insert Review Handler---------------

#Parameters: Key
@my_app.route ('/reviews', methods = ['GET','POST'])

def insert_review():
    command = """SELECT {a}.id, {a}.first_name, {a}.last_name,{a}.organization_name, {a}.user_review
                              FROM {a} 
                      """.format(a='reviews')
    cursor.execute(command)
    review_data = cursor.fetchall()


    command = """ SELECT MAX(id)
                    FROM reviews
            """
    cursor.execute(command)
    next_id = cursor.fetchone()
    review_id = next_id[0]+1


    form = ReviewForm(request.form, crsf_enabled=False)# This variable is linked to models.py

    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data # This variable is linked to the models
        org_name = form.org_name.data
        user_review = form.user_review.data


        # This command only works when if request.method == POST
        command = """  
            INSERT INTO reviews         
             (id,first_name, last_name,organization_name, user_review) VALUES 
            ({i},'{f}','{l}','{o}','{r}')
            """.format(i=review_id,f=first_name,l=last_name,o=org_name, r=user_review) #This format matches the models and if POST statement

        cursor.execute(command)
        conn.commit()
        # flash is a pop up?
        flash('Your Review has been created')
        return redirect(url_for('app.insert_review'))  # This request's syntax is the router.(html file)
        # The user will be directed to this URL. The database should already be inserted and able to be viewed once redirected



    return render_template('ReviewPage.html', form=form, review_list=review_data)


#---------------- Individual Edit Key Handler --------------#
@my_app.route('/edit/<key>')
def edit(key):
    command = """SELECT {a}.id, {a}.first_name, {a}.last_name, {a}.organization_name, {a}.user_review
                      FROM {a} 
                      WHERE {a}.id = {p1}
        """.format(a="reviews", p1=key)
    cursor.execute(command)
    edit_data = cursor.fetchall()

    if len(edit_data) == 0:
        return "The key " + key + " was not found"
    edit = edit_data[0]

    return render_template('edit.html', one_edit=edit)


#---------------- Edit Review Handler----------------#
@my_app.route('/review_edit/<key>', methods = ['GET','POST'])
def review_edit(key):
    command = """ SELECT *
                    FROM reviews   
                    WHERE id = {p1}
            """.format(p1=key)
    cursor.execute(command)
    single_review = cursor.fetchall()[0]

    form = ReviewForm(request.form, csrf_enabled=False, first_name=single_review[1], last_name=single_review[2],
                       organization_name=single_review[3], user_review=single_review[4])

    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data # This variable is linked to the models
        org_name = form.org_name.data
        user_review = form.user_review.data # This command only works when if request.method == POST

        command = """  
            UPDATE reviews SET first_name='{f}', last_name='{l}',organization_name='{o}',user_review='{u}'
            WHERE id ={i}
            """.format(f=first_name,l=last_name,o=org_name,u=user_review, i=key)
        cursor.execute(command)
        conn.commit()
        flash('Your review has been edited')
        return redirect(url_for('app.insert_review', key=key))

    if form.errors:
        flash(form.errors, 'danger')
    return render_template('review-edit.html',form=form, review_id=key)



#----------------- Delete Review Handler-------------#
@my_app.route('/reviews/delete/<key>', methods = ['GET','POST'])
def review_delete(key):
    command = """ SELECT *
                    FROM reviews
                    WHERE id = {p1}
            """.format(p1=key)
    cursor.execute(command)

    command = """ DELETE FROM reviews
                    WHERE id = {p1}
            """.format(p1=key)
    cursor.execute(command)
    conn.commit()

    flash('Your Review has been deleted')
    return redirect(url_for('app.insert_review'))




































