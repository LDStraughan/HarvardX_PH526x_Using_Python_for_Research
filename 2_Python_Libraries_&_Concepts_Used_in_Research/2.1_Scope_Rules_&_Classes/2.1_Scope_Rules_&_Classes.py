###################
# 2.1.1 SCOPE RULES
###################
# When calling for x, Python uses the first x that it finds
# LEGB = Local, Enclosing, Global, Built-in - Python starts looking locally, then the enclosing function, etc.

# Practice Scope Rules:
    def update():
        x.append(1)
    x = [1,1]
    update()
    x

    def update(n,x):
        n = 2
        x.append(4)
        print("update: ", n, x)
    def main():
        n = 1
        x = [0,1,2,3]
        print("main: ", n, x)
        update(n,x)
        print("main: ", n, x)
    main()

# Argument = object that is passed to a function as its input when function is called
# Parameter = variable that is used in the function definition to refer to an argument

##########################
# 2.1.1 SCOPE RULES - Quiz
##########################
# Question 1: Consider the following code:
#              def increment(n):
#                   n += 1
#                   print(n)
#
#               n = 1
#               increment(n)
#               print(n)
# What will this print? Note that here, we separate lines of output with ";"
# Solution 1: 2; 1

# Question 2: Consider the following code:
#               def increment(n):
#                   n += 1
#                   #blank#
#               n = 1
#               while n < 10:
#                   n = increment(n)
#               print(n)
# Fill in the #blank# to ensure this prints 10.
# Solution 2:
def increment(n):
    n += 1
    return n # This is the solution
n = 1
while n < 10:
    n = increment(n)
print(n)

#############################################
# 2.1.2 CLASSES & OBJECT-ORIENTED PROGRAMMING
#############################################
# In general, an object consists of internal data & methods that perform operations on said data
# If an existing object type doesn't suit your needs, create a new type of object known as a CLASS.

# Inheritance = you can define a new object type, a new class, that inherits properties from an existing object type

# How to Create a New Class:
class MyList(list): # Name of class = MyList; parentheses after MyList specifies inheritance
    def remove_min(self):
        self.remove(min(self)) # Functions inside class = Instance Methods
    def remove_max(self):
        self.remove(max(self))
# Class statement defines a blueprint of the new type of python object
x = [1,3,4,2,5,8,7,6,10,9]
dir(x)
y = MyList(x)
dir(y) # remove_min & remove_max are now optional methods
y.remove_max()
y.remove_min()
y # 1 & 10 have now been removed from the list

####################################################
# 2.1.2 CLASSES & OBJECT-ORIENTED PROGRAMMING - Quiz
####################################################
# Question 1: Consider the following code:
#               class NewList(list):
#                   def remove_max(self):
#                       self.remove(max(self))
#                   def append_sum(self):
#                       self.append(sum(self))
#               x = NewList([1,2,3])
#               while max(x) < 10:
#                   x.remove_max()
#                   x.append_sum()
#               print(x)
# What will this print?
# Solution 1: Nothing: this program will never halt.