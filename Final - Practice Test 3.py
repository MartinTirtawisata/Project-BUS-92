from flask import Flask
app = Flask(__name__)

NAME = 0
YEAR = 1
LENGTH = 2
RATING = 3
FRIDAY_SALES = 4
SATURDAY_SALES = 5
SUNDAY_SALES = 6
GENRES = 7
STAR = 8
IMAGE = 9

Movies =[
#Name,Year,Length, Rating,Genres,Star,Image
["The Revenant",2016,160, "PG-13",300000,150000,500000,"Horror, Thriller","Kevin Bacon","https://upload.wikimedia.org/wikipedia/en/thumb/b/b6/The_Revenant_2015_film_poster.jpg/220px-The_Revenant_2015_film_poster.jpg"],
["Love & Friendship",2016,180, "PG ",120000,145000,230000,"Drama, Romance"" ","Kate Beckinsale","https://upload.wikimedia.org/wikipedia/en/thumb/f/ff/Love_%26_Friendship_poster.png/220px-Love_%26_Friendship_poster.png"],
["High-Rise",2015,120, "R",70000,94000,103000,"Drama","Tom Hiddleston","https://upload.wikimedia.org/wikipedia/en/thumb/f/f5/High_Rise_2014_Film_Poster.jpg/220px-High_Rise_2014_Film_Poster.jpg"],
["Money Monster",2016,95, "R",400000,450000,670000,"Crime, Drama, Thriller ","George Clooney","https://upload.wikimedia.org/wikipedia/en/thumb/f/f2/Money_Monster_poster.png/220px-Money_Monster_poster.png"],
["Last Days in the Desert",2015,155,"PG-13",181000,200000,242000,"Adventure, Drama, History","Ewan McGregor","https://upload.wikimedia.org/wikipedia/en/thumb/c/ce/Last_Days_in_the_Desert_poster.jpg/220px-Last_Days_in_the_Desert_poster.jpg"],
["Search Party",2014,117, "R",41000,73000,99000,"Comedy","Adam Pally","https://upload.wikimedia.org/wikipedia/en/thumb/5/55/Search_party_xlg.jpg/220px-Search_party_xlg.jpg"],
["Dheepan",2015,190, "R",200000,210000,348000,"Crime, Drama"," Jesuthasan Antonythasan","https://upload.wikimedia.org/wikipedia/en/thumb/6/6e/Dheepan_poster.jpg/220px-Dheepan_poster.jpg"],
["Sunset Song",2015,165, "R",182000,293000,314000,"Drama","Agyness Deyn","https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/Sunset_Song_%28film%29_POSTER.jpg/220px-Sunset_Song_%28film%29_POSTER.jpg"],
["Kisschasy",2015,120, "R",110000,184000,221000,"Horror, Thriller ","Mille Dinesen","https://upload.wikimedia.org/wikipedia/en/thumb/b/bd/Kisschasy_-_Kisschasy_The_Movie.jpg/220px-Kisschasy_-_Kisschasy_The_Movie.jpg"],
["Captain America: Civil War",2016,105, "PG-13",230000,450000,623000,"Action, Adventure, Sci-Fi","Chris Evans","https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Captain_America_Civil_War_poster.jpg/220px-Captain_America_Civil_War_poster.jpg"],
["The Angry Birds Movie",2016, 95, "PG",51000, 73000, 82000,"Animation, Action, Comedy, Family"," Peter Dinklage","https://upload.wikimedia.org/wikipedia/en/thumb/6/65/Angry_Birds_2016_film_poster.jpg/220px-Angry_Birds_2016_film_poster.jpg"],
["The Nice Guys",2016,124, "R",64000,89000,120000,"Action, Comedy, Crime, Mystery,Thriller","Ryan Gosling","https://upload.wikimedia.org/wikipedia/en/thumb/e/e9/The_Nice_Guys_poster.png/220px-The_Nice_Guys_poster.png"],
["Me Before You",2016,130, "PG-13",81000,160000,241000,"Drama","Emilia Clarke","https://upload.wikimedia.org/wikipedia/en/thumb/f/fd/Me_Before_You_%28film%29.jpg/220px-Me_Before_You_%28film%29.jpg"],
["The Huntsman: Winter's War",2016,165,"PG-13",174000,193000,237000,"Action, Adventure, Drama, Fantasy","Chris Hemsworth","https://upload.wikimedia.org/wikipedia/en/thumb/a/ab/The_Huntsman_%E2%80%93_Winter%27s_War_poster.jpg/220px-The_Huntsman_%E2%80%93_Winter%27s_War_poster.jpg"]
]


