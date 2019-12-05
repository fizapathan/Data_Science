# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:17:15 2019

@author: Nazim Patham
"""

class categories :
    #main categories of the store
    def __init__(self, name, no_of_item, item_list):
        self.cat_name = name
        self.no_of_item = no_of_item
        self.item_list = item_list
        
    def display_category(self):
        return (self.cat_name, self.no_of_item)
#    def check_cat_existance(self, cat_list) :
#        for cat in cat_list :
#            if in_cat == cat
#      
        
        
        
class sub_category (categories) :
    #subcategory inherited from categories
    def __init__(self, name, no_of_subcat, subcat_list, msg) :
        categories.__init__(self, name, no_of_subcat, subcat_list)
        self.msg = msg
        
        
    def display_category(self):
        return ( 
                categories.display_category(self),
                self.msg
                )
        