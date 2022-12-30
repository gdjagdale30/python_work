#Import sqlite library
import sqlite3
#Create connction to connect database
con=sqlite3.connect("tutorial.db")
#Create connction to cursor
cur=con.cursor()

# # cur.execute("Create Table movie (title,year,score)")

# res=cur.execute("Select name from sqlite_master")

# print(res.fetchone())

# cur.execute("""Insert into movie values 
# ('Monty Python and the Holy Grali',1975,8.2),
# ('Circus',1978,8.7),
# ('Avatar',1976,8.5),('Terminator',1974,4.9)
# """)

# con.commit()

# res=cur.execute("Select score From movie")
# a=res.fetchall()
# print(a)

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()

res=cur.execute("Select * From movie")
a=res.fetchall()
print(a)

for row in cur.execute("Select year,title from movie Order By year"):
    print(row)