"""
_____________________________________________
20 Points - Question 1:
Create a homepage for the Century Movie Theathers 
with the following requirements:
a) At least one image from wikipedia (no other sources allowed)
b) A background different than white, 3 Different sizes and colors 
c) Student name and ID
e) links to all other pages in this project
_____________________________________________

"""
@app.route('/')
@app.route('/home')
def Home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Century Movie Theaters</title>       
</head>
<style>
    body {
    margin: 0;
    background-color: grey;
    text-align: center
}

#Pagetitle {
    background-color: #7fefdc;
    color: #af0827;
    width: 100%;
    height: 50px;
    text-align: center;
    font-size: 2em;
    padding-top: 10px;
}

#navbar {
    background-color: #e6ecf2;
    width: 100%;
    height: 55px;
}

#navbarSelection {
    float: left;
    color: #160f00;
}

#navbarSelection ul {
    margin: 10px;
}

#navbarSelection li {
    margin-top: 1px;
    list-style: none;
    float: left;
    font-weight: bold;
    padding: 10px 0 12px 0;
}

#navbarSelection li:last-child {
    border-right: none;
}

a.one:link, a.one:visited {
    color: black; 
    text-decoration: none;
    padding: 10px 30px 12px 30px;
    font-family: "Times New Roman", Times, serif; 
}

a.one:hover, a.one:active {
    color: black;
    background-color: #758fdd;
} 

a.two:link, a.two:visited {
    color: black; 
    text-decoration: none;
    padding: 10px 30px 12px 30px;
    font-family: Arial, Helvetica, sans-serif;   
}
a.two:hover, a.two:active {
    color: black;
    background-color: #758fdd;
} 

a.three:link, a.three:visited {
    color: black; 
    text-decoration: none;
    padding: 10px 30px 12px 30px;
    font-family: "Verdana", Times, sans-serif;   
}

a.three:hover, a.two:active {
    color: black;
    background-color: #758fdd;
} 


</style>

    <body>

    
         <div id="Pagetitle"> Century Movies Theatre </div>
        
             <div id="navbar">
            
                 <div class="fixedBar"> 
                    
                     <div id="navbarSelection">
                        
                         <ul>
                             <li><a class="one" href="http://127.0.0.1:5000/home">Home</a></li>
                             <li><a class="two" href="http://127.0.0.1:5000/movies">Movies List</a></li>
                             <li><a class="three" href="http://127.0.0.1:5000/disney">Disney Movies</a></li>
                      
                         </ul>
                    
                     </div>
                
                 </div>
            
             </div>
             <img src="https://upload.wikimedia.org/wikipedia/en/thumb/b/b6/The_Revenant_2015_film_poster.jpg/220px-The_Revenant_2015_film_poster.jpg" alt="Orion Cereal" style="width:304px;height:228px;">
         
         <h2><strong>Student Name: </strong> Martin Tirtawisata </h2>
         <h3><strong> Student ID: </strong> 011477076 </h3>
             
             
    
    </body>
</html>
    """

"""
_____________________________________________
20 Points - Question 2:
Create an individual page for movies
with the following requirements:
a) Movie Image
b) A background different than white, 3 different fonts, 3 different colors
c) At least 4 fields displayed
d) If id does not exist it should send a 
            message that it does not exist
_____________________________________________

