# -*- coding: utf-8 -*-
"""
Created on Sun May 12 11:54:14 2019

@author: Nazim Patham
"""

import sqlite3 as lite

def creat() :
    con = lite.connect('new_item_db.db')
    cur = con.cursor()    
    cur.execute("CREATE TABLE items(item_id INT, item_name TEXT, price INT)")
    
    
def insert():
    con = lite.connect('new_item_db.db')    
    cur = con.cursor()    

    idn = (int)(input("Enter the item id: "))
    name = input("Enter the item name: ")
    price = (int)(input("Enter the price: "))
    cur.execute("INSERT into items VALUES(?, ?, ?)", (idn, name, price))
#    cur.execute("INSERT into items VALUES('%d', '%s', '%d')" %(idn, name, price))
    cur.close()


def show():
    con = lite.connect('new_item_db.db')
    cur = con.cursor()    
    cur.execute("SELECT *FROM items")
    record = cur.fetchall()
    for i in record:
        print(i)
    con.close()
    


#creat()
insert()
show()    