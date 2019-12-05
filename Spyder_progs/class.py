# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:17:15 2019

@author: Nazim Patham
"""

class categories :
    
    def __init__(self, name, no_of_item):
        self.name = name
        self.no_of_item = no_of_item
        
    def display_category(self):
        print("category Name:", self.cat_name)
        print("No. of items:", self.no_of_item)
#      
#    def add_category (self, name, no_of_item) :
#        self.name = name
#        add_item_in_category(no_of_item)
#    
##function for adding item in the category
#    def add_item_in_category(self, no_of_item) :
#        self.no_of_item = no_of_item
#        for i in range(0,no_of_item,1):
# 