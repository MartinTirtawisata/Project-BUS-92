from flask import request, Blueprint, render_template
from my_app.source.models import cursor

my_app = Blueprint('app', __name__)

'''
Possible Ideas to make website better
#Homepage
1) Include a search function for what club is the user looking for - we could put auto completion on this (what nikaila did)
2) Leave a review link
3) Align the links so it's horizontal
4) #Maybe include most popular clubs with image

#Showall
1) Maybe reduce the columns to make it more specific, so people will have a reason to view each club individually
2) Give background color
3) Maybe the pictures could be animated OR carosel format (Changes every few seconds)

#show/<key>
1) Design it so it's the same with the others
2) Main image should be their logo
3) Add leave a review link; back to homepage; back to list link
4) We should add photos of the club, taken from Facebook
5) Add reviews at the bottom of the page
6) Star rated if possible? below the image/logo

#ReviewPage
1) Add more organizations
2) Add Gif or animiated picture to make it lively
3) re-format the text box
4) figure out how to add review to the database
#SQL
Create a new reviews table? with  category_ID, Club_id, reviews
'''

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



#----------Function for printing details of Organizations (Sub Table)---------

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


#---------------------- Function to print categories' table  -------------------

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

    if (len(club) == 0 or key == "0"):
        return "The key "+ key + " was not found"
        
  
    
    total = int(key)
    INDEX = (total - 1)
    
    
    message = '<table><col width="315">'
    message += '<td><img src="'+str(club[INDEX][URL])+'"style="width:220px;height:326px" id="logo2"></td>'
    message += '<p class="right"><b>Organization Name: </b>'+str(club[INDEX][ORGANIZATION_NAME])+'</p>'
    message += '<p class="right"><b>ID: </b>'+str(club[INDEX][CLUB_ID])+'</p>'
    message += '<p class="right"><b>Description: </b>'+str(club[INDEX][DESCRIPTION])+'</p>'
    message += '<p class="right"><b>Location: </b>   '+str(club[INDEX][LOCATION])+ '</p>'
    message += '<p class="right"><b>President: </b>   '+str(club[INDEX][PRESIDENT])+'</p>'
    message += '<p class="right"><b>Membership Fee: </b>   $'+str(club[INDEX][MEMBERSHIP_COST])+ '</p>'
    message += '<p class="right"><b>Fee required to join? </b>   '+yesORno(club[INDEX][PAYMENT_REQUIRED])+ '</p>'
    message += '<p class="right"><b>Rating: </b>   '+str(club[INDEX][RATING])+'</p>'
    message += '<p class="right"><b>Number Of Members: </b>   '+str(club[INDEX][NUMBER_OF_MEMBERS])+'</p>'
    
    footer3 = """ </table> </body> """
                                                        
    return (render_template("show_one.html")+message+footer3)



#------------------ Category Handler ----------------

@my_app.route('/category/<key>')

def one_category(key):
    
    command = """SELECT {a}.club_id, {a}.organization_name, {a}.president, {a}.number_of_members, {b}.category, {a}.rating
                      FROM {a} join {b} ON {a}.category_id = {b}.category_id
                      WHERE {b}.category like {k}
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


        
#--------------- Review Handler ------------------#

#Parameters: Key
@my_app.route ('/show/review')

def show_review():
    return render_template("ReviewPage.html")






#--------------- Category Handler ------------------#

@my_app.route ('/category')

def show_categories():
    
    command = """SELECT {b}.category_id, {b}.category
                FROM {b} 
                """.format(b='category')
                
    cursor.execute(command)
    club_data = cursor.fetchall()
    
    
    return print_categories(club_data)



































