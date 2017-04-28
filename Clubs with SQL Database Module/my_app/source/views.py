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
    LOCATION = 3
    CATEGORY = 4
    RATING = 5


    header = """
            <head>
            <title>List of Clubs</title>
            <style>

            body {
                    margin: 0;
                    padding: 0;
            }
            #fixedBar {
                    height: 150px;
                    color: #3072AD;
                    background-color: #EAB010;
                    margin: 0;
                    text-align: center;
            }
            #logo {
                    position: absolute;
                    padding-top: 2px;
                    overflow: auto;
            }
            #logo3 {
                    
                    height: 138px;
            }
            
            #home {
                    padding-right: 25px;
                    position: absolute;
                    top: 10px;
                    right: 1px;
            }
            #title {
                    font-size: 340%;
                    padding-top: 40px;
                    font-family: "Times New Roman", Times, serif;
            }
            div.clear {
                    float: clear;
            }
            #image {
                background-image: url("http://www.mtmary.edu/_images/_main/interior-clubs-orgs-026.jpg");
                height: 400px;
                width: 100%;
                margin: 0;
                background-size:100% 100%;
                background-repeat:no-repeat;
            }
            #info {
                width: 100%;
                height: 150px;
                text-align: center;
                background-color: #EAB010;
                font-size: 110%;
                margin: 0;
                padding: 32px 0 0 0;
            }
            table, th, td {
                border-style: outset;
                border-collapse: collapse;
                padding-left: 5px;
                padding-right: 5px;
                background-color: white;
            }
            th {
                padding: 5px;
                text-align: center;
                color: blue;
            }
            </style>
            </head>
            <body>
                <div id="fixedBar">

                    <div id="logo">
                        <img src="http://www.books-not-bombs.com/content/images/schools/sjsu.png" id="logo3" />
                    </div>

                    <div class="clear"> </div>


                    <h1 id="title"><font face="Palatino Linotype"> Spartan Organizations</font></h1>

                    <body link="yellow"><div id="home"><a href="http://127.0.0.1:5000/">Homepage</a></div></body>

                <div id="image"> </div>


                <div id="info">
                    <p><font face="Georgia"><b>Welcome to Student Involvement! Your home for Fraternity & Sorority Life,
                        Student Organziations, Campus Programming & Leadership! </p>
                    <p> With over 400 student organizations at SJSU, getting involved is the best
                        way to connect with campus life! </font></b></p>
                </div>

            <table style="width:100%">
              <caption><h1>San Jose State Clubs and Organizations</h1></caption>

              <tr>
                <th>Club ID</th>
                <th>Organization Name</th>
                <th>President</th>
                <th>Location</th>
                <th>Category</th>
                <th>Rating</th>
              </tr>

            </div>
                """

    footer = """
    </table></body>
    """
    message_out = ''

    key = 0
    for item in SJSU_Organizations:
        message_out += '<tr>'+\
                       '<td align="center">'+str(item[CLUB_ID])+'</td>'+\
                       '<td align="center">'+str(item[ORGANIZATION_NAME])+'</td>'+\
                       '<td align="center">'+str(item[PRESIDENT])+'</td>'+\
                       '<td align="middle">'+str(item[LOCATION])+'</td>'+\
                       '<td align="middle">'+str(item[CATEGORY])+'</td>'+\
                       '<td align="middle">'+str(item[RATING])+'</td>'+'</tr>'

        key += 1

    return (header+message_out+footer)

#----------Function for printing details of Organizations (Sub Table)---------

def yesORno(boolean):
    if (boolean == True):
        return "Yes"
    else:
        return "No"


