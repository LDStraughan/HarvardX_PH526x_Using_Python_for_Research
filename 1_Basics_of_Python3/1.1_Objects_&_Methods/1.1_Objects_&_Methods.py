#####################
# 1.1.1 PYTHON BASICS
#####################
# Interpreted Language = able to run program without need to first link/compile them (Python is interpreted language)

# Python had 2 different modes:
#       1) Interactive -  experimenting code (one line/expression at a time - if task is more challenging)
#       2) Standard - run programs from start to finish (if task is easy)

# Python is named after Monty Python

# A Python Distribution consists of the core Python package and hundreds of other modules working together

# Jupyter & Spyder = development environments

# Python 2 is a legacy language
# Python 3 is present & future of language

# Python 3 is not backwards compatible with 2

############################
# 1.1.1 PYTHON BASICS - Quiz
############################
# Question 1: Python has two operating modes. Which are they?
# Solution 1: Both of the above

# Question 2: Which version of Python will we focus on in this course?
# Solution 2: Python 3

# Question 3: Which of the following statements is NOT correct?
# Solution 3: Python 2 code will always work with Python 3.

###############
# 1.1.2 OBJECTS
###############
# Mutable = objects whose value can change (dictionaries, lists, etc.)
# Immutable = objects whose value cannot change after being created (strings, tuples, etc.)

# 'Import' statement imports modules

# Each object has 3 characteristics:
#       1) Type - number, strings, list, etc.
#       2) Value - data value contained in object
#       3) Identity - each object has a distinct identity number

# Attributes = data/function associated with objects
# Name of attribute follows name of object (separated by .)
# Two types of Attributes:
#       1) Data Attribute - value attached to an object
#       2) Method - function attached to an object (performs an operation/function on the object)

# Depending on the type of object, different methods are available

# Instance = one occurrence of an object

# Data Attribute vs Method:
import numpy as np
x = np.array([1, 3, 5])  # Array = object containing multiple values
y = np.array([1, 5, 9])
## Method:
x.mean()  # Mean = a method (in this case, connected to object x)
y.mean()  # Parenthesis following name of attribute because 'mean' is a function
## Data Attribute:
x.shape  # How many numbers are in object
y.shape  # No parenthesis following name of attribute because 'shape' is a data attribute

######################
# 1.1.2 OBJECTS - Quiz
######################
# Question 1: Python has immutable objects (e.g., strings and tuples) and mutable objects (e.g., dictionaries and
# lists). What does it mean for an object to be immutable? Solution 1: Its contents cannot be modified by the
# programmer after the object has been created.

# Question 2: Consider the following line of code:
x = 4  # In this assignment, what does the number 4 represent?
# Solution 2: The object value.

# Question 3: What is the difference between methods and data attributes of objects?
# Solution 3: Methods are functions associated with objects, whereas data attributes are data associated with objects.

#########################
# 1.1.3 MODULES & METHODS
#########################
import math
math.pi # value of pi
math.sqrt(10) # square root function
math.pi/2 # divide pi by 2
math.sin(math.pi/2) # sin of pi divided by 2

from math import pi # import just the value of pi from the math library

# Namespace = container of names shared by objects that usually go together - prevents naming conflicts

# Example of namespace:
import numpy as np
np.sqrt # numpy also has a square root function
math.sqrt(2)
np.sqrt(2)
# These two functions look the same but they exist in different namespaces
# numpy can do things math can't
np.sqrt([2, 3, 4]) # numpy can create an array and find the sqrt of all numbers simultaneously
math.sqrt([2, 3, 4]) # math can't do it with a list

# 3 things happen when we import
#       1) Python creates a new namespace for all objects in module
#       2) Python executes module code
#       3) Python creates a name to reference the namespace object

name = "Amy" # Defining a Python string - create an object containing this name
type(name) # Type function tells you what kind of an object this is

dir(name) # Directory function gives you a directory of things that you can do with the object
dir(str) # Does the same thing, because we know that the object is a string

help(name.upper) # Help function gives a brief description of the function you're asking about
name.upper # str.upper is a function/method that's bound to an object
name.upper() # Adding parentheses to the end calls that method, asking it to do something
# In this case, Python turns the name "Amy" into all uppercase
help(name.upper()) # Here we are asking for help on 'Amy' and Python doesn't have documentation on it

################################
# 1.1.3 MODULES & METHODS - Quiz
################################
# Question 1: Suppose that math.sqrt and numpy.sqrt had identical behavior. Are they the same function?
# Solution 1: No. Because they belong to different namespaces, Python treats them separately, regardless of their
# behavior.