"""
@app.route('/movie/<id>')
def movie(id):
    header = """
        <html>
        <head>
            <title>Movie Type</title>
        </head>
        <style>

         body {
        margin: 0;
        background-color: grey;
        text-align: center
    }

    #Pagetitle {
        background-color: #7fefdc;
        color: #af0827;
        width: 100%;
        height: 50px;
        text-align: center;
        font-size: 2em;
        padding-top: 10px;
    }

    #navbar {
        background-color: #e6ecf2;
        width: 100%;
        height: 55px;
    }

    #navbarSelection {
        float: left;
        color: #160f00;
    }

    #navbarSelection ul {
        margin: 10px;
    }

    #navbarSelection li {
        margin-top: 1px;
        list-style: none;
        float: left;
        font-weight: bold;
        padding: 10px 0 12px 0;
    }

    #navbarSelection li:last-child {
        border-right: none;
    }

    a.one:link, a.one:visited {
        color: black; 
        text-decoration: none;
        padding: 10px 30px 12px 30px;
        font-family: "Times New Roman", Times, serif; 
    }

    a.one:hover, a.one:active {
        color: black;
        background-color: #758fdd;
    } 

    a.two:link, a.two:visited {
        color: black; 
        text-decoration: none;
        padding: 10px 30px 12px 30px;
        font-family: Arial, Helvetica, sans-serif;   
    }
    a.two:hover, a.two:active {
        color: black;
        background-color: #758fdd;
    } 

    a.three:link, a.three:visited {
        color: black; 
        text-decoration: none;
        padding: 10px 30px 12px 30px;
        font-family: "Verdana", Times, sans-serif;   
    }

    a.three:hover, a.two:active {
        color: black;
        background-color: #758fdd;
    } 

    table {
        margin-top: 50px;
        background-color: #FAFAFA;
    }

    table td {
        border-right: 2px solid #EAB010;
        font-family: Arial, Helvetica, sans-serif; 
    }

        </style>
        <body>

            <div id="Pagetitle"> Movie Type</div>

                 <div id="navbar">

                     <div class="fixedBar"> 

                         <div id="navbarSelection">

                             <ul>
                                 <li><a class="one" href="http://127.0.0.1:5000/home">Home</a></li>
                                 <li><a class="two" href="http://127.0.0.1:5000/movies">Movies List/a></li>
                                 <li><a class="three" href="http://127.0.0.1:5000/disney">Disney Movies</a></li>

                             </ul>

                         </div>

                     </div>

                 </div>


        """

    footer = """
        </table></body></html>
        """

    index = int(id)
    if index >= len(Movies):
        return "The key " + id + " was not found"

    message = '<table><col width="250">'
    message += '<td><img src=' + (Movies[index][IMAGE]) + ' style="width:220px;height:226px"></td>'
    message += '<td valign="top"><h1 style="color:blue;">' + (Movies[index][NAME]) + '</h1>'
    message += '<p style="color:red;"><b>Year:</b> ' + str(Movies[index][YEAR]) + '</p>'
    message += '<p style="color:green;"><b>Length:</b> ' + str(Movies[index][LENGTH]) + '</p>'
    message += '<p><b>Rating:</b> ' + str(Movies[index][RATING]) + '</p>'
    message += '<p><b>Friday sales</b> ' + str(Movies[index][FRIDAY_SALES]) + '</p>'
    message += '<p><b>Genre</b> ' + str(Movies[index][GENRES]) + '</p></td>'
    return (header + message + footer)


"""
NAME = 0
YEAR = 1
LENGTH = 2
RATING = 3
FRIDAY_SALES = 4
SATURDAY_SALES = 5
SUNDAY_SALES = 6
GENRES = 7
STAR = 8
IMAGE = 9
_____________________________________________
20 Points - Question 3:
Implement the "Movies" table with the following
columns:
- Index in first column
- Exactly 5 additional columns of your choice

In addition, your table should have the following
formatting requirements:
a) First column should display the index
c) Background shouldn't be white
d) Name of the movies should be clickable to individual pages
e) Link to the homepage
_____________________________________________

