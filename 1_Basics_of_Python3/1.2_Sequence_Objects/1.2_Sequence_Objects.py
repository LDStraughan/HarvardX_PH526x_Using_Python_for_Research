#################
# 1.2.1 SEQUENCES
#################
# Sequence = collection of objects ordered by their position
# 3 Basic Sequences:
#       1) Lists
#       2) Tuples
#       3) Range Objects
# Python has addition sequence types for representing things like strings
# Any sequence data type will support the common sequence operations
# Each type has its own methods available for performing specific operation

# Indexing starts at 0 - the first element in the sequence is called with 0
s = ["a", "b", "c", "d"] # creates a list object called s
s[0] # Returns "a"
s[1] # Returns "b"
s[-1] # Negative index starts at the back - Returns "d" (0 is always 0)

# Slicing = extracts multiple objects from a sequence
s[0:2] # Returns "['a', 'b']" - slices stop before the last element stated (in this case before 2 or 'c')

########################
# 1.2.1 SEQUENCES - Quiz
########################
# Question 1: Consider the following tuple and index (1,2,3)[-0]. What will this return?
# Solution 1:
(1,2,3)[-0] # 1

# Question 2: Consider the following tuple and index (1,2,3)[-0:0]. What will this return?
# Solution 2:
(1,2,3)[-0:0] # ()

#############
# 1.2.2 LISTS
#############
# Lists are mutable sequences of objects of any type, typically used to store homogeneous items
# Strings = sequences of individual characters - Immutable
# Lists = sequence of any type of Python object - Mutable

numbers = [2, 4, 6, 8] # Construct a list of numbers - square brackets construct a list
numbers[0] # Look at first element in list - Returns "2"
numbers[1] # Look at second element in list - Returns "4"
numbers[-1] # Look at last element in list - Returns "8"

numbers.append(10) # Append the number 10 to the numbers list
numbers # Returns "[2, 4, 6, 8, 10]"

# Concatenation = operation of joining character strings end-to-end
# E.g., the concatenation of "snow" and "ball" is "snowball".

x = [12, 14, 16] # Construct a second list of numbers
#  Use plus sign (as long as both objects are lists) to concatenate them
numbers + x # Returns "[2, 4, 6, 8, 10, 12, 14, 16]"
type(_) # Check type of object last printed - Returns "<class 'list'>"

numbers = [1, 3, 5, 7, 11, 13, 17, 19, 23] # Construct new list of numbers
numbers.reverse() # Reverse the content of the list - but it doesn't return anything
# List methods are called In-Place Methods - they MODIFY the original list
numbers # Returns "[23, 19, 17, 13, 11, 7, 5, 3, 1]"

names = ["Zofia", "Alex", "Morgan", "Anthony"] # Construct list of names
names.sort() # sort method sorts the names - Returns nothing
names # The list is now in alphabetical order

# sort method takes the existing list and reorders the objects within it
# sorted function constructs a completely new list with the objects reordered
names.reverse()
names # Order has been reversed

sorted_names = sorted(names) # Sorts the names list and saves it in the object 'sorted_names'
names # names list has not changed - it's still reversed
sorted_names # New list has all of the names in alphabetical order

sorted(numbers) # Sorts the numbers list - does not make an object automatically
numbers # numbers list has not changed - it's still reversed

len(names) # Find out how many objects the list contains -  Returns "4"

####################
# 1.2.2 LISTS - Quiz
####################
# Question 1:Consider a list x=[1,2,3]. Which index corresponds to 2 in x?
# Solution 1:
x=[1,2,3] # 1

# Question 2: Consider a list x=[1,2,3]. Enter the code below for how you would use the append method to add the
# number 4 to the end of list x.
# Solution 2:
x.append(4)

# Question 3: What do list methods such as reverse and sort return?
# Solution 3: They return nothing because they are in-place methods, meaning they alter the content of the original list.

##############
# 1.2.3 TUPLES
##############
# Tuples are immutable sequences typically used to store heterogeneous data
# Tuple = single object consisting of several different parts
# Especially useful when you want to return more than one object - you wrap all of the objects within a single tuple

