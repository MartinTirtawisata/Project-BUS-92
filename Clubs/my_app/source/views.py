from my_app import app
from my_app.source.models import SJSU_clubs
#-------------------- Home Page Handler --------------------
@app.route('/')
@app.route('/home')
def homePage():
    return """
<head>
<title> SJSU Clubs Homepage </title>



<!--BACKGROUND IMAGE-->

<style>
body {background-image: url("https://c1.staticflickr.com/6/5290/5265285009_cc99c82221_b.jpg"); 
      background-size:100% 100%;
      background-repeat:no-repeat;
}
h1   {color:rgb(255,215,0) ;text-align:center}
p    {color: red;}
</style>
</head>



<!--HEADER TEXTS-->

<font face="Palatino Linotype">
<h1 style="color:yellow;">San Jose State Clubs & Organizations</h1>
</font>

<center>
<p><font size="5" color="blue" font face="Georgia">An easy to use database to search for clubs & organizations on campus</font></p>

<p><b><font size="4" color="red" font face="Trebuchet MS">Click below to search for a club that interests you</font></b></p>
</center>

<hr>



<!--DEVELOPERS/SJSU LINKS-->

<body link="yellow">
<font face="Verdana">
<p style="text-align:left">
<a href="http://www.sjsu.edu/"> SJSU Website</a>
</p>
</body>

<body link="yellow">
<p style="text-align:left">
<a href="http://127.0.0.1:5000/developers"> Developers</a>
</p>
</font>
</body>



<!--MIDDLE IMAGE-->

<center><img src="https://upload.wikimedia.org/wikipedia/en/thumb/2/27/San_Jose_State_Spartans_Logo.svg/996px-San_Jose_State_Spartans_Logo.svg.png" alt="Spartan Logo" style="width:193px;height:193x;" align="bottom"></center>



<!--SHOW ALL CLUBS LINK-->

<body link="yellow">
<font size="25">
<p style="text-align:center">
<a href="http://127.0.0.1:5000/showall"> SHOW ALL SJSU CLUBS</a>
</p>
</font>
</body>



<!--BOTTOM RIGHT IMAGE-->

<div>
<img src="http://www.books-not-bombs.com/content/images/schools/sjsu.png"
style=
"position:absolute;
float:right;
right:0px;
bottom:0px;
width:120px;
height:120px;">
</div>

"""

def yesORno(boolean):
    if (boolean == True):
        return "Yes"
    else:
        return "No"

#-------------------- Show All Handler --------------------
@app.route('/showall')
def show_all():
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
        background-color: yellow;
        margin: 0;
        text-align: center;        
}

#logo {
        position: absolute;
        padding-left: 5px; 
        padding-top: 8px;
        overflow: auto;
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
    height: 200px;
    text-align: center;
    background-color: yellow;
    padding: 100px 0px 0px 0px;
    font-size: 110%;
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

<div id="container">


    <div id="fixedBar">

        <div id="logo">
            <img src="http://www.books-not-bombs.com/content/images/schools/sjsu.png" style="width:200px; height:130px" />
        </div>
        
        <div class="clear"> </div>


        <h1 id="title"><font face="Palatino Linotype"> Spartan Organizations</font></h1>
        
        <body link="yellow"><div id="home"><a href="http://127.0.0.1:5000/">Homepage</a></div></body>

</div>

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
    <th>Club_ID</th>
    <th>Organization Name</th>
    <th>Classification</th>
    <th>Location</th>
    <th>Rating</th>
    <th>Number of Reviews</th> 
    <th>Membership Cost</th>
    <th>Payment Required</th>
  </tr>
  
</div>  
    """
    
    footer = """
</table></body>
    """
    message_out = ''

    for item in SJSU_clubs:
        message_out += '<tr>'+\
                       '<td align="center">'+str(item[0])+'</td>'+\
                       '<td align="center">'+str(item[1])+'</td>'+\
                       '<td align="center">'+str(item[2])+'</td>'+\
                       '<td align="middle">'+str(item[3])+'</td>'+\
                       '<td align="middle">'+str(item[4])+'</td>'+\
                       '<td align="middle">'+str(item[5])+'</td>'+\
                       '<td align="middle">'+str(item[6])+'</td>'+\
                       '<td align="middle">'+yesORno((item[7]))+'</td>'+'</tr>'
        
    return (header+message_out+footer)



#-------------------- Show Key Handler --------------------
#Parameters: Key, integer
@app.route('/show/<key>') #Ways to control the parameter
# IMAGES HAVE BEEN ADDED TO THE FIRST 15 ITEMS IN THE TABLE ONLY SO FAR
def get_message(key):
    
    total = int(key)
    INDEX = (total - 1)
    
    if total >= len(SJSU_clubs):
        return "The key "+ key + " was not found" 
    
    header2 = """
    
        <head>
        <style>
        
            body {
                    margin: 0;
                    padding: 0;
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
    message += '<td><img src="'+str(SJSU_clubs[INDEX][10])+'"style="width:220px;height:326px" id="logo2"></td>'
    message += '<td valign="top"><p id="descrip">'+str(SJSU_clubs[INDEX][8])+'</p>'
    message += '<br>'
    message += '<p class="right"><b>Organization Name:</b>   '+str(SJSU_clubs[INDEX][1])+'</p>'
    message += '<p class="right"><b>Classification:</b>   ' +str(SJSU_clubs[INDEX][2])+ '</p>'
    message += '<p class="right"><b>Location:</b>   '+str(SJSU_clubs[INDEX][3])+ '</p>'
    message += '<p class="right"><b>President:</b>   '+str(SJSU_clubs[INDEX][9])+'</p>'
    message += '<p class="right"><b>Membership Fee:</b>   $'+str(SJSU_clubs[INDEX][6])+ '</p>'
    message += '<p class="right"><b>Fee required to join?</b>   '+yesORno(SJSU_clubs[INDEX][7])+ '</p>'
    message += '<p class="right"><b>Rating:</b>   '+str(SJSU_clubs[INDEX][4])+ '</p>'
    message += '<p class="right" id="bottom"><b>Number of Reviews</b>   '+str(SJSU_clubs[INDEX][5])+ '</p></td>'
    
   
    return header2+message+footer2

