# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 20:04:30 2014

@author: administrateur
"""

alph = 'abcdefghijklmnopqrstuvwxyz'

for c1 in alph:
        for c2 in alph:
            cT = c1 + c2
            if c1 < c2:
                print(cT)
