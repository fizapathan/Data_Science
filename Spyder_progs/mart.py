# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:07:58 2019

@author: Fiza Patham
"""

babies = {
        "Clothes" : 300,
        "Diper" : 30,
        "Bottle" : 30,
        }

sports = {
        "Clothes" : 600,
        "Shoes" : 800,
        "Fitness band" : 1250,
        "Badminton Racket" : 200,
        "Basket ball" : 200,
        "Hockey Stick" :300
        }


music = {
        "Guitar" : 3000,
        "Keyboard" : 2000,
        "Flute" : 200,
        "Tabla" : 2000
        }

electronics = {
        "Keyboard" : 800,
        "Mouse" : 300
        }

categories = {
        "Babies" : 3,
        "Sports" : 5,
        "Music" : 4,
        "Electronics" : 5
        }

flag = 1

while flag==1 :
    print("Do you want to: 1.Print Categories 2.Add categories 3.Exit")
    choice = input("Enter choice: ")

    if (choice==1) :
        print("Below are categories: ")
        print(categories.keys())
"""
    elif (choice==2) :
        new_category = input("Enter the name of the category: ")
        no_of_items = input("Enter the number of items in ",new_category)
        categories.update(new_category,no_of_items)
        new_category = {}
        for i in no_of_items : 
            new_item = input("Enter item",i)
            new_item_price = input("Enter the price of ",new_item)
            new_category.update(new_item, new_item_price)

    elif (choice==3) :
        flag = 0

        
"""