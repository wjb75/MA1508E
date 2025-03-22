# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 20:09:18 2025

@author: wongj
"""

import sympy as sp
import numpy as np
from sympy.core.numbers import Rational as r
A = sp.Matrix([[0,0,0,0,-1],[1,2,2,1,0],[4,5,6,3,6],[-2,-1,-2,-1,-2],[3,0,2,1,3]])
sp.pprint(f"A is \n")
sp.pprint(A)

sp.pprint("A.rref() = ")
sp.pprint(A.rref())
sp.pprint("the basis for col(A) is")
for i in A.rref()[1]:
    print(A.col(i))
    
print("They form a new matrix:")
sp.pprint(A[:,A.rref()[1]])

sp.pprint(A.nullspace())
sp.pprint(A.rowspace(simplify=True))

sp.pprint(sp.Matrix([r(3,4)]))# to represent exact rational