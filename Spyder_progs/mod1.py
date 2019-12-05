# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:35:03 2019

@author: Nazim Patham
"""
from items import items_class
from category_banao import categories
from category_banao import sub_category


try:    
    def category_check(category, ctg_lst) :
        for cat in ctg_lst :
            if cat.cat_name == category :
                return 0

    list_music = [items_class("Tabla", 300), items_class("Sitaar", 800), items_class("flute", 100), items_class("keyboard", 1000)]
    list_elect = [items_class("Keyboard", 400), items_class("Mouse", 100), items_class("CPU", 6000), items_class("Webcam", 3000), items_class("LED", 40000), items_class("OLED", 100000), items_class("Curved Display LED", 300000)]
    
#    subcategories_music = [sub_category("traditional", 2, list_music_traditional,"Traditional musical instruments used since the age of lord Rama"), sub_category("modern", 2, list_music_modern)]
#    subcategories_elect = [sub_category("Laptop accessories", 4, list_elect_lappy, "All the Laptop accessories are not available:p"), sub_category("T.V", 3, list_elect_tv, "Yaha wo milega jo kahi nahi milta")]

    categories_list = [categories("Music", 2, list_music), categories("Electronics", 2, list_elect)]

 
    choice = 1
    
    while choice != 0:


        print("Categories: ")
        for cat in categories_list :
            cat.display_category()
        
        choice = (int)(input("""\nPress 1 to display items of the existing categories
                 \nPress 2 to add new categories
                 \nPress 3 to add items to the existing categories
                 \nPress 4 to delete a category
                 \nPress 5 to delete an item from a category
                 \nPress 6 to update the price of any item
                 \nPress 0 to exit\n  ->"""))
        
        if choice == 1 :
            d_category = input("Enter the name of the category:")
            for cat in categories_list :
                if cat.cat_name == d_category :
                    for itm in cat.item_list:
                        itm.display_item()
                        
                    break
                
            else :
                print("This category doesn't exists!")
                
                
        elif choice == 2 :
            new_category = input("Enter the name of new category: ")
            for cat in categories_list :
                if cat.cat_name == new_category :
                    ch = input("This cat already exists, would you like to rewrite it? y/n")
                    if ch == 'y' :
                        cat.item_list = []
                        n = (int)(input("Enter no. of items: "))
                        #list_of_item = []
                        for i in range (0, n, 1) :
                            itm_obj = items_class(input("Enter the name of item: "), (int)(input("Enter Price: ")))
                            cat.item_list.append(itm_obj)
                        
                        #cat.item_list = list_of_item
                    break
                        
                        
            else :
                n = (int)(input("Enter no. of items: "))
                list_of_item = []
                for i in range (0, n, 1) :
                    itm_obj = items_class(input("Enter the name of item: "), (int)(input("Enter Price: ")))
                    list_of_item.append(itm_obj)
    
                
                cat = categories(new_category, n, list_of_item)
                categories_list.append(cat)
                
                
        elif choice == 3 :
            d_category = input("Enter the name of the category:")
            for cat in categories_list :
                if cat.cat_name == d_category :
                    n = (int)(input("No. of items:"))
                    for i in range (0, n, 1) :
                        itm_obj = items_class(input("Enter the name of item: "), (int)(input("Enter Price: ")))
                        cat.item_list.append(itm_obj)
                    break
                
                else :
                    print("This category doesn.t exist!")
            cat.no_of_item += n
        elif choice == 4 :
            d_category = input("Enter the name of the category:")
            for cat in categories_list :
                if cat.cat_name == d_category :
                    categories_list.remove(cat)
                    
            else :
                print("Cat doesn't exist")
                    
        elif choice == 5 :
            d_category = input("Enter the name of the category:")
            for cat in categories_list :
                if cat.cat_name == d_category :
                    itm = input("Enter the item name: ")
                    for itm_obj in cat.item_list :
                        if itm == itm_obj.item_name :
                            cat.item_list.remove(itm_obj)
                            break
                    else:
                        print("This item doesn't exist")
                    break
            else :
                print("This category does't exist")
                
                
        elif choice == 6:
            d_category = input("Enter the name of the category:")
            for cat in categories_list :
                if cat.cat_name == d_category :
                    itm = input("Enter the item name: ")
                    for itm_obj in cat.item_list :
                        if itm == itm_obj.item_name :
                            new_price = (int)(input("Enter the new price: "))
                            if(new_price>0) :
                                itm_obj.price = new_price
                            else :
                                print("Invalid price entered")
                            break
                    break
                
            else :
                print("cat doesn't exist")
                
        elif choice>6 or choice<0 :
            print("Wrong choice entered, try again.")
            
            
            
except :
    print("Oops! An exception occured")