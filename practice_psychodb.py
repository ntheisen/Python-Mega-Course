# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:59:49 2019

@author: the607
"""

import mysql.connector

def create_table():
    conn = sqlite3.connect('lite.db')  #creates a file if not present
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT,quantity INTEGER,price FLOAT)")
    conn.commit()
    conn.close()


def insert_sql(item, qty, price):
    conn = sqlite3.connect('lite.db')  #creates a file if not present
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, qty, price))
    conn.commit()
    conn.close()
    
def view_table():
    conn = sqlite3.connect('lite.db')  #creates a file if not present
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete_row(item):
    conn = sqlite3.connect('lite.db')  #creates a file if not present
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))  #comma is needed when only 1 item
    conn.commit()
    conn.close()

def update_row(qty, price, item):
    conn = sqlite3.connect('lite.db')  #creates a file if not present
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (qty, price, item))  
    conn.commit()
    conn.close()

update_row(11, 6, 'Coffee Cup')
#insert_sql('Coffee Cup', 10, 5)
delete_row('Wine Glass')

print(view_table())



import mysql.connector
word = input("Enter a word in English and press Enter: ")
con = mysql.connector.connect(
    user="ardit700_student", 
    password = "ardit700_student", 
    host="108.167.140.122", 
    database = "ardit700_pm1database"
)
cursor = con.cursor()
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()
if results:
    for result in results:
        print(result[1])
else:
    print("We couldn't find any results about that.")