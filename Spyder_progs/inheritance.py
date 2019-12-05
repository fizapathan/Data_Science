# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:35:03 2019

@author: Nazim Patham
"""
from items import items_class
from category_banao import categories
from category_banao import sub_category

#
#class main:
def category_check() :
    d_category = input("Enter the category name in which you want to add subcategories: ")
    for cat in categories_list :
        if cat.cat_name == d_category :
            return 0
        else :
            return  1
            
#add items or subcategories in the lists

def overwrite() :
    cat.item_list = []
    n = (int)(input("Enter no. of categories/subcategories: "))
    for i in range (0, n, 1) :
        subcat_obj = sub_category(input("Enter the name of subcategory: "), (int)(input("Enter no. of items: ")), [], input("Enter msg: "))
        cat.item_list.append(subcat_obj)

def add_specified_number_of_subcat():
    no = (int)(input("Enter the number of subcategories you want to add: "))
    for i in range(0, no, 1) :
        cat.no_of_item += 1
        new_subcat_obj = sub_category(input("Enter the new subcategory: "), (int)(input("Enter the no. of items: ")), [], input("Enter the message: "))
        cat.item_list.append(new_subcat_obj)

def add_item() :
    d_category = input("Enter the name of the category:")
    for cat in categories_list :
        if cat.cat_name == d_category :
            d_subcategory = input("Enter the name of the subcategory: ")
            for subcat in cat.item_list:
                if subcat.cat_name == d_subcategory :
                    n = (int)(input("Enter the no. of items you want to add: "))
                    for i in range(0, n, 1) :
                        subcat.no_of_item += 1
                        itm_obj = items_class(input("Enter the name of item: "), (int)(input("Enter th price: ")))
                        subcat.item_list.append(itm_obj)
    
#list of the items in music category
list_music_traditional = [items_class("Tabla", 300), items_class("Sitaar", 800)]
list_music_modern = [items_class("flute", 100), items_class("keyboard", 1000)]
#list of the items in electronics category
list_elect_lappy = [items_class("Keyboard", 400), items_class("Mouse", 100), items_class("CPU", 6000), items_class("Webcam", 3000)]
list_elect_tv= [items_class("LED", 40000), items_class("OLED", 100000), items_class("Curved Display LED", 300000)]

#messages for the music category
msg_music_traditional = "Traditional musical instruments used since the age of lord Rama"
msg_music_modern = "Modern nusical instruments"
#messages for the electronics category
msg_elect_lapyy = "All the Laptop accessories are not available:p"
msg_elect_tv = "Yaha wo milega jo kahi nahi milta"

subcategories_music = [sub_category("traditional", 2, list_music_traditional, msg_music_traditional ), sub_category("modern", 2, list_music_modern, msg_music_modern)]
subcategories_elect = [sub_category("Laptop accessories", 4, list_elect_lappy, msg_elect_lapyy ), sub_category("T.V", 3, list_elect_tv, msg_elect_tv )]

categories_list = [categories("Music", 2, subcategories_music), categories("Electronics", 2, subcategories_elect)]

 
choice = 1

while choice != 0:

    print("Categories: ")
    for cat in categories_list :
        print("Here comes the details: ", cat.display_category())
        for subcat in  cat.item_list:
            print("Here comes subcategories: ", subcat.display_category())
        
    
    choice = (int)(input("""\nPress 1 to display items of the existing categories
             \nPress 2 to add new categorry
             \nPress 3 to add new subcategory
             \nPress 4 to add items to the existing subcategories
             \nPress 5 to delete a category
             \nPress 6 to delete a subcategory
             \nPress 7 to delete an item from a subcategory
             \nPress 8 to update the price of any item
             \nPress 0 to exit\n  ->"""))
    
    if choice == 1 :
        d_category = input("Enter the name of the category:")
        for cat in categories_list :
            if cat.cat_name == d_category :
                d_subcategory = input("Enter the name of the subcategory: ")
                for subcat in cat.item_list:
                    if subcat.cat_name == d_subcategory :
                        for itm in subcat.item_list :
                            print("Items: ", itm.display_item())
                        break
                else :
                    print("this subcategory doesn't exist!")
                    break
            break
        else :
            print("This category doesn't exists!")
            break
            
            
    elif choice == 2 :
        new_category = input("Enter the name of new category: ")
        for cat in categories_list :
            if cat.cat_name == new_category :
                ch = input("This cat already exists, would you like to (a.)add a new subcategory to it  (b.)rewrite it? ")
                if ch == 'a' :
                    add_specified_number_of_subcat()
                    
                elif ch  == 'b' :
                    overwrite()
                break
                                        
        else :
            n = (int)(input("Enter no. of subcategories: "))
            list_of_subcat= []
            for i in range (0, n, 1) :
                subcat_obj = sub_category(input("Enter the name of subcategories: "), (int)(input("Enter no. of items: ")), [], input("Enter the message: "))
                list_of_subcat.append(subcat_obj)

            
            cat = categories(new_category, n, list_of_subcat)
            categories_list.append(cat) 
    
    
    elif choice == 3:
        d_category = input("Enter the category name in which you want to add subcategories: ")
        for cat in categories_list :
            if cat.cat_name == d_category :
                add_specified_number_of_subcat()
                break
        else :
            print("This category doesn't exist!")
            break
        
            
    elif choice == 4 :
        add_item()
        
        
    elif choice == 5 :
        d_category = input("Enter the category name which you want to delete: ")
        for cat in categories_list :
            if cat.cat_name == d_category :
                del cat.item_list
                categories_list.remove(cat)
                break
        else :
            print("This category doesn't exist!")
            break
                
                
    elif choice == 6 :
        d_category = input("Enter the category name: ")
        for cat in categories_list :
            if cat.cat_name == d_category :
                d_subcategory = input("Enter the name of the subcategory to be deleted: ")
                for subcat in cat.item_list:
                    if subcat.cat_name == d_subcategory :
                        del subcat.item_list
                        cat.item_list.remove(subcat)
                        break
                else :
                    print("This subcategory doesn't exist!")
                    break
                break
            
        else :
            print("This category does't exist!")
            break
                
    elif choice == 7 :
        d_category = input("Enter the category name: ")
        for cat in categories_list :
            if cat.cat_name == d_category :
                d_subcategory = input("Enter the name of the subcategory to be deleted: ")
                for subcat in cat.item_list:
                    if subcat.cat_name == d_subcategory :
                        d_item = input("Enter the name of the item to be deleted: ")
                        for itm in subcat.item_list :
                            if itm.item_name == d_item :
                                subcat.item_list.remove(itm)
                                break
                        else :
                            print("This item doesn't exist!")
                            break
                        break
                    
                else :
                    print("This subcategory doesn't exist!")
                    break
                break
            
        else :
            print("This category doesn't exist!")
            break


    elif choice == 8 :
        d_category = input("Enter the category name: ")
        for cat in categories_list :
            if cat.cat_name == d_category :
                d_subcategory = input("Enter the name of the subcategory to be deleted: ")
                for subcat in cat.item_list:
                    if subcat.cat_name == d_subcategory :
                        d_item = input("Enter the name of the item to be deleted: ")
                        for itm in subcat.item_list :
                            if itm.item_name == d_item :
                                new_price = (int)(input("Enter the new price: "))
                                itm.price = new_price
                                break
                        else :
                            print("This item doesn't exist!")
                            break
                        break
                    
                else :
                    print("This subcategory doesn't exist!")
                    break
                break
            
        else :
            print("This category doesn't exist!")
            break

