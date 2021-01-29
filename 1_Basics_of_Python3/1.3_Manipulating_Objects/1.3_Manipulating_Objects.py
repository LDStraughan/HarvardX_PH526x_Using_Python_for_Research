######################
# 1.3.1 DYNAMIC TYPING
######################
# Computer's memory works in Binary Code - 0's & 1's. How does a program interpret this sequence?
# A TYPE does 2 things:
#       1) Tells a program to read the sequence in chunks (e.g. 32 bits)
#       2) Tells the computer what te number represents (e.g. integer, character, piece of music, etc.)
# If you move data from one variable to another one that doesn't match, you could lose information.
# E.g. If your program expects a floating-point number but you provide it with an integer, there's no problem because
# integers are a subset of fp numbers.
# But if the program expects an integer and you provide it with a fp number, some info will likely lost.

# Typing or Assigning Data Types = set of rules the language uses to ensure that the receiver knows how to interpret it.

# 2 language typing:
#       1) Static Typing - C++: Type checking is performed during compile time
#       2) Dynamic Typing - Python: TYpe checking is performed at run time

# If we say that x = 3, Python knows x is an integer
# Three important concepts here:
#       1) Object - Python first creates ab object (e.g. 3)
#       2) Variable - Then, Python creates the variable name (e.g. x)
#       3) Reference - Finally, Python will insert a reference from the name of the variable to the actual object
# *NB* Variable names always link to objects, never to other variables
# Variable is, therefore, reference to given object - a name is possibly one of many linked to an object

# Each object has a type, value and an identity
L = [1,2,3]
M = [1,2,3]
L == M # Are the contents/value of L the same as the contents/value of M? - Returns "True"
# Comparisons between 2 lists is done element-wise (L[0] is compared to M[0])
L is M # Is L the same object as M? - Returns "False"
# The identities are different
id(L) # Returns "2064963590912"
id(M) # Returns "2064963591168"
id(L) == id(M) # Is L the same object as M? - Returns "False"

M = L # M is just another name for the same list, L
M = list(L) # Copies list L into an entirely new list, M
M = L[:] # Copies list L into an entirely new list, M

#############################
# 1.3.1 DYNAMIC TYPING - Quiz
#############################
# Question 1: Consider the following code:
#               x=3.
#           x did not exist in memory prior to this code. Which of the following does NOT occur?
# Solution 1: The object 3 refers to the variable name x.

# Question 2:Consider the following code:
#               x=3
#               y=x
#               y=y-1
#           What does x equal?
# Solution 2: 3

# Question 3: Consider the following code:
#               L1 = [2,3,4]
#               L2 = L1
#               L2[0] = 24
#           What does L1 equal?
# Solution 3: [24, 3, 4]

# Question 4: Consider the following code:
#               L = [2,3,4]
#               M1 = L
#               M2 = L[:]
#               M1 is M2
#           What will this return?
# Solution 4: False

##############
# 1.3.2 COPIES
##############
# Copy Module = Create identical copies of an object
# 2 Types of Copies:
#       1) Shadow Copy - Constructs a new compound object and inserts references to the OG object
#       2) Deep Copy - Constructs a new compound object and recursively inserts copies of the OG objects

#####################
# 1.3.2 COPIES - Quiz
#####################
# Question 1: Consider the following code:
#               import copy
#               x = [1,[2]]
#               y = copy.copy(x)
#               z = copy.deepcopy(x)
#               y is z
#           What will this return?
# Solution 1:
import copy
x = [1,[2]]
y = copy.copy(x) # copy.copy = Shadow Copy
z = copy.deepcopy(x) # copy.deepcopy = Deep Copy
y is z # Returns "False"

##################
# 1.3.3 STATEMENTS
##################
# Statements = Used to compute values, assign values, modify attributes, etc.

# 3 Example of more Specialised Statements:
#       1) Return - Return values from a function
#       2) Import - Import modules
#       3) Pass - Do nothing in situations where we need a placeholder for syntactical reasons

