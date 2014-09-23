# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 15:56:48 2014

@author: administrateur
"""

import sys
if len(sys.argv) >= 3:
    print(int(sys.argv[1]) + int(sys.argv[2]))
else:
    print("usage: python3 solution.py OP1 OP2")
