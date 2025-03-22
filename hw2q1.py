# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 10:09:44 2025

@author: wongj
"""

import sympy as sp
from sympy import pprint
import numpy as np
A = sp.Matrix([[1,0,1,10,7,3,2],[0,1,-3,2,3,-2,1],[0,-1,3,2,3,2,-1,],[1,2,-5,6,7,-1,4,]])

pprint("A is ")
pprint(A)

pprint("rref(A) = ")
pprint(A.rref(pivots = True))
              
        