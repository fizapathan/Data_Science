# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 17:56:19 2019

@author: Nazim Patham
"""

import time
from threading import Thread

def backgroundprocess():
  print("thread one")
  time.sleep(3)
  print("thread two")
  
for i in range(20):
  t = Thread(target=backgroundprocess)
  t.start()