# Compound Statements = Contain groups of other statements and affect/control the execution of said statements
# Typically span multiple lines
# Consists of one or more clauses - Clause consists of a header and a block/suite of code
# Clause headers start with KEYWORD, end with COLON and are at the SAME INDENTATION LEVEL
# Block/Suite of code must be indented to indicate that it forms a group of statements under the header
# Example:
if x > y: # Header Line
    difference = x - y # Block of code
    print("x is greater than y") # Block of code
print("But this gets printed no matter what!")

# In Python, indentation is not just cosmetic - it determines the logical structure of program
if x > y: # Is x > y?
    absval = x - y # Absolute Value = how far 2 numbers are from one another
elif y > x: # If first 'if' fails, is y > x?
    absval = y - x
else: # If both 'if' statements fail, just do this
    absval = 0
# If the first statement is true, python won't be evaluated - Python goes through conditions until first truth
# Built-in 'abs' function does all of this

#########################
# 1.3.3 STATEMENTS - Quiz
#########################
# Question 1: Consider the following code:
#               if False:
#                   print("False!")
#               elif True:
#                   print("Now True!")
#               else:
#                   print("Finally True!")
#           What does this print?
# Solution 1: "Now True!"

# Question 2: Consider the following code:
#               if n%2 == 0:
#                   #blank#
#               else:
#                   print("odd")
# Assume that n is a previously defined integer. Can you replace the #blank# line so that the code prints "even" if n
# is even, and "odd" if n is odd?
# Solution 2:
if n%2 == 0:
    print("even")
else:
    print("odd")

#########################
# 1.3.4 FOR & WHILE LOOPS
#########################
# For Loop = sequence iteration that assigns items in sequence to target one at a time & runs the block of code for
# each item
# Unless the loop is terminated early, it'll run as many times as there are items

for x in range(10):
    print(x) # Prints out the numbers one at a time

names = ["Jim", "Tom", "Nick", "Pam", "Sam", "Tim"] # Define List of 6 names
for name in names:
    print(name) # Prints out the names one at a time

age = {"Jim": 31, "Nick": 31, "Pam": 27, "Sam": 35, "Tim": 31, "Tom": 50} # Create Dictionary of names & ages
for name in age.keys():
    print(name, age[name]) # Python first prints the name, then the age of the person

for name in age: # Looping over dictionaries is so common that we can remove the ",keys" part:
    print(name, age[name])
# Doesn't loop in any specific order

for name in sorted(age.keys()): # Sorts names by alphabetical order
    print(name, age[name])

for name in sorted(age.keys(), reverse = True): # Sorts names by reverse alphabetical order
    print(name, age[name])

# While Loop = Repeated execution of code, as long as given expression is true

# While Loop - You don't know how many times you're running the code
# For Loop - You are aware how many times the code will run (as many times as there are items)

################################
# 1.3.4 FOR & WHILE LOOPS - Quiz
################################
# Question 1: Consider bears = {"Grizzly":"angry", "Brown":"friendly", "Polar":"friendly"}. Can you replace #blank# so
# the code will print a greeting only to friendly bears? Your code should work even if more bears are added to the
# dictionary.
#               for bear in bears:
#                   if #blank#:
#                   print("Hello, "+bear+" bear!")
#               else:
#                   print("odd")
# Solution 1:
bears = {"Grizzly":"angry", "Brown":"friendly", "Polar":"friendly"}
for bear in bears:
    if bears[bear] == "friendly":
    print("Hello, "+bear+" bear!")
else:
    print("odd")

# Question 2: Consider the following code:
#               is_prime = True
#               for i in range(2,n):
#                   if n%i == 0:
#                       #blank#
#               print(is_prime)
# Can you fill in the #blank# line so the code will only print True if n is prime?
# Solution 2:
is_prime = True
for i in range(2,n):
    if n%i == 0:
        is_prime = False
print(is_prime)
# A more compact way to accomplish the same task is: not any([n%i==0 for i in range(2,n)]).

