import sqlite3
sqlite_file = 'SJSU_Organizations.sqlite'

conn = sqlite3.connect(sqlite_file)
cursor = conn.cursor()



'''
def insert_user_review(orgName,userReview,numReview):
    con = sql.connect ("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO user_review (orgName, userReview,numReview)")
    con.commit()
    con.close()
'''