T = (1,3,5,7) # Construct tuple - parentheses create a tuple
type(T) # Returns "<class 'tuple'>"
len(T) # Number of objects in tuple = 4
T + (9, 11) # Concatenate tuple with another tuples, i.e. (9, 11)
T[1] # Returns "3"

# Packing and Unpacking Tuples:
x = 12.23 # Create variable 'x'
y = 23.34 # Create variable 'y'
# Think of these as coordinates
coordinate = (x,y) # PACK a tuple using x & y - called TUPLE PACKING
type(coordinate) # Returns "<class 'tuple'>"
coordinate # Returns "(12.23, 23.34)"
(c1, c2) = coordinate # UNPACK tuple into another tuple
c1 # Contains the first object - Returns "12.23"
c2 # Contains the second object - Returns "23.34"

# Can use tuples in FOR loops:
        # Create multiple tuples of coordinates:
        c0 = (0,0)
        c1 = (1,1)
        c2 = (2,4)
        c3 = (3,9)
        c4 = (4,16)
        c5 = (5,25)
        c6 = (6,36)
        c7 = (7,49)
        c8 = (8,64)
        c9 = (9,81)

        coordinates = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9] # Construct list of coordinate tuples
        coordinates
for (x,y) in coordinates: # Go over the container one at a time
    print(x,y)
for x,y in coordinates: # Don't need parenthesis
    print(x,y)

# What if there's only 1 object in a tuple?:
c = (2,3) # 2 objects in tuple
type(c) # Returns "<class 'tuple'>"
c = (2) # 1 object in tuple?
type(c) # Not actually a tuple - Returns "<class 'int'>"
c = (2,) # 1 object in tuple
type(c) # Returns "<class 'tuple'>"

#####################
# 1.2.3 TUPLES - Quiz
#####################
# Question 1: Consider the tuple x=(1,2,3). How could you add the integer 4 to the end of the tuple?
# Solution 1: This is impossible. Tuples are immutable, so they can't be edited after they’ve been created.

# Question 2: Consider x=(1,2,3). Use the count method to count the number of 3s in x.
# Solution 2:
x=(1,2,3)
x.count(3)

# Question 3: Consider again x=(1,2,3). If you wanted the sum of the numbers in x using a single function, which
# command would you use?
# Solution 3:
sum(x)

# Question 4: Which of the following prints type tuple?
# Solution 4:
type((2,))

##############
# 1.2.4 RANGES
##############
# Ranges = Immutable sequences of integers, typically used in FOR loops
range(5) # Create a range object, put the stopping value of the range in parentheses - Returns "range(0, 5)"
list(range(5)) # To see the content of that range, turn it into a list - Returns "[0, 1, 2, 3, 4]"
# Python stops before the stopping value, so range 5 = 0 to 4
list(range(1,6)) # Provide starting point - Returns "[1, 2, 3, 4, 5]"
list(range(1,13, 2)) # Provide step size of 2 - Returns "[1, 3, 5, 7, 9, 11]"

# Only turn range objects into lists to see the content
# Using lists in a FOR loop means more numbers - range = 3 numbers (start, stop & step); lists = potentially much more

#####################
# 1.2.4 RANGES - Quiz
#####################
# Question 1: Why might you prefer to use a range over a list?
# Solution 1: Ranges take up less memory than lists because they do not hold all the numbers simultaneously.

###############
# 1.2.5 STRINGS
###############
# Strings = Immutable sequences of characters
# Enclose strings in single quotes, quotation marks or triple quotes

S = "Python" # Define a string
len(S) # len function to find out how long the string is - Returns "6"
S[0] # Access first element - Returns "P"
S[-1] # Access last element - Returns "n"
S[0:3] # Slice the first three elements - Returns "Pyt"
S[-3:] # Slice using negative indices - Returns "hon"
"y" in S # Is 'y' in the string? - Returns "True"
"Y" in S # Is capital 'Y' in the string? - Returns "False"

