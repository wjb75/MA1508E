# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 17:00:27 2025

@author: wongj
"""

import sympy as sp

# Define the symbolic variable
t = sp.symbols('t')

# Define data points
data = [0, sp.Rational(1, 6), sp.Rational(1, 4), sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(2, 3)]
ndata = len(data)

# Define the function terms
f = [
    sp.cos(2 * sp.pi * t),
    sp.sin(2 * sp.pi * t),
    sp.cos(4 * sp.pi * t),
    sp.sin(4 * sp.pi * t),
    sp.cos(6 * sp.pi * t),
    sp.sin(6 * sp.pi * t)
]

# Define the function output values
b = sp.Matrix([
    -2,
    2 + 7 * sp.sqrt(3) / 2,
    7,
    1 - 3 * sp.sqrt(3) / 2,
    -4,
    1 + 3 * sp.sqrt(3) / 2
])

# Initialize an ndata x (number of terms) zero matrix A
A = sp.zeros(ndata, len(f))

# Loop through each data point and evaluate each term in f at t = data[i]
for k, val in enumerate(data):
    # Substitute t with the current data point in each function
    row = [expr.subs(t, val) for expr in f]
    # Assign the evaluated row into A (convert list to a 1xN Matrix row)
    A[k, :] = sp.Matrix([row])

# Form the augmented matrix [A | b]
R = A.row_join(b)
print("Augmented matrix [A | b]:")
sp.pprint(R)
print("\nReduced Row Echelon Form (rref) of [A | b]:")
R_rref, pivots = R.rref()
sp.pprint(R_rref)

