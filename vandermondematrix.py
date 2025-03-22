# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 17:04:09 2025

@author: wongj
"""

import sympy as sp
import numpy as np

# -------------------------------
# Example 1: Quadratic Polynomial Fit
# Given data points (1,11), (2,16), (3,19)
# p(t) = a0 + a1*t + a2*t^2
# -------------------------------

# Data points
v = [1, 2, 3]
# Build Vandermonde matrix with columns corresponding to t^0, t^1, t^2
A = sp.Matrix([[t**i for i in range(len(v))] for t in v])
b = sp.Matrix([11, 16, 19])

print("Example 1: Quadratic Fit")
print("Vandermonde matrix A:")
sp.pprint(A)
print("\nVector b:")
sp.pprint(b)

# Augment and compute rref
R = A.row_join(b)
print("\nAugmented matrix [A | b]:")
sp.pprint(R)
R_rref, pivots = R.rref()
print("\nrref([A | b]) =")
sp.pprint(R_rref)

# -------------------------------
# Example 2: Exam Use (Degree-5 Polynomial)
# Using data points from t = 0 to 10 in steps of 2
# Data: [0, 2.9, 14.8, 39.6, 74.3, 119]
# p(t) = a0 + a1*t + a2*t^2 + a3*t^3 + a4*t^4 + a5*t^5
# -------------------------------

# Define parameters for data generation
start = 0
stop_inclusive = 10
step = 2
numberofelements = (stop_inclusive - start) // step + 1  # Should be 6

# Generate t values: [0, 2, 4, 6, 8, 10]
v2 = list(range(start, stop_inclusive + 1, step))

# Build the Vandermonde matrix for these points with increasing powers:
# Each row is [1, t, t^2, ..., t^5]
A2 = sp.Matrix([[t**i for i in range(numberofelements)] for t in v2])
# Data vector (function values)
data = sp.Matrix([0, 2.9, 14.8, 39.6, 74.3, 119])

print("\n\nExample 2: Degree-5 Polynomial Fit")
print("Vandermonde matrix A2:")
sp.pprint(A2)
print("\nData vector:")
sp.pprint(data)

# Form augmented matrix and compute rref
R2 = A2.row_join(data)
print("\nAugmented matrix [A2 | data]:")
sp.pprint(R2)
R2_rref, pivots2 = R2.rref()
print("\nrref([A2 | data]) =")
sp.pprint(R2_rref)

# Solve the system A2 * coeff = data
# This is analogous to MATLAB's A \ data
coeff = A2.LUsolve(data)
print("\nSolution for coefficients (ascending order):")
sp.pprint(coeff)

# MATLAB uses fliplr(coeff') to obtain coefficients in descending order.
# In Python, we reverse the list of coefficients.
coeff_list = list(coeff)           # [a0, a1, ..., a5]
coeff_list_desc = coeff_list[::-1]   # now [a5, a4, ..., a0]
print("\nCoefficients (descending order for polyval):")
print(coeff_list_desc)

# To evaluate the polynomial at t = 7.5 using NumPy's polyval,
# we need a numerical array of coefficients.
coeffs_numeric = [float(c) for c in coeff_list_desc]
value_at_7_5 = np.polyval(coeffs_numeric, 7.5)
print("\nPolynomial evaluated at t = 7.5:")
print(value_at_7_5)
