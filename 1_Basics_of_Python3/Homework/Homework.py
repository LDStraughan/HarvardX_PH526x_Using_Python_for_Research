############
# EXERCISE 1
############
# In this five-part exercise, we will count the frequency of each letter in a given string.
#   Exercise 1a:
#      Import the string library.
#      Create a variable alphabet that consists of the lowercase and uppercase letters in the English alphabet using the
#      ascii_letters data attribute of the string library.
#      What line of code did you use to create the alphabet variable?
#   Solution:
        import string
        alphabet = string.ascii_letters

#   Exercise 1b:
#       The lower and upper case letters of the English alphabet should stored as the string variable alphabet.
#       Consider the sentence 'Jim quickly realized that the beautiful gowns are expensive'.
#       Create a dictionary count_letters with keys consisting of each unique letter in the sentence and values
#       consisting of the number of times each letter is used in this sentence. Count upper case and lower case letters
#       separately in the dictionary.
#   Solution:
        sentence = "Jim quickly realized that the beautiful gowns are expensive"
        count_letters = {}
        for letter in sentence:
                if letter in alphabet:
                        if letter in count_letters.keys():
                                count_letters[letter] += 1
                        else:
                                count_letters[letter] = 1
#       What is the 3rd value of the dictionary?
        print(list(count_letters.values())[2]) # Returns "1"
#       What is the 8th value of the dictionary?
        print(list(count_letters.values())[7]) # Returns "3"

#   Exercise 1c:
#       Rewrite your code from Exercise 1b to make a function called counter that takes a string input_string and
#       returns a dictionary of letter counts count_letters.
#       Use your function to call counter(sentence).
#       What is the correct function header for the counter function?
#   Solution:
        def counter(input_string): # This is the correct header
            count_letters = {}
            for letter in input_string:
                if letter in alphabet:
                    if letter in count_letters:
                        count_letters[letter] += 1
                    else:
                        count_letters[letter] = 1
            return count_letters

#   Exercise 1d:
#       Abraham Lincoln was a president during the American Civil War. His famous 1863 Gettysburg Address has been
#       stored as address. Use the counter function from 1c to return a dictionary consisting of the count of each
#       letter in this address and save it as address_count.
        address = """Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth."""
#       How many times does the letter h appear in the Gettysburg Address?
#   Solution:
        address_count = counter(address)
        address_count["h"] # Returns "80"

#   Exercise 1e:
#       In Exercise 1d, you stored the frequency of each letter in the Gettysburg Address is in address_count. Use this dictionary to find the most common letter in the Gettysburg address.
#       What is the most frequent letter in the Gettysburg Address?
#   Solution:
        maximum = 0
        most_frequent_letter = ""
        for letter in address_count:
            if address_count[letter] > maximum:
                maximum = address_count[letter]
                most_frequent_letter = letter
        print(most_frequent_letter) # Returns "e"

############
# EXERCISE 2
############
# Consider a circle inscribed in a square. The ratio of their areas (the ratio of the area of the circle to the area
# of the square) is   π4  . In this six-part exercise, we will find a way to approximate this value
#   Exercise 2a:
#       Using the math library, calculate and print the value of  π4 .
#       What is the value of  π4 ?
#   Solution:
        import math
        round(math.pi/4, 6) # Returns "0.785398"

#   Exercise 2b:
#       Using random.uniform(), create a function rand() that generates a single float between −1 and 1.
#       Call rand() once. For us to be able to check your solution, we will use random.seed() to fix the seed value of
#       the random number generator.
#       We include some sample code to get you started:
#               import random
#               random.seed(1) # Fixes the seed of the random number generator.
#               def rand():
#                  # define `rand` here!
#               rand()
#       What is the value you get from calling rand()?
#   Solution:
        import random
        random.seed(1) # Fixes the seed of the random number generator.
        def rand():
           return random.uniform(-1, 1)
        rand()

#   Exercise 2c:
#       The distance between two points x and y is the square root of the sum of squared differences along each
#       dimension of x and y. Write a function distance(x, y) that takes two vectors as its input and outputs the
#       distance between them. Use your function to find the distance between 𝑥=(0,0) and 𝑦=(1,1).
#    Solution:
        def distance(x, y):
            return math.sqrt((x[0] - y[0])*2 + (x[1] - y[1])*2)
        distance((0,0),(1,1))