# Question 2: After running import numpy as np, if you want to access the square root function (sqrt()) from the
# library numpy, which method would you use?
# Solution 2: np.sqrt()

####################################
# 1.1.4 NUMBERS & BASIC CALCULATIONS
####################################
# Numbers are one type of object in Python
# Python has 3 different numeric types:
#       1) Integers
#       2) Floating Point Numbers
#       3) Complex Numbers

# Python integers have unlimited precision - your integer will never be too long to fit into Python's integer type
# You can freely mix different numeric types

123 + 34 # Addition
123 * 34 # Multiplication
123 ** 34 # Raise a number to a power
6/7 # Division
15/7 # Floating Point Division - use 1 slash
15//7 # Floor/Integer Division - use 2 slash signs (rounds to the closest integer)

# Python's Interactive Mode provides the underscore operator
_ # Value of underscore operator = the last object python has returned to you
_*2 # You can interact with the underscore

10 * 2 # Basic multiplication
_ + 5 # Previous answer (20) plus 5
_ ** 2 # Previous answer (25) to the power of 2

# Sometimes we need to use go beyond built-in functions and operations
import math # math module has some basic mathematical operations
# Factorial Operation: n! = n*(n-1)...*1
# E.g. 3! = 3*2*1 = 6
math.factorial(3) # Super easy in Python

###########################################
# 1.1.4 NUMBERS & BASIC CALCULATIONS - Quiz
###########################################
# Question 1: n  factorial is defined as the product of all integers  1,...,n . Additionally, by definition,  0!≡1 .
# What is 4 factorial?
# Solution 1:
math.factorial(4) # 4! = 24

#####################
# 1.1.5 RANDOM CHOICE
#####################
import random # Import the random module
random.choice([2, 44, 55, 66]) # Python returns one of the numbers in the list at random
random.choice(["a", "cc", "dd", "ee"]) # Python doesn't care about the type of object in the list

############################
# 1.1.5 RANDOM CHOICE - Quiz
############################
# Question 1: True or false: random.choice will not work on immutable types.
# Solution 1: False: random.choice only requires that the object has several values regardless of mutability.

##############################
# 1.1.6 EXPRESSIONS & BOOLEANS
##############################
# Expression = combination of objects and operators that computes a value
# Many expressions involve Boolean Data Type
# Boolean Objects = only have two values: True & False
type(True) # In Python, capitalise the words 'True' or 'False' for Python to understand them as boolean
type(TRUE) # Doesn't work if it's all capitalised
type(true) # Doesn't work if not capitalised

# Boolean Operations = operations involving logic, take in 1 or more boolean objects and return 1 boolean object back
# 3 Boolean Operations:
#       1) or - if either x or y is true, Python returns "True"
                True or False # Returns "True"
                True or True # Returns "True"
                False or False # Returns "False"
#       2) and - only true if both objects are true
                True and False # Returns "False"
                True and True # Returns "True"
                False and False # Returns "False"
#       3) not - negates the value of the object
                not True # Returns "False"
                not False # Returns "True"

# 8 different Comparison Operations in python - results of comparisons are always 'True" or 'False
2 < 4 # Is 2 less than 4? - Returns "True"
2 <= 2 # Is 2 less than or equal to 2? - Returns "True"
2 == 2 # Is 2 equal to 2? - Returns "True"
2 != 2 # Is 2 not equal to 2? - Returns "False"

# == and != test whether 2 objects are the same, not if the contents of 2 object are the same
[2, 3] == [3, 3] # Returns "False"
[2, 3] == [2, 3] # Returns "True"
[2, 3] == [3, 2] # Returns "False"

[2, 3] is [2, 3] # Is the first list the same object as the second list? - Returns "False"
[2, 3] is not [2, 3] # Is the first list not the same object as the second list? - Returns "True"

# The == operator compares the value or equality of two objects, whereas the Python is operator checks whether two
# variables point to the same object in memory.

2.0 == 2.0 # Both are Floating Point Numbers - Returns "True"
2.0 == 2 # 2.0 = Floating Point Number & 2 = Integer - Returns "True"
# Python turns the Integer into a Floating Point Number

#####################################
# 1.1.6 EXPRESSIONS & BOOLEANS - Quiz
#####################################
# Question 1: Consider the expression True and not False is True. What will this return?
# Solution 1:
True and not False is True # True

# Question 2: What is the difference between == and is?
# Solution 2: == tests whether objects have the same value, whereas is tests whether objects have the same identity.