def print_subtable(SJSU_Organizations):
    CLUB_ID = 0
    ORGANIZATION_NAME = 1
    NUMBER_OF_MEMBERS = 2
    NUMBER_OF_REVIEWS = 3
    PAYMENT_REQUIRED = 4
    MEMBERSHIP_COST = 5

    header = """
            <head>
            <title>Further Organization Details</title>
            <style>

            body {
                    margin: 0;
                    padding: 0;
            }
            #fixedBar {
                    height: 150px;
                    color: #3072AD;
                    background-color: #EAB010;
                    margin: 0;
                    text-align: center;
            }
            #logo {
                    position: absolute;
                    padding-top: 2px;
                    overflow: auto;
            }
            #logo3 {

                    height: 138px;
            }

            #home {
                    padding-right: 25px;
                    position: absolute;
                    top: 10px;
                    right: 1px;
            }
            #title {
                    font-size: 340%;
                    padding-top: 40px;
                    font-family: "Times New Roman", Times, serif;
            }
            div.clear {
                    float: clear;
            }
            #image {
                background-image: url("http://www.mtmary.edu/_images/_main/interior-clubs-orgs-026.jpg");
                height: 400px;
                width: 100%;
                margin: 0;
                background-size:100% 100%;
                background-repeat:no-repeat;
            }
            #info {
                width: 100%;
                height: 150px;
                text-align: center;
                background-color: #EAB010;
                font-size: 110%;
                margin: 0;
                padding: 32px 0 0 0;
            }
            table, th, td {
                border-style: outset;
                border-collapse: collapse;
                padding-left: 5px;
                padding-right: 5px;
                background-color: white;
            }
            th {
                padding: 5px;
                text-align: center;
                color: blue;
            }
            </style>
            </head>
            <body>
                <div id="fixedBar">

                    <div id="logo">
                        <img src="http://www.books-not-bombs.com/content/images/schools/sjsu.png" id="logo3" />
                    </div>

                    <div class="clear"> </div>


                    <h1 id="title"><font face="Palatino Linotype"> Spartan Organizations</font></h1>

                    <body link="yellow"><div id="home"><a href="http://127.0.0.1:5000/">Homepage</a></div></body>

                <div id="image"> </div>


                <div id="info">
                    <p><font face="Georgia"><b>Here, you will find further details regarding each club</font></b></p>
                </div>

            <table style="width:100%">
              <caption><h1>San Jose State Clubs and Organizations</h1></caption>

              <tr>
                <th>Club ID</th>
                <th>Organization Name</th>
                <th>Number Of Members</th>
                <th>Number Of Reviews</th>
                <th>Payment Required?</th>
                <th>Membership Cost</th>
              </tr>

            </div>
                """

    footer = """
    </table></body>
    """
    message_out = ''

    key = 0
    for item in SJSU_Organizations:
        message_out += '<tr>' + \
                       '<td align="center">' + str(item[CLUB_ID]) + '</td>' + \
                       '<td align="center">' + str(item[ORGANIZATION_NAME]) + '</td>' + \
                       '<td align="center">' + str(item[NUMBER_OF_MEMBERS]) + '</td>' + \
                       '<td align="middle">' + str(item[NUMBER_OF_REVIEWS]) + '</td>' + \
                       '<td align="middle">' + yesORno(club[PAYMENT_REQUIRED]) + '</td>' + \
                       '<td align="middle">' + str(item[MEMBERSHIP_COST]) + '</td>' + '</tr>'

        key += 1

    return (header + message_out + footer)




#-------------------- Home Page Handler --------------------
@my_app.route('/')
@my_app.route('/home')
def homePage():
    return render_template("Homepage Template.html")

#-------------------- Show All Handler --------------------
@my_app.route('/showall')

def organizations():
    command = """SELECT {a}.club_id, {a}.organization_name, {a}.president, {a}.location, {b}.category, {a}.rating
                      FROM {a} join {b} ON {a}.category_id = {b}.category_id
        """.format(a="organizations", b='category')
    cursor.execute(command)
    club_data = cursor.fetchall()

    return (print_maintable(club_data))
 
#-------------------- Further Details Handler --------------------
@my_app.route('/details')

def details():
    command = """SELECT {c}.club_id, {a}.organization_name, {c}.number_of_members, {c}.number_of_reviews, {c}.payment_required, {c}.membership_cost
                          FROM {c} join {a} ON {c}.club_id = {a}.club_id
            """.format(a="organizations", c='details')
    cursor.execute(command)
    club_data = cursor.fetchall()

    return (print_subtable(club_data))




#-------------------- Show Key Handler --------------------
#Parameters: Key, integer
@my_app.route('/show/<key>') #Ways to control the parameter