"""
@app.route('/movies')
def movies():
    header = """
   <head>
   <title>Movie List</title>
   <style>
       body {
       margin: 0;
       background-color: grey;
       text-align: center
   }

   #Pagetitle {
       background-color: #7fefdc;
       color: #af0827;
       width: 100%;
       height: 50px;
       text-align: center;
       font-size: 2em;
       padding-top: 10px;
   }

   #navbar {
       background-color: #e6ecf2;
       width: 100%;
       height: 55px;
   }

   #navbarSelection {
       float: left;
       color: #160f00;
   }

   #navbarSelection ul {
       margin: 10px;
   }

   #navbarSelection li {
       margin-top: 1px;
       list-style: none;
       float: left;
       font-weight: bold;
       padding: 10px 0 12px 0;
   }

   #navbarSelection li:last-child {
       border-right: none;
   }

   a.one:link, a.one:visited {
       color: black; 
       text-decoration: none;
       padding: 10px 30px 12px 30px;
       font-family: "Times New Roman", Times, serif; 
   }

   a.one:hover, a.one:active {
       color: black;
       background-color: #758fdd;
   } 

   a.two:link, a.two:visited {
       color: black; 
       text-decoration: none;
       padding: 10px 30px 12px 30px;
       font-family: Arial, Helvetica, sans-serif;   
   }
   a.two:hover, a.two:active {
       color: black;
       background-color: #758fdd;
   } 

   a.three:link, a.three:visited {
       color: black; 
       text-decoration: none;
       padding: 10px 30px 12px 30px;
       font-family: "Verdana", Times, sans-serif;   
   }

   a.three:hover, a.two:active {
       color: black;
       background-color: #758fdd;
   } 

   </style>
   </head>
   <body>    
           <div id="Pagetitle"> Movie List</div>

                <div id="navbar">

                    <div class="fixedBar"> 

                        <div id="navbarSelection">

                            <ul>
                                <li><a class="one" href="http://127.0.0.1:5000/home">Home</a></li>
                                <li><a class="two" href="http://127.0.0.1:5000/movies">Movies List</a></li>
                                <li><a class="three" href="http://127.0.0.1:5000/disney">Disney Movies</a></li>

                            </ul>

                        </div>

                    </div>

                </div>


           <table style="width:100%">
               <caption><h1>List Of All Movies</h1></caption>
                   <tr>
                       <th>Index</th>
                       <th>Name</th>
                       <th>Year</th>
                       <th>Length Of Movie</th>
                       <th>Rating</th>
                       <th>Genre</th>
                   </tr>

       """
    footer = """
   </table></body>
       """

    index = 0
    message_out = ""
    for Movie in Movies:
        message_out += '<tr>' + \
                       '<td align="center">' + str(index) + '</td>' + \
                       '<td>''<a class="four" href="http://127.0.0.1:5000/movie/' + str(index) + '">' + Movie[NAME] + '</a></td>' + \
                       '<td>' + str(Movie[YEAR]) + '</td>' + \
                       '<td>' + str(Movie[LENGTH]) + '</td>' + \
                       '<td>' + str(Movie[RATING]) + '</td>' + \
                       '<td>' + str(Movie[GENRES]) + '</td>' + \
                       '</tr>'
        index += 1

    return (header + message_out + footer)


"""
NAME = 0
YEAR = 1
LENGTH = 2
RATING = 3
FRIDAY_SALES = 4
SATURDAY_SALES = 5
SUNDAY_SALES = 6
GENRES = 7
STAR = 8
IMAGE = 9
___________________________________________
15 Points - Question 4:
Disney studios is working with our company on a 
partnership to promote movies.
For this partnership, we are interested only in long 
movies (more than 100 minutes length) that are either Dramas rated "R"
or Thrillers rated "PG-13".

Create a function DisneyDeal(moview), that returns
true or false if the movie should be promoted.
___________________________________________
"""
def DisneyDeal(movie):
    if movie[LENGTH] > 100:
        if "Drama" in movie[GENRES] and movie[RATING] == "R":
            return True
        if "Thriller" in movie[GENRES] and movie[RATING] == "PG-13":
            return True
    return False




"""
a) Interested in long movies where LENGTH > 100 AND
b) Either Drama(GENRES) rated R (RATING = R) OR
c) Thrillers(GENRES) rated PG-13 (RATING)
___________________________________________
20 Points - Question 5:
Disney will be paid a comission of 10% for the total sales (Friday
Sunday and Satturday)

Using the function DisneyDeal() you created in question 3,
implement the "Movies for Disney" table with the following
columns:
- Index in first column
- Exactly 6 additional columns of your choice
- 8th column shows the comission for Disney

