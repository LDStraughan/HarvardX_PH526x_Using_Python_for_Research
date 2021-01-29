####################################
# 2.2.1 INTRODUCTION TO NUMPY ARRAYS
####################################
# NumPy = Python module designed for scientific computation
# Has several useful features:
#       1) NumPy Arrays = n-dimensional array objects and are core component of scientific & numerical computation
#       2) Integrates your code with existing C, C++, Fortran code
#       3) Helps perform linear algebra, generate random numbers, etc.

# Numpy Arrays = additional data type used to represent vectors & matrices - have FIXED SIZE when created
# Elements in NumPy arrays = all the same data type - leading to more efficient & simpler code
# By default, elements are floating-point numbers

# Constructing Empty Vector & Matrix
import numpy as np # Import numpy module
zero_vector = np.zeros(5) # Define zero vector with 5 elements
zero_matrix = np.zeros((5,3)) # Matrix is a 2-dimensional table - argument has to be a tuple
# np.ones function works the same as np.zeros, just imports 1's instead of 0's
# np.empty is the same, just allocates requested space but doesn't initialise it - if dealing with a very large array
# this will save time
# np.array constructs array using specified values - input argument is a sequence of numbers

# Practice:
x = np.array([1,2,3])
y = np.array([2,4,6])
# When constructing a 2-D NumPy array, specify elements of each row and define entire table as a list containing them
np.array([[1,3], [5,9]])
# Transpose = turn table sideways - 1st row becomes 1st column, etc.
A = np.array([[1,3], [5,9]])
A.transpose()
A

###########################################
# 2.2.1 INTRODUCTION TO NUMPY ARRAYS - Quiz
###########################################
# Question 1: True or False: a numpy array's length may be modified after being created.
# Solution 1: False

# Question 2: Consider the following object:
#               numpy.array([0., 0., 0., 0., 0.])
#           What code will produce that object?
# Solution 2: numpy.zeros(5)

# Question 3: Consider the following code:
#               x = numpy.array([[3,6],[5,7]])
#               y = x.transpose()
#               print(y)
#           What does this print?
# Solution 3: array([[3 5],[6 7]])

############################
# 2.2.2 SLICING NUMPY ARRAYS
############################
# Indices start at 0
# In 2-D arrays, the 1st index specifies the row & 2nd the column
# In multi-D arrays, use colon in place of fixed value for index - elements corresponding to all values will be returned

# Practice:
x = np.array([1,2,3]) # 1-D arrays are lowercase
y = np.array([2,4,6])
X = np.array([[1,2,3], [4,5,6]]) # 2-D arrays are uppercase
Y = np.array([[2,4,6], [8,10,12]])

x[2] # Returns "3" - element located at position 2
x[0:2] # Returns "array([1, 2])" - slicing also works here

z = x + y
z # Returns "array([3, 6, 9])" - adds each corresponding element together

X[:,1] # Returns "array([2, 5])" - access to column 1 (i.e. 2nd column) of table X
Y[:,2] # Returns "array([ 6, 12])" - access to column 2 (i.e. 3rd column) of table Y
X[:,1] + Y[:,2] # Returns "array([ 8, 17])" - can add them together
X[1,:] # Returns "array([4, 5, 6])" - access to row 1 (i.e. 2nd row) of table X
X[1] # Returns "array([4, 5, 6])" - 2-D arrays are defined as nested rows so this shorthand works
X[1,:] + Y[1,:] # Returns "array([12, 15, 18])" - can add them together

[2,4] + [6,8] # Returns "[2, 4, 6, 8]" - adding 2 lists concatenates the lists
np.array([2,4]) + np.array([6,8]) # Returns "array([ 8, 12])" - element-wise addition occurs in arrays

###################################
# 2.2.2 SLICING NUMPY ARRAYS - Quiz
###################################
# Question 1: Consider the following code:
#               x = np.array([1,2,5])
#               x[1:2]
#           What does this return?
# Solution 1: array([2]) - splicing stops before including stop value

# Question 2: Consider the following code:
#               a = np.array([1,2])
#               b = np.array([3,4,5])
#               a + b
#           What does this return?
# Solution 2: This code contains an error. - arrays have different shapes

#############################
# 2.2.3 INDEXING NUMPY ARRAYS
#############################
# NumPy arrays can be indexed with other arrays and other sequence-like objects like lists
z1 = np.array([1,3,5,7,9])
z2 = z1 + 1 # takes each element from z1 and adds 1
z1 # Returns "array([1, 3, 5, 7, 9])"
z2 # Returns "array([ 2,  4,  6,  8, 10])"
ind = [0,2,3] # Define a list to index z1 & z2
z1[ind] # Returns "array([1, 5, 7])"
ind = np.array([0,2,3]) # Also works as np.array
z1[ind] # Returns "array([1, 5, 7])" - can index NumPy arrays with lists or other numPy arrays