# Polymorphism = what an operator does depends on the type of object it's applied to
12 + 12 # Addition - adds two NUMBERS together to create new value
"hello" + "world" # Concatenation - takes two STRINGS and puts them next to each other
# Both use '+' but they do different things
# 3 * 5 = 5 + 5 + 5 - Multiplication of numbers
# 3 * S = S + S + S - Python concatenates the 'S'
S = "Python" # Define a string object S
3 * S # Python concatenates the string with itself to become a new string - Returns "PythonPythonPython"
"eight equals " + 8 # Doesn't work because the first object is a string and the second a number
"eight equals " + str(8) # Have to turn a number into a string with str function

dir(str) # List things we can do with a string
help(str.replace) # Return a copy with all occurrences of substring old replaced by new.
name = "Tina Fey" # Define a string and store it in object 'name'
name.replace("T", "t") # Replace the capital T in 'name' with lowercase t
# Strings are immutable, so Python doesn't modify the original string, it makes a copy
new_name = name.replace("T", "t") # Assign the new string to a variable
name # Capital T remains the same
new_name # Lowercase t has replaced the capital T

# Split Method = breaks down a string into substrings - Specify the character Python should use to split string
names = name.split(" ") # Split string by the space (" ") in between them
type(names) # Returns "<class 'list'>"
len(names) # How many objects are contained in the list? - Returns "2"
names # Returns ['Tina', 'Fey']
names[0] # Returns "Tina"
names[1] # Returns "Fey"
type(names[0]) # Extract the first object and ask what type of object it is  - Returns "<class 'str'>"
# Now that we know it's a string, we can call string methods to modify it
names[0].upper() # Returns "TINA"
names[1].lower() # Returns "fey"

######################
# 1.2.5 STRINGS - Quiz
######################
# Question 1: Which of the following expressions are valid?
# Solution 1:
2 + 2
"2" + "2"
2 * 2
2 * "2"

# Question 2: Which of the following lines of code will fail to return the integers 0 through 9 in a single string?
# Solution 2:
str(range(10))

# Question 3: Assume you have assigned x the string value of "125,000" (i.e., x = "125,000"). Can you find a string
# method that tests if x only contains digits? Enter your code that tests whether x contains only digits.
# Solution 3:
x = "125,000"
x.isdigit() # The isdigit() method tests whether a string only contains digits - Returns "False"

############
# 1.2.6 SETS
############
# Sets = Unordered collections of distinct hashable objects
# Hashable = Immutable objects - its value does not change during its lifetime, so Python creates a unique hash value
# to identify it. This can then be used by dictionaries to track the unique keys and SETS to track unique values.
# 2 types of sets:
#               1) Set - Mutable
#               2) Frozen Set - Immutable
# Sets can't be indexed - objects inside sets don't have locations
# Elements can't be duplicated - they have to be unique/distinct
# Useful for keeping track of distinct objects and doing mathematical set operations like unions, intersections, and
# set differences.

# Create an object that contains distinct IDs
ids = set() # Can create an empty set with set function followed by parentheses
ids = set ([1,2,3,4,5,6,7,8,9]) # Create a set with members in it - insert a list into parentheses
len(ids) # Returns "9"
ids.add(10) # Add an ID to set
len(ids) # Returns "10"
ids.add(2) # Add ID number 2 to set - we already have 2 in the set
len(ids) # Returns "10" - Nothing happened because numbers have to be unique
ids.pop() # pop function removes members/objects from set
ids.pop() # Do this 4 times
ids.pop()
ids.pop()
len(ids) # Returns "6" - the first 4 numbers have been removed
ids = set(range(11)) # Redefine IDs set with numbers ranging 0 - 10
ids # Returns "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}"
males = set([1,3,5,7,9]) # Construct a set of IDs of males - build as a list
females = ids - males # Define female set as IDs minus males IDs
females # Returns "{0, 2, 4, 6, 8, 10}"
type(females) # Returns "<class 'set'>"

# Set Union Operation:
everyone = males | females # Create set called everyone, containing males and females (short hand for set union is "|")
everyone # Returns "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}"

# Take an Intersection of 2 sets with "&" operation
everyone & set([4,5,6,11,13]) # Define another set and look for where the sets intersect - Returns "{4, 5, 6}"