Extended Requirements:
a) The title of the list should include "for Disney"
b) Add a note below the table with the criteria used for Disney's list
___________________________________________
"""
@app.route('/disney')
def disney():
    header = """
       <head>
       <title>Movies For Disney</title>
       <style>
       table, th, td {

             padding-left: 10px;
           padding-right: 10px;
       }
       th {
           padding: 5px;
           text-align: center;
           color: blue;
       }
        body {
        margin: 0;
        background-color: grey;
        text-align: center
    }

    #Pagetitle {
        background-color: #7fefdc;
        color: #af0827;
        width: 100%;
        height: 50px;
        text-align: center;
        font-size: 2em;
        padding-top: 10px;
    }

    #navbar {
        background-color: #e6ecf2;
        width: 100%;
        height: 55px;
    }

    #navbarSelection {
        float: left;
        color: #160f00;
    }

    #navbarSelection ul {
        margin: 10px;
    }

    #navbarSelection li {
        margin-top: 1px;
        list-style: none;
        float: left;
        font-weight: bold;
        padding: 10px 0 12px 0;
    }

    #navbarSelection li:last-child {
        border-right: none;
    }

    a.one:link, a.one:visited {
        color: black; 
        text-decoration: none;
        padding: 10px 30px 12px 30px;
        font-family: "Times New Roman", Times, serif; 
    }

    a.one:hover, a.one:active {
        color: black;
        background-color: #758fdd;
    } 

    a.two:link, a.two:visited {
        color: black; 
        text-decoration: none;
        padding: 10px 30px 12px 30px;
        font-family: Arial, Helvetica, sans-serif;   
    }
    a.two:hover, a.two:active {
        color: black;
        background-color: #758fdd;
    } 

    a.three:link, a.three:visited {
        color: black; 
        text-decoration: none;
        padding: 10px 30px 12px 30px;
        font-family: "Verdana", Times, sans-serif;   
    }

    a.three:hover, a.two:active {
        color: black;
        background-color: #758fdd;
    } 
       </style>
       </head>
       <body>
           <div id="Pagetitle"> For Disney</div>

                 <div id="navbar">

                     <div class="fixedBar"> 

                         <div id="navbarSelection">

                             <ul>
                                 <li><a class="one" href="http://127.0.0.1:5000/home">Home</a></li>
                                 <li><a class="two" href="http://127.0.0.1:5000/movies">Movies List</a></li>
                                 <li><a class="three" href="http://127.0.0.1:5000/disney">Disney Movies</a></li>

                             </ul>

                         </div>

                     </div>

                 </div>
           <table style="width:100%">
               <caption><h1>for Costco</h1></caption>
                   <tr>
                       <th>Index</th>
                       <th>Name</th>
                       <th>Year</th>
                       <th>Length</th>
                       <th>Rating</th>
                       <th>Genres</th>
                       <th>Star</th>
                       <th>Commission</th>
                   </tr>

           """
    footer = """
       </table>
       <pre> 
           a) Interested in long movies where LENGTH > 100 AND
            b) Either Drama(GENRES) rated R (RATING = R) OR
            c) Thrillers(GENRES) rated PG-13 (RATING)
       </pre>
       </body>
           """
    index = 0
    message_out = ""
    for movie in Movies:
        if DisneyDeal(movie):
            message_out += '<tr>' + \
                           '<td align="center">' + str(index) + '</td>' + \
                           '<td><a class="four" href="http://127.0.0.1:5000/cereal/' + str(index) + '">''<strong>' + movie[NAME] + '</strong></a></td>' + \
                           '<td>' + str(movie[YEAR]) + '</td>' + \
                           '<td>' + str(movie[LENGTH]) + '</td>' + \
                           '<td>' + str(movie[RATING]) + '</td>' + \
                           '<td>' + str(movie[GENRES]) + '</td>' + \
                           '<td>' + str(movie[STAR]) + '</td>' + \
                           '<td>' + str(0.10 * (movie[FRIDAY_SALES] + movie[SATURDAY_SALES] + movie[SUNDAY_SALES])) + '</td>' + \
                           '</tr>'
        index += 1

    return (header + message_out + footer)

"""
NAME = 0
YEAR = 1
LENGTH = 2
RATING = 3
FRIDAY_SALES = 4
SATURDAY_SALES = 5
SUNDAY_SALES = 6
GENRES = 7
STAR = 8
IMAGE = 9
___________________________________________
5 Points - Professional-looking website
___________________________________________
"""

if __name__ == '__main__':
    app.run()