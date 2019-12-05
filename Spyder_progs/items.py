# -*- coding: utf-8 -*-
"""
Created on Mon May  6 12:20:54 2019

@author: Nazim Patham
"""

class items_class :
    def __init__(self, name, price):
        self.item_name = name
        self.price = price
        
    def display_item(self) :
        return {self.item_name, self.price}