# Use sets to count no. of unique letters in a word:
word = "anitdisestablishmentarianism" # Define word of interest
letters = set(word) # Create word into a set and store it in 'letters' object
letters # Returns "{'a', 'd', 'l', 't', 's', 'r', 'i', 'e', 'm', 'b', 'n', 'h'}"
len(word) # Length of base word - Returns "28"
len(letters) # No. of unique letters in word - Returns "12"

###################
# 1.2.6 SETS - Quiz
###################
# Question 1: Let sets x={1,2,3} and y={2,3,4}. How could you get {4} from x and y using basic set operations? Enter
# your code here.
# Solution 1:
x={1,2,3}
y={2,3,4}
y - x
y.difference(x) # Also works well

# Question 2: Consider again sets x={1,2,3} and y={2,3,4}. How could you get {2, 3} from x and y using basic set
# operations? Enter your code here.
# Solution 2:
x & y
x.intersection(y) # Also works well

# Question 3: Consider again sets x={1,2,3} and y={2,3,4}. How could you get {1, 4} from x and y using the provided set
# methods? Enter your code here.
# Solution 3:
set(x|y) - set(x&y)
x.symmetric_difference(y) # Also works well

# Question 4: Consider again sets x={1,2,3} and y={2,3,4}. Which of the following lines of code will determine if all
# elements of x are in y?
# Solution 4:
x.is_in(y)

####################
# 1.2.7 DICTIONARIES
####################
# Dictionaries - Mappings from key objects to value objects
# Must consist of Key:Value pairs where keys are immutable
# Dictionaries are mutable - you can modify its contents as you wish
# Used for fast look-ups on unordered data
# Not sequences - don't have left-right order - Looping over will be in arbitrary order

age = {} # Construct empty dictionary
age = dict() # Does the same as "age = {}"
age = {"Dwight": 29, "Jim": 31, "Pam": 27} # Names = Key; Age = Value objects
age["Pam"] # Look for Pam's age - Returns "27"
age["Dwight"] = age ["Dwight"] + 1 # Increase Dwight's age by 1
age["Dwight"] += 1 # Does the same as "age["Dwight"] = age ["Dwight"] + 1"
age["Dwight"] # Dwight has aged 2 years - Returns "31"
# + must come before =, otherwise we're saying x = +1 - first do incrementation, then assignment

# View Object = provide a dynamic view of the keys/values in the dictionary
# As you modify dictionary, views will change correspondingly
# Keys Method:
names = age.keys() # Extract all names in dictionary and store in 'names' object
type(names) # Returns "<class 'dict_keys'>"
age["Michael"] = 50 # Add Michael to 'age' dictionary, aged 50
names # Returns "dict_keys(['Dwight', 'Jim', 'Pam', 'Michael'])" - names object now contains Michael without redefining
# Values Method:
ages = age.values() # Extract all ages in dictionary and store in 'ages' object
type(ages) # Returns "<class 'dict_values'>"
age["Stanley"] = 46 # Add Stanley to 'age' dictionary, aged 46
names # Returns "dict_keys(['Dwight', 'Jim', 'Pam', 'Michael', 'Stanley'])" - names object now contains Stanley
ages # Returns "dict_values([31, 31, 27, 50, 46])" - ages object now contain's Stanley's age without redefining

# Object Membership in a Dictionary:
"Jim" in age # Is Jim a key in our dictionary? - Returns "True"
"Creed" in age # Is Creed in our dictionary? - Returns "False"

###########################
# 1.2.7 DICTIONARIES - Quiz
###########################
# Question 1: Consider the dictionary: age={'Tim':29, 'Jim':31, 'Pam':27, 'Sam':35}
# age[0] returns an error. Why?
# Solution 1: There is no key 0 in the dictionary.

# Question 2: Why may you not edit the key "Tim" to "Tom"?
# Solution 2: Dictionary keys are not mutable.

# Question 3:Which of the following data structures may be used as keys in a dict?
# Solution 3: Strings & Tuples (because they are immutable)