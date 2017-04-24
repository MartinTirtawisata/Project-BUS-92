from my_app import app
from my_app.source.models import SJSU_clubs
#-------------------- Home Page Handler --------------------
@app.route('/')
@app.route('/home')
def homePage():
    return """
<title>Homepage</title>
<body>
    <head>
<title> SJSU Clubs Homepage </title>



<style>
    
    
    body {
        margin: 0;
        padding: 0;
    }
    
    #firstBar {
        height: 115px;
        background-color: #EAB010;
        text-align: center;
    }
    
    h1  {
        color: #3072AD ;
        font-size: 240%;
    
    }
    
    p {
        font-size: 1.4em;
        border: 1px solid black;
    }
    
    table {
            float: right;
            color: navy;
    }
    
    th {
            text-align: left;
            font-size: 1.2em;
    }
    
    td {
            font-family: "Courier New";
    }
    
    #mainImage {
        background-image: url("https://c1.staticflickr.com/6/5290/5265285009_cc99c82221_b.jpg"); 
        background-size: 100%;
        background-repeat: no-repeat;
        height: 900px;
        margin: 0;
    }
    
    #moreInfo {
        margin: 0;
    }
    
    #SJSU_link1 {
        float: left;
        padding-left: 20px;
        padding-top: 15px;
    }
    #SJSU_link2 {
        
        float:left;
        position: relative;
        top: 47px;
        left: -90px;
    }
    
    #SJSU_link3 {
        float:left;
        position: relative;
        top: 80px;
        left: -232px;
    }
    
    #title {
        padding-right: 320px;
        padding-top: 10px;
        margin: 0;
    }
    
    #title2 {
        margin: 0;
        padding-bottom: 0px;
    }

    
    #image4 {
        height: 500px;
        background-image: url("https://upload.wikimedia.org/wikipedia/en/thumb/2/27/San_Jose_State_Spartans_Logo.svg/996px-San_Jose_State_Spartans_Logo.svg.png");
        background-repeat: no-repeat;
        background-position: center;
        background-size: 35%;
    }
    
     a:link {
        color: black; 
        text-decoration: none;
     }
            
     a:visited {
        text-decoration: none;
        color: black;
     }
    
     a:hover {
        color: #3072AD;
     }
        
     a:active {
        color: yellow;
     } 
     
    #logo2div {
        float: right;
        
        position: relative;
        top: -174px;
    }
    
    #logo2 {
        height: 116px
    }
    
    
    
 
    
    
</style>
        
<body>
    
    <div id="firstBar">   
        
        <div id="SJSU_link1"> 
            <a href="http://www.sjsu.edu/"> SJSU Website </a> 
        </div>
        <div id="SJSU_link2">
            <a href="http://127.0.0.1:5000/showall"> List All Organizations</a>
        </div>
        <div id="SJSU_link3">
            <a href="http://www.sjsu.edu/getinvolved/studentorgs/new/"> Get Involved </a>
        </div>
    
        <h1 id="title"> San Jose State University </h1>
        <h1 id="title2"> Organizations </h1>
        
        <p>An easy to use database to search for clubs & organizations on and off campus</p>
        <div id="logo2div"> 
            <img src="http://www.books-not-bombs.com/content/images/schools/sjsu.png" id="logo2">
        </div>
    
    </div>
    
    <div id="mainImage"> </div>

    <div id="image4"> </div>
    
    <div id="names"> 
        <table>
            <tr> <th>Developers</th> </tr>
            <tr> <td>Carlos Quirarte</td> </tr>
            <tr> <td>Sean Scudellari</td> </tr>
            <tr> <td>Martin Tirtawisata</td> </tr>
        </table>
    </div>
    
    
    
</body>

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
        background-color: #EAB010;
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
            <img src="http://www.books-not-bombs.com/content/images/schools/sjsu.png" style="width:200px; height:130px" />
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
    <th>Club_ID</th>
    <th>Organization Name</th>
    <th>Classification</th>
    <th>Location</th>
    <th>President</th>
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
                       '<td align="middle">'+str(item[9])+'</td>'+\
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

