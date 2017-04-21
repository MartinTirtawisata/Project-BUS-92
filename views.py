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

#-------------------- Show All Handler --------------------
@app.route('/showall')
def show_all():
    header = """
<head>
<title>All Movies</title>
<style>
table, th, td {
    border: 2px solid green;
    border-collapse: collapse;
    padding-left: 10px;
    padding-right: 10px;

}
th {
    padding: 5px;
    text-align: center;
    color: blue;
}
</style>
</head>
<body>

<table style="width:100%">
  <caption><h1>Movie List</h1></caption>
  <tr>
    <th>Key</th>
    <th>Movie</th>
    <th>Genre</th>
    <th>Popularity</th>
    <th> Year </th>
    <th> Length </th> 
  </tr>
    """
    
    footer = """
</table></body>
    """
    message_out = ""

    key = 0
    for item in SJSU_clubs:
        message_out += '<tr>'+\
                       '<td align="center">'+str(key)+'</td>'+\
                       '<td>'+item[0]+'</td>'+\
                       '<td>'+item[3]+'</td>'+\
                       '<td align="right">'+str(item[4])+'</td>'+\
                       '<td align="right">'+str(item[1])+'</td>'+\
                       '<td align="right">'+str(item[2])+'</td>'+'</tr>'
        key += 1
    return header+message_out+footer

@app.route('/developers')
#INSERT DEVELOPER INFO HERE


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