# Question 3: Consider the following code:
#               n=100
#               number_of_times = 0
#               while n >= 1:
#                   n //= 2
#                   number_of_times += 1
#               print(number_of_times)
#           What will this print?
# Solution 3:
n=100
number_of_times = 0
while n >= 1:
    n //= 2
    number_of_times += 1
print(number_of_times) # Returns "7"

###########################
# 1.3.5 LIST COMPREHENSIONS
###########################
# List Comprehension = Take an existing list, apply an operation to all items on it and create a new list with results

# Computing squares of a list of numbers:
numbers = range(10)
squares = [] # Set up an empty List
for number in numbers: # for loop to go over each number
    square = number**2 # square is each number squared
    squares.append(square) # append squared number to squares list
squares # Returns "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]"

squares2 = [number**2 for number in numbers] # does the same as above
squares2 # Returns "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]"

# List Comprehensions are fast and elegant

##################################
# 1.3.5 LIST COMPREHENSIONS - Quiz
##################################
# Question 1: Consider the following code:
#               sum([i**2 for i in range(3)])
#           What will this output?
# Solution 1:
sum([i**2 for i in range(3)]) # Returns "5"

# Question 2: How can you use a list comprehension, including if and for, to sum the odd numbers from 0 through 9?
# Solution 2:
sum([i for i in range(10) if i%2 == 1]) # Returns "25"

###############################
# 1.3.6 READING & WRITING FILES
###############################
# Reading:
filename = "inputfile.txt"
for line in open(filename):
    print(line)
# rstrip() method removes the line break character inherent in txt
for line in open(filename):
    line = line.rstrip()
    print(line)

# Writing:
F = open("outputfile.txt", "w") # "w" tells Python we are creating a file object for writing, not reading
F.write("Python\n") # Provide input as a string - Add extra character (\n) for the line break
F.close()

######################################
# 1.3.6 READING & WRITING FILES - Quiz
######################################
# Question 1: Consider the following code:
#
#                 F = open("input.txt", "w")
#                 F.write("Hello\nWorld")
#                 F.close()
#                 lines = []
#                 for line in open("input.txt"):
#                     lines.append(line.strip())
#                 print(lines)
#           What does this print?
# Solution 1:
F = open("input.txt", "w")
F.write("Hello\nWorld")
F.close()
lines = []
for line in open("input.txt"):
    lines.append(line.strip())
print(lines) # Returns "['Hello', 'World']"

#################################
# 1.3.7 INTRODUCTION TO FUNCTIONS
#################################
# Functions = Devices for grouping statements so that they can be run multiple times more easily
# Maximise code reuse and minimise code redundancy
# Procedural Decomposition = Divide larger tasks into smaller chunks

# Write functions with the "def" statement
# Send result object back to caller using "return" statement
def add(a,b): # Define an add function
    mysum = a + b # Calculate a sum - names created & assigned in function are local & exist only while function runs
                  # "global" statement = modify the value of a global variable from inside a function
    return mysum # Return mysum to the caller function
add(12, 15) # Use the function just created - Returns "27"
# Arguments are matched by position, so 12 = a and 15 = b

# Tuples can return multiple values from a function
def add_and_sub(a,b):
    mysum = a + b
    mydiff = a - b
    return (mysum, mydiff) # Create a tuple where the first object returned is mysum and second is mydiff
add_and_sub(20, 15) # Returns "(35, 5)"

# Arguments are passed by assigning multiple objects to local names
def modify(mylist):
    mylist[0] *= 10 # Look at the first element of the list and multiply it by 10
L = [1,3,5,7,9] # Create a List
modify(L) # Call modify function using L
L # Returns "[10, 3, 5, 7, 9]" - first element has been multiplied by 10

########################################
# 1.3.7 INTRODUCTION TO FUNCTIONS - Quiz
########################################
# Question 1: Consider the following function:
#               def modify(mylist):
#                       mylist[0] *= 10
#                   return(mylist)
#               L = [1, 3, 5, 7, 9]
#               M = modify(L)
#               M is L
#           What is the value of the final line?
# Solution 1:
def modify(mylist):
    mylist[0] *= 10
    return(mylist)
