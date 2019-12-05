# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 18:02:24 2019

@author: Nazim Patham
"""

import threading
import time

class examplethread(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())
            
            
threadone = examplethread(name="one")
threadtwo = examplethread(name="two")

threadone.start()
time.sleep(1)
threadtwo.start()

print("Completed")