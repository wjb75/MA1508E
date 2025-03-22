# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 16:55:00 2025

@author: wongj
"""


import sympy as sp
import numpy as np

# --- Code Block %2 ---
# Define symbolic variable 'a'
a = sp.symbols('a')

# Define matrices A, B, C
A = sp.Matrix([[0, -1, 0],
               [3, a, 1],
               [0, 0, -1]])
B = sp.Matrix([[2, 1, 3],
               [-1, a, 2],
               [0, -1, 0]])
C = sp.Matrix([[1, 2, 3],
               [1, a, 1],
               [3, 3, -1]])

# Calculate determinants
det_A = sp.det(A)
det_B = sp.det(B)
det_C = sp.det(C)
print("det(A) =", det_A)
print("det(B) =", det_B)
print("det(C) =", det_C)

# --- Code Block %5 ---
# Define matrix A for rref
A5 = sp.Matrix([
    [-1, 1, 1, 1, 0, 3, 5, 2, 1, 3],
    [ 1, 0, 2, 3, 1, 1, 3, 0, 2, 1],
    [ 3, 2, 3, 8, 5, 1, 7, 4, 3, 2],
    [ 0, 0, 3, 3, 1, 1, 6, 0, 4, 3]
])
rref_A5, pivots = A5.rref()
print("\nrref(A) =")
sp.pprint(rref_A5)

# --- Code Block %q6 ---
# Define symbolic matrix B for row operations
B_sym = sp.Matrix([
    [2,      2*a,  3,    2, 1],
    [1,  a - 1, 1 - a, a + 3, 0],
    [3,     -1, 4 - a, a + 2, 1],
    [-2, 2 - 2*a, -3,   a - 1, -1]
])

# Perform row operations (MATLAB uses 1-based indexing; Python uses 0-based)
# Swap row 0 and row 1:
B_sym.row_swap(0, 1)
# Row 1 = Row 1 - 2*Row 0
B_sym[1, :] = B_sym[1, :] - 2 * B_sym[0, :]
# Row 2 = Row 2 - 3*Row 0
B_sym[2, :] = B_sym[2, :] - 3 * B_sym[0, :]
# Row 3 = Row 3 + 2*Row 0
B_sym[3, :] = B_sym[3, :] + 2 * B_sym[0, :]
# Row 2 = Row 2 - Row 1
B_sym[2, :] = B_sym[2, :] - B_sym[1, :]
# Row 1 = Row 1 + Row 3
B_sym[1, :] = B_sym[1, :] + B_sym[3, :]

# Define a helper function to substitute specific values for 'a' and compute rref
def compute_B_rref(a_val):
    B_sub = B_sym.subs(a, a_val)
    rref_B, piv = B_sub.rref()
    return rref_B

# Evaluate for different values of a
for val in [0, 1, -0.5, -sp.Rational(3,5), 4, -3]:
    rref_result = compute_B_rref(val)
    print(f"\nrref(B) with a = {val} :")
    sp.pprint(rref_result)

# --- Code Block %8 ---
# Define matrices T, A, C, D and compute rref
T = sp.Matrix([
    [6, 12, 9, 9],
    [4, 8, 7, 7],
    [0, 0, 1, 1]
])
print("\nrref(T) =")
sp.pprint(T.rref()[0])

A8 = sp.Matrix([
    [4, 8, 8, 8],
    [0, 0, -1, -1],
    [-6, -12, -10, -10]
])
print("\nrref(A) =")
sp.pprint(A8.rref()[0])

C8 = sp.Matrix([
    [2, 4, 1, 1],
    [12, 20, 16, 16],
    [10, -20, -16, 16]
])
print("\nrref(C) =")
sp.pprint(C8.rref()[0])

D8 = sp.Matrix([
    [10, 20, 17, 17],
    [2, 4, 2, 2],
    [4, 8, 6, 6]
])
print("\nrref(D) =")
sp.pprint(D8.rref()[0])

# --- Code Block %9 ---
# Define symbolic variables a and b, then matrix R
a, b = sp.symbols('a b')
R = sp.Matrix([
    [1, 2, -3, 5, b],
    [0, a - 3, 1, 3, 2],
    [0, 0, b - 2, a, 1],
    [0, 0, 0, 1, 7],
    [0, 0, 0, 0, a + 1]
])
# Row 1 = Row 1 / 2 (Python row index 1)
R[1, :] = R[1, :] / 2
# Swap rows 2 and 4 (indices 2 and 4)
R.row_swap(2, 4)
# Row 3 = Row 3 + 2*Row 1 (index 3)
R[3, :] = R[3, :] + 2 * R[1, :]
print("\ndet(R) =", sp.det(R))

# --- Code Block %10 ---
# Define matrices A, B, C, D with symbolic variable a
A10 = sp.Matrix([
    [2, 1, 2],
    [-1, 1, 0],
    [0, -3, a]
])
B10 = sp.Matrix([
    [0, 2, 2],
    [1, 0, 3],
    [0, 1, a]
])
C10 = sp.Matrix([
    [1, 0, 3],
    [-1, 1, 0],
    [-1, 0, a]
])
D10 = sp.Matrix([
    [-1, 1, 0],
    [1, -1, 2],
    [3, 1, a]
])
print("\ndet(A) =", sp.det(A10))
print("det(B) =", sp.det(B10))
print("det(C) =", sp.det(C10))
print("det(D) =", sp.det(D10))