L = [1, 3, 5, 7, 9]
M = modify(L)
M is L # Returns "True" - Because L is mutable, modify alters mylist directly

################################
# 1.3.8 WRITING SIMPLE FUNCTIONS
################################
# Construct a function that loops over all members of sequence 1 and asks if that member is also part of sequence 2:
def intersect(s1, s2): # There will be 2 input arguments
    res = []  # How are we going to keep track of results that our function generates? - Create res as empty List
    for x in s1: # Look at member x is in sequence 1
        if x in s2: # Check id member x is also in sequence 2
            res.append(x) # If both are True, append the answer to "res" list
    return res # Return the answer
intersect([1,2,3,4,5], [3,4,5,6,7]) # Returns "[3, 4, 5]"

# Construct a program that generates passwords - be able to specify character set & length of password:
def password(length): # Only needs one argument - the length of the password
     import random # What module, if any, would we need to import? - Random
     pw = str() # Generate an empty String
     characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+" # Define character set
     for i in range(length): # Create a range object that consists of length number of members
        pw = pw + random.choice(characters) # Sample characters randomly from "characters" List - Concatenate characters
     return pw
password(20) # IT WORKS!

#######################################
# 1.3.8 WRITING SIMPLE FUNCTIONS - Quiz
#######################################
# Question 1: Consider the function intersect() defined in the previous video, 1.3.8: Writing Simple Functions.
#           What will intersect([1,2,3], [3,4,5,6,7]) return?
# Solution 1: [3]

# Question 2: Consider the following code:
#               def is_vowel(letter):
#                   if #blank#:
#                       return(True)
#                   else:
#                       return(False)
#           Can you replace #blank# in the second line so is_vowel becomes a function that takes a letter as input and
#           prints whether a letter is a vowel (in "aeiouy")?
# Solution 2:
def is_vowel(letter):
    if letter in "aeiouy":
        return(True)
    else:
        return(False)

# Question 3: Consider the function call is_vowel(4). Why would this not work?
# Solution 3: 4 is not a string, and Python cannot test if an int is in a string.

# Question 4: Consider the following proposed emendation of is_vowel:
#               def is_vowel(letter):
#                   if type(letter) == int:
#                       letter = str(letter)
#                   if letter in "aeiouy":
#                       return(True)
#                   else:
#                       return(False)
#            Does this properly accommodate objects of type int for use with is_vowel? For example, will is_vowel(4)
#            produce a correct answer?
# Solution 4:
def is_vowel(letter):
    if type(letter) == int:
        letter = str(letter)
    if letter in "aeiouy":
        return(True)
    else:
        return(False)
is_vowel(4)

# Question 5: Recall that  n!  (" n  factorial") is defined as the product of all integers  1,...,n .
#           Additionally, by definition,  0!≡1 .
#           Let's create a factorial function. Consider the following code:
#               def factorial(n):
#                   if n == 0:
#                       return 1
#                   else:
#     	                N = 1
#                       for i in range(1, n+1):
#                           #blank#
#                       return(N)
#           Can you fill in the #blank# to complete the function as described above?
# Solution 5:
def factorial(n):
    if n == 0:
        return 1
    else:
    	N = 1
        for i in range(1, n+1):
            N *= i # Alternatively, N = N * i also works
        return(N)

################################
# 1.3.9 COMMON MISTAKES & ERRORS
################################
# Common Mistake 1:
#   Not reading/understanding error messages

# Common Mistake 2:
#   Forgetting that dictionaries are unordered

# Common Mistake 3:
#   Trying to do an operation not supported by the object
#   Make sure you know the type of the object and the methods available to said object

# Common Mistake 4:
#   Trying to access an object in the wrong way

# Common Mistake 5:
#   Trying to modify immutable objects

# Common Mistake 6:
#   Trying to operate on objects of different type

# Common Mistake 7:
#   Improper indentation

#######################################
# 1.3.9 COMMON MISTAKES & ERRORS - Quiz
#######################################
# Question 1: When you encounter an error in Python, what should you do?
# Solution 1: All of the above.