def get_message(key):    
    ORGANIZATION_NAME = 0
    PRESIDENT = 1
    LOCATION = 2
    RATING = 3
    NUMBER_OF_MEMBERS = 4
    PAYMENT_REQUIRED = 5
    MEMBERSHIP_COST = 6
    URL = 7
    DESCRIPTION = 8
    CLUB_ID = 9
  
    
    command = """ SELECT {a}.club_id, {a}.Organization_name, {a}.description, {a}.President, {a}.Location, {a}.Rating, {c}.number_of_members, {c}.payment_required,{c}.membership_cost,{c}.Image_URL
                         FROM {a} join {c} ON {a}.club_id = {c}.club_id
                         WHERE {a}.club_id = {p1}
    """.format(a="Organizations", c='details', p1=key)
    cursor.execute(command)
    club_data = cursor.fetchall()                           
  
    if len(club_data) == 0:
        return "The key "+ key + " was not found"
    club = club_data[0] 

    header2 = """

        <head>
        <style>

            body {
                    margin: 0;
                    padding: 0;
                    background-color: #E3E3E5;
            }

            #image2 {
                    background-image: url("http://www.pressdemocrat.com/csp/mediapool/sites/dt.common.streams.StreamServer.cls?STREAMOID=1Q_PpZ$$ef91sZ23ohmJAc$daE2N3K4ZzOUsqbU5sYshvOQ8ctBOtI8vYy4xeVFrWCsjLu883Ygn4B49Lvm9bPe2QeMKQdVeZmXF$9l$4uCZ8QDXhaHEp3rvzXRJFdy0KqPHLoMevcTLo3h8xh70Y6N_U_CryOsw6FTOdKL_jpQ-&CONTENTTYPE=image/jpeg");
                    height: 535px;
                    width: 100%;
                    margin: 0;
                    background-size:100% 100%;
                    background-repeat:no-repeat;
                    text-align: center;
                    font-size: 1.3em;
            }

            #descrip {
                    font-size: 1.5em;
                    text-align: center;
                    padding-top: 20px;
            }

            #logo2 {
                    margin: auto;
                    display: block;
            }



            table td {
                    border-right: 2px solid #EAB010;
            }

            table td:first-child {
                    border-left: none;
            }

            table td:last-child {
                    border-right: none;
            }

            p.right {
                    padding-left: 20px;
            }

            #filler {
                    height: 150px;
            }

            #bottom {
                    padding-bottom: 25px;
            }

            #list {
                    display: inline-block;
                    margin-right: 10px;

            }

            #home2 {
                    display: inline-block;
            }

            a:link {
                    color: black;
                    text-decoration: none;
            }

            a:visited {
                    text-decorator: none;
            }


            a:hover {
                    color: #EAB010;
            }


            a:active {
                    color: yellow;
            }

        </style>
        </head>
        <body>

            <div id="club_name">

            <div id="image2">
                <div id="list"><a href="http://127.0.0.1:5000/showall"> List </a> </div>
                <div id="home2"><a href="http://127.0.0.1:5000/"> Homepage </a> </div>
            </div>
        """

    footer2 = """
        </body> """


    message = '<table><col width="315">'
    message += '<td><img src="'+str(club)[URL]+'style="width:220px;height:326px" id="logo2"></td>'
    message += '<p class="right"><b>Organization Name:</b>'+str(club[ORGANIZATION_NAME])+'</p>'
    message += '<p class="right"><b>ID:</b>' + str(club[CLUB_ID]) + '</p>'
    message += '<p class="right"><b>Description:</b>'+str(club[DESCRIPTION])+'</p>'
    message += '<p class="right"><b>Location:</b>   '+str(club[LOCATION])+ '</p>'
    message += '<p class="right"><b>President:</b>   '+str(club[PRESIDENT])+'</p>'
    message += '<p class="right"><b>Membership Fee:</b>   $'+str(club[MEMBERSHIP_COST])+ '</p>'
    message += '<p class="right"><b>Fee required to join?</b>   '+yesORno(club[PAYMENT_REQUIRED])+ '</p>'
    message += '<p class="right"><b>Rating:</b>   '+str(club[RATING])+ '</p>'
    message += '<p class="right" id="bottom"><b>Number of Reviews:</b>   '+str(club[NUMBER_OF_MEMBERS])+ '</p></td>'


    return header2+message+footer2


#------------------ Club Search ----------------
@my_app.route('/club-search')
def club_search ():
    club_ID = request.args.get('clubID')
    orgName = request.args.get('orgName')
    president = request.args.get('president')
    location = request.args.get('location')
    rating = request.args.get('rating')
    num_of_reviews = request.args.get('number_of_reviews')
    payment_required = request.args.get('payment_required')
    membership_cost = request.args.get('membership_cost')
    
    
    validation = ""
    
    if club_ID != None:
        validation += "organizations.club_id = "+str(club_ID)
        
    if orgName != None:
        if validation != "":
            validation += " AND " 
        validation += "organizations.organization_name LIKE '%"+orgName+"%'"
        
    if president != None:
        if validation !="":
            validation += " AND "
        validation += "organizations.president LIKE '%"+president+"%'"
        
    if location != None:
        if validation !="":
            validation += " AND "
        validation += "organizations.location LIKE '%"+location+"%'"
        
    if rating != None:
        if validation !="":
            validation += " AND "
        validation += "organizations.rating= "+str(rating)
        
    if num_of_reviews != None:
        if validation !="":
            validation += " AND "
        validation += "organizations.number_of_reviews = "+str(num_of_reviews) 
    
# Confused on how to make it boolean    
    if payment_required != None:
        if validation !="":
            validation += " AND "
        validation += "organizations.payment_required '%"+payment_required+"%'"
        
    if membership_cost != None:
        if validation !="":
            validation += " AND "
        validation += "organizations.membership_cost= "+str(membership_cost)

        #MARTIN MAKE SURE CHANGE THE B'S TO C'S ON YOUR VIEWS FILE
    if validation == "":
        command = """ SELECT {a}.club_id, {a}.president, {a}.location, {a}.rating, {c}.number_of_reviews, {c}.payment_required, {c}.membership_cost
        ON {a} join {c} FROM {a}.club_id = {c}.club_ID
        WHERE {val}
        """.format(a="organizations",c= 'details')
    else:
        command = """ SELECT {a}.club_id, {a}.president, {a}.location, {a}.rating, {c}.number_of_reviews, {c}.payment_required, {c}.membership_cost
        ON {a} join {c} FROM {a}.category_ID = {c}.club_ID
        WHERE {val}
        """.format(a="organizations",c= 'details',val = validation)
    
    cursor.execute(command)
    club_data = cursor.fetchall()
    return (print_maintable(club_data))


'''We have to create new def function for this because the print_table is set for the home page only'''


        
#--------------- Review Handler ------------------#
#Parameters: Key
@my_app.route ('/show/review')

def show_review():
    return render_template("ReviewPage.html")



































