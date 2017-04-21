from my_app import app
from my_app.source.models import SJSU_clubs

#-------------------- Home Page Handler --------------------
@app.route('/')
@app.route('/home')
def homePage():
    return """
<head>
<title> SJSU Clubs Homepage </title>
<style>
body {background-image: url("https://c1.staticflickr.com/6/5290/5265285009_cc99c82221_b.jpg"); 
      background-size:100% 100%;
      background-repeat:no-repeat;
}
h1   {color:rgb(255,215,0) ;text-align:center}
p    {color: red;}
</style>
</head>
<h1> San Jose State Clubs & Organization </h1>
<hr>
<p style="text-align:left">
<a href="http://127.0.0.1:5000/developers"> Developers</a>
<p style="text-align:center">
<a href="http://127.0.0.1:5000/showall">Show all SJSU Clubs</a>
</p>
"""

#-------------------- Show All Handler --------------------
@app.route('/showall')
def show_all():
    header = """
<head>
<title>List of Clubs</title>
<style>

body {
        margin: 0;
}

#home {
    padding: 25px 5px 5px 20px;
}

#title {
        padding: 15px 20px 15px 20px;
        text-align: center;
        font-size: 50px;
        color: #3072AD;
        background-color: #EAB010;
        margin: 0;
}

#image {
    background-image: url("http://www.mtmary.edu/_images/_main/interior-clubs-orgs-026.jpg");
    height: 400px;
    width: 100%;
    margin: 0;
}

#info {
    width: 100%;
    height: 200px;
    text-align: center;
    background-color: grey;
    padding: 100px 0px 0px 0px;
    font-size: 110%;
}


table, th, td {
    border-style: outset;
    border-collapse: collapse;
    padding-left: 10px;
    padding-right: 10px;
    background-color: #e3e3e7; 
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

<div id="home"><a href="http://127.0.0.1:5000/">Homepage</a></div>

<h1 id="title">Spartan Organizations</h1>

<div id="image"> </div>

<div id="info">
<p>Welcome to Student Involvement! Your home for Fraternity & Sorority Life, 
Student Organziations, Campus Programming & Leadership! </p>
<p> With over 400 student organizations at SJSU, getting involved is the best 
way to connect with campus life! </p>
</div>

<table style="width:100%">
  <caption><h1>San Jose State Clubs and Organizations</h1></caption>
   
  <tr>
    <th>Club_ID</th>
    <th>Club Name</th>
    <th>Classification</th>
    <th>Location</th>
    <th>Rating</th>
    <th>Number of Reviews</th> 
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
                       '<td align="middle">'+str(item[5])+'</td>'+'</tr>'
        
    return (header+message_out+footer)



#-------------------- Show Key Handler --------------------
#Parameters: Key, integer
@app.route('/show/<key>') #Ways to control the parameter
def get_message(key):
    index = int(key)
    MOVIES = 0
    if index >= len(MOVIES):
        return "The key "+ key + " was not found"     

    message = '<table><col width="250">'   
    message += '<td><img src='+MOVIES[index][6]+' style="width:220px;height:326px"></td>'
    message += '<td valign="top"><h1 style="color:blue;">'+ MOVIES[index][0]+'</h1>'
    message += '<p><b>Year:</b> ' + str(MOVIES[index][1])+'</p>'
    message += '<p><b>Genre:</b> ' + MOVIES[index][3]+'</p>'
    message += '<p><b>Popularity:</b> ' + str(MOVIES[index][4])+'</p>'
    message += '<p><b>Awards:</b> ' + str(MOVIES[index][5])+'</p></td>'
    
    return message