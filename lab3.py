"""
=========================================================
Python Programming Lab – Lab 03
Subject : Advanced Python for Data Science

Student Name : Bibek Chand
Department   : BCT (III/I)
Roll No      : 5
Lab Title    : NumPy Basics
=========================================================

OBJECTIVE:
1. To understand NumPy arrays and their advantages
2. To perform basic array operations
3. To understand array indexing and slicing
4. To use mathematical functions on arrays
5. To explore multi-dimensional arrays

THEORY:
NumPy is a Python library for numerical computations.
- Provides efficient arrays
- Supports vectorized operations
- Essential for data science and machine learning
"""

import numpy as np

# -------------------------
# Creating Arrays
# -------------------------
print("\n--- Creating Arrays ---")
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([[1, 2], [3, 4]])

print("1D array:", arr1)
print("2D array:\n", arr2)

# -------------------------
# Array Operations
# -------------------------
print("\n--- Array Operations ---")
print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Max:", np.max(arr1))
print("Min:", np.min(arr1))

# -------------------------
# Indexing and Slicing
# -------------------------
print("\n--- Indexing and Slicing ---")
print("First element of arr1:", arr1[0])
print("Last row of arr2:", arr2[-1, :])

# -------------------------
# Mathematical Operations
# -------------------------
print("\n--- Mathematical Operations ---")
arr3 = arr1 * 2
arr4 = arr1 + arr3
print("arr1 * 2:", arr3)
print("arr1 + arr3:", arr4)

# -------------------------
# Multi-dimensional arrays
# -------------------------
print("\n--- Multi-dimensional Arrays ---")
arr5 = np.arange(1, 13).reshape(3, 4)
print(arr5)

"""
RESULT:
All NumPy operations executed successfully.
Arrays created, sliced, and manipulated as expected.

CONCLUSION:
NumPy simplifies numerical computations in Python.
It is efficient and essential for data science tasks.
Multi-dimensional arrays help handle complex datasets easily.
"""
