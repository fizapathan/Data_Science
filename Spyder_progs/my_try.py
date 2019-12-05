# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:52:31 2019

@author: Nazim Patham
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May  4 15:24:30 2019

@author: Fiza Patham
"""

#function for adding item in the category
def add_item_in_category(t_dictionary) :
    y = (int)(input("Number of items? "))

    for i in range(0,y,1):

        t_dictionary[input("name: ")] = int(input("price: "))

    listOfCategories.append(t_dictionary)

    categories[x] = y
    
    
#manually entered categories    
sports = {

    "name": "sports",

    "s1":10,

    "s2":20,

    "s3":30,

    "s4":20,

    "s5":30

}

 

babies = {

    "name": "babies",

    "b1":100,

    "b2":200,

    "b3":300,

    "b4":250

}

 

musicals = {

    "name": "musicals",

    "m1":60,

    "m2":70,

    "m3":80

}

 

# putting all the dictionaries together in a tuple

listOfCategories = [babies, sports, musicals]

 

# initializing categories dictionary

categories ={}

 

for i in listOfCategories:

    categories[i["name"]] = len(i) - 1

 

x = 1

 

while x != 0:

 

    # printing categories

    print("Total Categories:",len(listOfCategories))

    for key in categories.keys():

        print("Category:",key,":: Items:",categories[key])

 

    # taking user input

    x = (int)(input("Press 1 for item details in categories\nPress 2 for adding a new category\nPress 3 to add new items\nPress 4 to delete a category\nPress 0 to exit\n->"))

 

    if x == 1:

        # printing details of a category

        x = input("Please enter the name of the catgory: ")

        i = 0

        while x != listOfCategories[i]['name']:

            i += 1

        else:

            print("ITEM\t\tPRICE")

            print("----\t\t-----")

            for key in listOfCategories[i].keys():

                if key == "name":

                    continue

                print(key + "\t\t\t" + (str)(listOfCategories[i][key]))

    elif x == 2:

        # adding a new category

        x = input("Please enter the name of the catgory: ")

        for category in listOfCategories:

            if category["name"] == x:

                ch = input("This category already exists, would you like to overwrite it? (y/n):")
                
                #overwrite the category
                if ch == 'y' :
                    category.clear()
                    category["name"] = x
                    add_item_in_category(category)
                    break
                    
                #leave the existing category as it is
                elif ch == 'n' :
                    break
                
                else :
                    print("try again\n")
            
        else:

            temp_dictionary = {

                "name":x

            }
            
            add_item_in_category(temp_dictionary)

    elif x == 3 :
        x = input("Please enter the name of the category: ")
        for category in listOfCategories:
            if category["name"] == x :
                add_item_in_category(category)
                break
            
    elif x == 4 :
        x = input("Please enter the name of the category: ")
        for category in listOfCategories:
            if category["name"] == x :
                del category
        