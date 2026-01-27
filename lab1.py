"""
=========================================================
Python Programming Lab – Lab 01
Subject : Advanced Python for Data Science

Student Name : Bibek Chand
Department   : BCT (III/I)
Roll No      : 5
Lab Title    : Introduction to Python Basics
=========================================================

OBJECTIVE:
1. To understand basic data types in Python
2. To learn loops and the range() function
3. To understand mutable and immutable data types
4. To use input() and type casting
5. To define and use functions

THEORY:
Python is a high-level, interpreted programming language
that is widely used in data science due to its simplicity
and powerful libraries.

Python supports various built-in data types.

Mutable data types:
- List
- Dictionary
- Set

Immutable data types:
- int
- float
- string
- tuple

The input() function always accepts data as a string.
Type casting is required to perform numerical operations.
"""

# --------------------------------------------------
# 1. BASIC DATA TYPES
# --------------------------------------------------

a = 10                  # int
b = 99.99               # float
c = 3 + 4j              # complex
s = "python"            # string
l = [4, 5, 6]           # list
t = (1, 2, 3)           # tuple
j = {1, 2, 3}           # set
i = True                # boolean
d = {"Name": "Bibek Chand", "Roll": 5}  # dictionary

print("Basic Data Types:")
print(a, b, c, s, l, t, j, i, d)

# --------------------------------------------------
# 2. LOOP THROUGH LIST
# --------------------------------------------------

print("\nElements of list:")
for item in l:
    print(item)

# --------------------------------------------------
# 3. RANGE FUNCTION
# --------------------------------------------------

print("\nEven numbers from 0 to 8:")
for num in range(0, 10, 2):
    print(num)

# --------------------------------------------------
# 4. TYPE CHECKING
# --------------------------------------------------

print("\nData Types:")
print(type(a))
print(type(b))
print(type(d))
print(type(t))

# --------------------------------------------------
# 5. INPUT FUNCTION
# --------------------------------------------------

name = input("\nEnter your name: ")
print(f"Hello {name}")

# --------------------------------------------------
# 6. TYPE CASTING
# --------------------------------------------------

x = input("\nEnter a number: ")
y = input("Enter another number: ")
print("Without type casting (string):", x + y)

m = int(input("Enter a number: "))
n = int(input("Enter another number: "))
print("With type casting (int):", m + n)

# --------------------------------------------------
# 7. FUNCTION EXAMPLE
# --------------------------------------------------

def area_rectangle(length, breadth):
    """
    This function calculates the area of a rectangle
    using length and breadth provided as parameters.
    """
    return length * breadth

print("\nArea of rectangle:", area_rectangle(4, 5))

"""
---------------------------------------------------------
DISCUSSION:
This experiment helped in understanding the core concepts
of Python programming such as data types, loops, user input,
type casting, and functions. These concepts form the base
for advanced topics in data science like NumPy, Pandas,
and machine learning.

RESULT:
All the programs were executed successfully and the
expected output was obtained.

CONCLUSION:
This lab provides a strong foundation in Python programming.
It enhances logical thinking and prepares students for
advanced data science and backend development tasks.
---------------------------------------------------------
"""