#   Exercise 2d:
#       Write a function in_circle(x, origin) that determines whether a point in a two dimensional plane falls within a
#       unit circle surrounding a given origin.
#       Your function should return a boolean True if the distance between x and origin is less than 1 and False
#       otherwise.
#       Use distance(x, y) as defined in Exercise 2c.
#       Use your function to determine whether the point (1,1) lies within the unit circle centered at (0,0):
#           def in_circle(x, origin = [0,0]):
#               # Define your function here!
#       Does the point (1,1) lie within the unit circle centered at (0,0)?
#   Solution:
        def in_circle(x, origin=[0, 0]):
            if len(x) != 2:
                return "x is not two-dimensional!"
            elif distance(x, origin) < 1:
                return True
            else:
                return False
        in_circle((1, 1)) # Returns "False"

#   Exercise 2e:
#       Create a list inside of R=10000 booleans that determines whether or not a point falls within the unit circle
#       centered at (0,0).
#       Set the seed to 1 using random.seed(1).
#       Use the rand function from Exercise 2b to generate R randomly located points.
#       Use the function in_circle to test whether or not a given pint falls within the unit circle.
#       Find the proportion of points that fall within the circle by summing all True values in the inside list; then
#       divide the answer by R to obtain a proportion.
#       Print your answer. This proportion is an estimate of the ratio of the two areas!
#       What is the proportion of points within the unit circle?
#   Solution:
        inside = []
        R = 10000
        random.seed(1) # Fixes the seed of the random number generator.
        for i in range(R):
            point = [rand(), rand()]
            inside.append(in_circle(point))

        sum(inside)/R # Returns "0.779"

#   Exercise 2f:
#       Calculate the difference between your estimate from Exercise 2e and math.pi / 4. Note: inside and R are defined
#       as in Exercise 2e.
#       What is the difference between our estimate from 2e and the true value of  π4?
#   Solution:
        0.785398 - 0.779 # Returns "0.006398000000000015"

############
# EXERCISE 3
############
# A list of numbers representing measurements obtained from a system of interest can often be noisy. One way to deal with noise to smoothen the values by replacing each value with the average of the value and the values of its neighbors.
#
#   Exercise 3a:
#       Write a function moving_window_average(x, n_neighbors) that takes a list x and the number of neighbors
#       n_neighbors on either side of a given member of the list to consider.
#       For each value in x, moving_window_average(x, n_neighbors) computes the average of the value and the values of
#       its neighbors.
#       moving_window_average should return a list of averaged values that is the same length as the original list.
#       If there are not enough neighbors (for cases near the edge), substitute the original value for a neighbor for
#       each missing neighbor.
#       Use your function to find the moving window sum of x=[0,10,5,3,1,5] and n_neighbors=1.
#   Solution:
        def moving_window_average(x, n_neighbors=1):
            n = len(x)
            width = n_neighbors*2 + 1
            x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
            means = []
            for i in range(n):
                sum_window = 0
                for element in x[i: i + width]:
                    sum_window += element
                means.append(sum_window / width)
            return means

        x = [0,10,5,3,1,5]
        print(moving_window_average(x, 1))

#   Exercise 3b:
#       Compute and store R=1000 random values from 0-1 as x.
#       Compute the moving window average for x for values of n_neighbors ranging from 1 to 9 inclusive.
#       Store x as well as each of these averages as consecutive lists in a list called Y.
#       Use this code to get started:
#           random.seed(1) # This line fixes the value called by your function,
#                # and is used for answer-checking.
#           # write your code here!
#       What is the moving window average for the 10th entry in x for n_neighbors = 5?
#   Solution:
        random.seed(1)  # This line fixes the value called by your function, and is used for answer-checking.
        R = 1000
        x = [random.random() for i in range(R)]
        Y = [x] + [moving_window_average(x, i) for i in range(1, 10)]
        Y[5][9] # Returns "0.45325045824763405"

#   Exercise 3c:
#       For each list in Y, calculate and store the range (the maximum minus the minimum) in a new list ranges.
#       Print your answer. As the window width increases, does the range of each list increase or decrease? Why do you
#       think that is?
#       As window width increases, does the range of each list increase or decrease?
#   Solution:
        ranges = [max(x) - min(x) for x in Y]
        print(ranges) # decrease