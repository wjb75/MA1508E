# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 17:12:16 2025

@author: wongj
"""

from sympy import *
import numpy as np
a = symbols("a")
U = Matrix([[5,2,5,4],[5,5,6,6],[4,5,3,6],[7,7,6,9],[-2,-3,-3,-3]])
pprint(U)

V   = Matrix ([[3,0,5],[4 ,-1 ,6],[3 ,1 ,1],[5,1,4,],[-2,1,-2]])
pprint(f"V is {V}")

UlV = U.row_join(V)
pprint(UlV.rref())

VlU = V.row_join(U)
pprint(VlU.rref())

u1 = Matrix([5,5,4,7,-2])
v3 = Matrix([5,6,1,4,-2])

pprint(p:= u1+v3)
pprint(U.row_join(p).rref())
pprint(V.row_join(p).rref())

W = Matrix([[-3,4,1],[0,7,7,],[1,5,6,],[0,8,8],[-1,-4,-5]])
pprint(W)

UlW = U.row_join(W)
pprint(UlW)


pprint(UlW.rref())
WlU = W.row_join(U)
pprint(WlU.rref())
#print(type((WlU.rref()[0][2,5])))

Su = U[:,(0,1,2,)]
pprint(Su)
Coeff = Su.row_join(-V).row_join(Matrix([0 ,0,0,0,0]))
pprint(Coeff)

# Coeff.LUsolve(Matrix([0,0,0,0,0])) #cannot becuz underdetermined

pprint(Coeff.rref())


pprint((np.sum(Su, axis=1))/4)
pprint(Su[:,0]-Su[:,2])


#test, unrelated
A = U = Matrix([[a,a,a,a],[5,5,6,6],[4,5,3,6],[7,7,6,9],[-2,-3,-3,-3]])
pprint(A)
pprint(type(B:=(np.sum(A, axis=1))))
pprint(B)
pprint(Matrix(B))
pprint(type(Matrix(B)[0]))
print(Mul(2,3))
print(A.rref())