# NumPy arrays can also be indexed using logical indices - like boolean elements
z1 = np.array([1,3,5,7,9])
z1 > 6 # Returns "array([False, False, False,  True,  True])"
z1[z1>6] # Returns "array([7, 9])" - prints all of the elements in z1 that satisfy the index
z2 = z1 + 1
z2[z1>6] # Returns "array([ 8, 10])" - prints the corresponding elements in z2 that satisfied the index regarding z1
ind = z1>6
z2[ind] # Returns "array([ 8, 10])" - does the same thing

# When slicing an array using colon, you get a view of the object - if you modify it, the original will also be modified
# In contrast, when indexing an array, a copy of the original data is returned
z1 = np.array([1,3,5,7,9])
w = z1[0:3] # SLICING
w[0] = 3
w # Returns "array([3, 3, 5])"
z1 # Returns "array([3, 3, 5, 7, 9])" - first element (at location 0) has ben modified
z1 = np.array([1,3,5,7,9])
ind = [0,1,2] # INDEXING
w = z1[ind]
w[0] = 3
w # Returns "array([3, 3, 5])"
z1 # Returns "array([1, 3, 5, 7, 9])" - first element (at location 0) remains the same
# SPLICING changes original & INDEXING creates a copy

####################################
# 2.2.3 INDEXING NUMPY ARRAYS - Quiz
####################################
# Question 1: Consider the following code:
#               a = np.array([1,2])
#               b = np.array([3,4,5])
#               b[a]
#           What does this return?
# Solution 1: array([4, 5])

# Question 2: Consider again the above code, as well as the following:
#               c = b[1:]
#               b[a] is c
#           What does Python return?
# Solution 2: False - When testing values, you could try b[a] == c or all(b[a] == c)

#########################################
# 2.2.4 BUILDING & EXAMINING NUMPY ARRAYS
#########################################
# NumPy provides a few ways to construct arrays with fixed starts & end values, so that other elements are uniformly
# spaced between them
# np.linspace = linearly spaced elements - set start and end point, then the number of elements in array
np.linspace(0,100,10) # Returns "array([  0.        ,  11.11111111,  22.22222222,  33.33333333, 44.44444444,
                      # 55.55555556,  66.66666667,  77.77777778, 88.88888889, 100.        ])"
# np.logspace = logorithmically spaced elements - set log of starting and end points, then no. of elements in array
np.logspace(1,2,10) # log of 10 is 1, log of 100 is 2, with 10 evenly spaced elements - Returns "array([ 10.        ,
                    # 12.91549665,  16.68100537,  21.5443469 , 27.82559402,  35.93813664,  46.41588834,  59.94842503,
                    # 77.42636827, 100.        ])"
np.logspace(np.log10(250), np.log10(500), 10) # start with base 10 logarithm of 250, end with base 10 logarithm of 500,
                                              # and have 10 evenly spaced elements - Returns "array([250.        ,
                                              # 270.01493472, 291.63225989, 314.98026247, 340.19750004, 367.43362307,
                                              # 396.85026299, 428.62199143, 462.93735614, 500.        ])"

# Know the shape of an array or no. of elements in it:
X = np.array([[1,2,3], [4,5,6]])
X.shape # What is the shape of array X? - Returns "(2, 3)" - It has 2 rows & 3 columns
X.size # How many elements in array X? - Returns "6" - It has 6 elements in it
# We don't need parentheses in above examples because shape & size are data attributes, not methods of the arrays

# Check whether entries an an array satisfy logical conditions:
x = np.random.random(10) # NumPy has own random module - Generating 10 random numbers, ranging from 0 - 1
x # Returns "array([0.44516206, 0.77674082, 0.28893503, 0.00930683, 0.43315403, 0.57186819, 0.68847475, 0.98444465,
  # 0.58136969, 0.95573297])"
np.any(x > 0.9) # Are there any elements in array x that are greater than 0.9? - Returns "True"
np.all(x >= 0.1) # Are all of the elements in array x greater than or equal to 0.1? - Returns "False"
# Output answers for the entire array - doesn't specify which is true and false

################################################
# 2.2.4 BUILDING & EXAMINING NUMPY ARRAYS - Quiz
################################################
# Question 1: Consider the following code:
#               x = 20
#               not np.any([x%i == 0 for i in range(2, x)])
#           What does the above code do?
# Solution 1: Finds whether x is prime. - x%i == 0 tests if x has a remainder when divided by i. If this is not true for
#                                         all values strictly between 1 and x, it must be prime!