# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:32:45 2019

@author: the607
"""

import sqlite3


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
