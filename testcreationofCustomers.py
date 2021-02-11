import sqlite3
import os
os.system('clear')

# SQLITE DATABASE INTO #

#creates a database if db does not exist
conn = sqlite3.connect('customer.db')

#the thing that goes and does stuff for us in the database; make a query, etc
# create a cursor
c = conn.cursor()


#create a table
'''
c.execute("""CREATE TABLE customer (
            first_name text, 
            last_name text,
            email text
            )""")
'''

#c.execute("INSERT INTO customer VALUES ('John','Elder','john@codemy.com')")

c.execute("SELECT * FROM customer")

items = c.fetchall()

for item in items:
    print(item[0] + ' last name: ' + item[1])

#commit changes
conn.commit()

#close database connection
conn.close()