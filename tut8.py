# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 15:30:50 2025

@author: wongj
"""

import sympy as sp

v1 = sp.Matrix([1,2,-1])
sp.pprint(v1)
v2 = sp.Matrix([1,0,1])
sp.pprint(v2)

sp.pprint(v1.dot(v2))


#2a
w1 = sp.Matrix([1,1,1,1,1])
w2 = sp.Matrix([1,2,-1,-2,0])
w3 = sp.Matrix([1,-1,1,-1,0])
M = w1.row_join(w2).row_join(w3)

sp.pprint(M.rref())



print(w1.dot(w2), w2.dot(w3), w3.dot(w1))

sp.pprint(Mt := M.transpose().row_join(sp.Matrix([0,0,0])).rref(pivots = False))
M0 = M.transpose().nullspace()
M0m = M0[0].row_join(M0[1])
sp.pprint(M0)
sp.pprint(w1n := w1.normalized())
sp.pprint(w2n := w2.normalized())
sp.pprint(w3n := w3.normalized())
v = sp.Matrix([2,0,1,1,-1])
vp = (v.dot(w1n))*w1n + (v.dot(w2n))*w2n + (v.dot(w3n))*w3n
sp.pprint(vp)
sp.pprint(v-vp)
sp.pprint(M0m.row_join(v-vp).rref())

#3

u1 = sp.Matrix([1,2,2,-1])
u2 = sp.Matrix([1,1,-1,1])
u3 = sp.Matrix([-1,1,-1,-1])
u4 = sp.Matrix([-2,1,1,2])

sp.pprint(u1.dot(u2))
sp.pprint(u1.dot(u3))
sp.pprint(u1.dot(u4))
sp.pprint(u3.dot(u2))
sp.pprint(u4.dot(u2))
sp.pprint(u4.dot(u3))

sp.pprint(u1n := u1.normalized())
sp.pprint(u2n := u2.normalized())
sp.pprint(u3n := u3.normalized())
sp.pprint(u4n := u4.normalized())
normset= [u1n,u2n,u3n,u4n]
sp.pprint(normset)

S  = u1.row_join(u2).row_join(u3).row_join(u4)
T =  u1n.row_join(u2n).row_join(u3n).row_join(u4n)

v = sp.Matrix([0,1,2,3])
sp.pprint(S.row_join(v).rref())
sp.pprint(T.row_join(v).rref())


#4a

u1 = sp.Matrix([1,1,1,1])
u2 = sp.Matrix([1 ,-1,1,0])
u3 = sp.Matrix([1 , 1,-1,-1])
u4 = sp.Matrix([1 ,2,0,1])
sp.pprint(u1)
sp.pprint(u2)
v1 = u1
print(v1.norm()**2, u2.dot(v1))
v2 = u2 - (u2.dot(v1)/(v1.dot(v1))) * v1
sp.pprint(v2)

v3 = u3 - (u3.dot(v1)/(v1.dot(v1))) * v1 - (u3.dot(v2)/(v2.dot(v2))) * v2
sp.pprint(v3)
v4 = u4 - (u4.dot(v1)/(v1.dot(v1))) * v1 - (u4.dot(v2)/(v2.dot(v2))) * v2 - (u4.dot(v3)/(v3.dot(v3))) * v3
sp.pprint(v4)
# sp.pprint((u4.dot(v1)/(v1.dot(v1))) * v1)
# sp.pprint((u4.dot(v2)/(v2.dot(v2))) * v2)
# sp.pprint((u4.dot(v3)/(v3.dot(v3))) * v3)
print("after normalization")
sp.pprint(v1n := v1.normalized())
sp.pprint(v2n := v2.normalized())
sp.pprint(v3n := v3.normalized())
sp.pprint(v4n := v4.normalized())

#4b
u1 = sp.Matrix([1,2,2,1])
u2 = sp.Matrix([1 ,2,1,0])
u3 = sp.Matrix([1 ,0,1,0])
u4 = sp.Matrix([1 ,0,2,1])
sp.pprint(u1)
sp.pprint(u2)
v1 = u1
print(v1.norm()**2, u2.dot(v1))
v2 = u2 - (u2.dot(v1)/(v1.dot(v1))) * v1
sp.pprint(v2)

v3 = u3 - (u3.dot(v1)/(v1.dot(v1))) * v1 - (u3.dot(v2)/(v2.dot(v2))) * v2
sp.pprint(v3)
v4 = u4 - (u4.dot(v1)/(v1.dot(v1))) * v1 - (u4.dot(v2)/(v2.dot(v2))) * v2 - (u4.dot(v3)/(v3.dot(v3))) * v3
sp.pprint(v4)

print("after normalization")
sp.pprint(v1n := v1.normalized())
sp.pprint(v2n := v2.normalized())
sp.pprint(v3n := v3.normalized())
sp.pprint(v4n := v4.normalized())

#q3
A = sp.Matrix([[0,1,1,0],[1,-1,1,-1],[1,0,1,0],[1,1,1,1]])
b = sp.Matrix([6,3,-1,1])

sp.pprint(A.row_join(b).rref())
At = A.transpose()

sp.pprint(A)
sp.pprint(At)
sp.pprint((At*A).row_join(At*b))

sp.pprint((At*A).row_join(At*b).rref())

s = sp.symbols('s')
u = sp.Matrix([-6-s,-1-s,7+s, s])
sp.pprint(u)

sp.pprint(A*u)