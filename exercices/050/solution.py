# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 17:38:41 2014

@author: administrateur
"""
s = 0
for x in range(1000):
    if x/3 == 0:
        x = s + x
    if x/5 == 0:
        x = s + x
print(x)
