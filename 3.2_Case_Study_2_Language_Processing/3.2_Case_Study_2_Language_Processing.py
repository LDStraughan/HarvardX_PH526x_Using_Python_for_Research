###########################################
# 3.2.1 INTRODUCTION TO LANGUAGE PROCESSING
###########################################
# Let's examine properties of individual books from various authors & languages:
#       - Book Lengths
#       - Number of unique words
#       - How these cluster by language/authorship

# Project Gutenberg (gutenberg.org) - Oldest digital library of books

# Several Nested Folders in Download:
#       1) Languages: English, French, German, & Portuguese
#       2) Authors: 1 - 4 Authors per Language (13 in total)
#       3) Books: 1- 16 Books per Author (102 in total)
#   Some authors appear in several language categories

# Goal = Write a function that, given a string of text, counts the number of times each unique word appears
# Use Dictionary - Keys = Strings of unique words; Values = Integers that count no. of time word appears

##################################################
# 3.2.1 INTRODUCTION TO LANGUAGE PROCESSING - Quiz
##################################################
# Question 1: What is Project Gutenberg?
# Solution 1: An online repository of publically available books in many languages

######################
# 3.2.2 COUNTING WORDS
######################
# Helpful to create a test string:
text = "This is my test text. We're keeping this text short to keep things manageable."

def count_words(text): # Create function
    # Docstring
    """Count the number of times each word occurs in text (str). Return dictionary where keys are unique words and values are word counts."""
    word_counts = {} # Create dictionary
    for word in text.split(" "): # Break the text down into words
        # known word
        if word in word_counts:
            word_counts[word] += 1  # If we've already seen the word, increase counter by 1
        # unknown word
        else:
            word_counts[word] = 1 # If this is the first time seeing the word, set counter to 1
    return word_counts
count_words(text) # Problems: registers punctuation as part of a word, and capitals as separate words to lowercase

def count_words(text): # Create function
    # Docstring
    """Count the number of times each word occurs in text (str). Return dictionary where keys are unique words and values are word counts. Skip punctuation."""
    text = text.lower() # Convert everything to lowercase
    skips = [".", ",", ";", ":", '"'] # List of punctuation that we want to skip - use single quotes around double quote
    for ch in skips:
        text = text.replace(ch, "") # Replace punctuation in 'skips' list with empty string
    word_counts = {} # Create dictionary
    for word in text.split(" "): # Break the text down into words
        # known word
        if word in word_counts:
            word_counts[word] += 1  # If we've already seen the word, increase counter by 1
        # unknown word
        else:
            word_counts[word] = 1 # If this is the first time seeing the word, set counter to 1
    return word_counts
count_words(text)

# Counting objects in Python is so common that there is a counter tool to support rabbit tallies:
from collections import Counter

def count_words_fast(text): # Create new function with Counter
    # Docstring
    """Count the number of times each word occurs in text (str). Return dictionary where keys are unique words and values are word counts. Skip punctuation."""
    text = text.lower() # Convert everything to lowercase
    skips = [".", ",", ";", ":", '"'] # List of punctuation that we want to skip - use single quotes around double quote
    for ch in skips:
        text = text.replace(ch, "") # Replace punctuation in 'skips' list with empty string
    word_counts = Counter(text.split(" ")) # This line does everything the for loop did above
    return word_counts
count_words_fast(text)

count_words(text) == count_words_fast(text) # Are these objects the same? - Returns "True"

#############################
# 3.2.2 COUNTING WORDS - Quiz
#############################
# Question 1: The function count_words is as defined in Video 3.2.2.
#             Consider the following code:
#               len(count_words("This comprehension check is to check for comprehension."))
#             What does this return?
# Solution 1:
len(count_words("This comprehension check is to check for comprehension.")) # Returns "6"

# Question 2: The functions count_words and count_words_fastare as defined in Video 3.2.2. Consider the following code:
#               count_words(text) is count_words_fast(text)
#             What does this return?
# Solution 2:
count_words(text) is count_words_fast(text) # Returns "False" - While the two provide the same results, they are
                                                              # different objects in memory.

######################
# 3.2.3 READING A BOOK
######################
# Character Encoding = Process how computer encodes certain characters
# Here, we'll use UTF-8 encoding = Dominant character encoding for the web

def read_book(title_path): # Define function
    # Docstring
    """Read a book and return it as a string."""
    with open(title_path, "r", encoding = "utf8") as current_file: # Reading with 'with' statement is smarter
        text = current_file.read() # Read file and store it in 'text' object
        text = text.replace("\n", "").replace("\r","") # Can train 2nd replace method immediately after 1st
    return text # Return 'text' object to the caller

text = read_book("./Books/English/shakespeare/Romeo and Juliet.txt")
len(text) # Returns "169275" - That's characters

ind = text.find("What's in a name?") # Returns an index if it finds the substring
ind # Returns "42757"
sample_text = text[ind : ind+17] # Extract sample text
sample_text # Returns ""What's in a name?""

###########################################
# 3.2.4 COMPUTING WORD FREQUENCY STATISTICS
###########################################
# We want to know how many UNIQUE WORDS are in a given book and the FREQUENCY each word appears
def word_stats(word_counts): # Define function
    # Docstring
    """Return number of unique words and word frequencies."""
    num_unique = len(word_counts) # Length of dictionary returns no. of unique words, each entry in dictionary is unique
    counts = word_counts.values() # Extract values from dictionary
    return (num_unique, counts) # Return tuple containing both objects

# Test on English version of Romeo & Juliet:
text = read_book("./Books/English/shakespeare/Romeo and Juliet.txt") # Read in the book
word_counts = count_words(text) # Count the words in the book
(num_unique, counts) = word_stats(word_counts) # Return number of unique words and frequencies
num_unique # Returns "5224"
sum(counts) # How many words are there in total? - Returns "40776"
print(num_unique, sum(counts)) # Returns "5224 40776"

# Compare with the German version of Romeo & Juliet:
text = read_book("./Books/German/shakespeare/Romeo und Julia.txt") # Read in the book
word_counts = count_words(text) # Count the words in the book
(num_unique, counts) = word_stats(word_counts) # Return number of unique words and frequencies
num_unique # Returns "7543"
sum(counts) # How many words are there in total? - Returns "20311"
print(num_unique, sum(counts)) # Returns "7543 20311"

##################################################
# 3.2.4 COMPUTING WORD FREQUENCY STATISTICS - Quiz
##################################################
# Question 1: As defined in Video 3.2.4, which of the following does the function word_stats return?
# Solution 1: The number of unique words AND A list of word counts

# Question 2: Which of the two versions of Romeo and Juliet from Project Gutenberg contains more unique words,
            # the original or the German translation?
# Solution 2: The German translation

##############################
# 3.2.5 READING MULTIPLE FILES
##############################
# Navigating file directories is an important skill

# Goal = Read every book contained in various subdirectories of our 'Book' folder
import os # Help us read directories
book_dir = "./Books" # Keep track of 'Book' directory
os.listdir(book_dir) # Returns "['English', 'French', 'German', 'Portuguese']"

# Generate a list of directories contained within 'Books" directory:
for language in os.listdir(book_dir): # Loop over each language in the 'Book' directory
    for author in os.listdir(book_dir + "/" + language): # Loop over authors in each language - Concatenating is helpful
        for title in os.listdir(book_dir + "/" + language + "/" + author): # Loop over titles in each author
            inputfile = book_dir + "/" + language + "/" + author + "/" + title # Store full path for each book
            print(inputfile) # Print just to see that the function is working properly
            text = read_book(inputfile) # Read in the book
            (num_unique, counts) = word_stats(count_words(text)) # Feed text into count_words function, returning object
                                                                 # that is turned into a tuple, which is then unpacked
                                                                 # into num_unique and counts

# Pandas = Library that provides additional data structures and data analysis functionalities for Python
# Especially useful for manipulating numerical tables and time series data
# Pandas gets its name from PANel DAta - referring to multi-dimensional structured data sets
import pandas as pd # import pandas
table = pd.DataFrame(columns = ("name", "age")) # DataFrame is most common data structure in pandas
# Add new entries to our table based on location of said entries
table.loc[1] = "James", 22 # Row 1 of table = Name (so it has to be a string), Age
table.loc[2] = "Jess", 32 # Row 2 of table = Name (so it has to be a string), Age
table # Returns "    name age
               # 1  James  22
               # 2   Jess  32"

# Use Pandas DF to keep track of book statistics:
import os # Help us read directories
book_dir = "./Books" # Keep track of 'Book' directory

import pandas as pd # Import pandas
book_stats = pd.DataFrame(columns = ("Language", "Author", "Title", "Length", "Unique")) # Create empty DF with 5 cols
title_num = 1 # Need to keep track of the row of the table

for language in os.listdir(book_dir): # Loop over each language in the 'Book' directory
    for author in os.listdir(book_dir + "/" + language): # Loop over authors in each language - Concatenating is helpful
        for title in os.listdir(book_dir + "/" + language + "/" + author): # Loop over titles in each author
            inputfile = book_dir + "/" + language + "/" + author + "/" + title # Store full path for each book
            print(inputfile) # Print just to see that the function is working properly
            text = read_book(inputfile) # Read in the book
            (num_unique, counts) = word_stats(count_words(text)) # Feed text into count_words function, returning object
                                                                 # that is turned into a tuple, which is then unpacked
                                                                 # into num_unique and counts
            book_stats.loc[title_num] = language, author, title, sum(counts), num_unique # Insert the elements we want
            title_num += 1 # Increase counter by 1 every time
book_stats # Returns object with [102 rows x 5 columns]
book_stats.head() # Prints top 5 lines - Returns "  Language       Author                          Title Length Unique
                                                # 1  English  shakespeare  A Midsummer Night's Dream.txt  16103   4345
                                                # 2  English  shakespeare                     Hamlet.txt  28551   6776
                                                # 3  English  shakespeare                    Macbeth.txt  16874   4780
                                                # 4  English  shakespeare                    Othello.txt  26590   5898
                                                # 5  English  shakespeare                Richard III.txt  48315   5535"
book_stats.tail() # Prints bot 5 - Returns "        Language       Author                       Title  Length Unique
                                           # 98   Portuguese      Queir¢s  O crime do padre Amaro.txt  128630  29311
                                           # 99   Portuguese      Queir¢s              O Mandarim.txt   21440   7839
                                           # 100  Portuguese      Queir¢s         O Primo Bazilio.txt  107303  27654
                                           # 101  Portuguese      Queir¢s                Os Maias.txt  195771  40680
                                           # 102  Portuguese  shakespeare                  Hamlet.txt   30567   9704"

# Modifications:
#       1) Capitalise Authors
#       2) Get rid of .txt at the end of titles
import os # Help us read directories
book_dir = "./Books" # Keep track of 'Book' directory

import pandas as pd # Import pandas
book_stats = pd.DataFrame(columns = ("Language", "Author", "Title", "Length", "Unique")) # Create empty DF with 5 cols
title_num = 1 # Need to keep track of the row of the table

for language in os.listdir(book_dir): # Loop over each language in the 'Book' directory
    for author in os.listdir(book_dir + "/" + language): # Loop over authors in each language - Concatenating is helpful
        for title in os.listdir(book_dir + "/" + language + "/" + author): # Loop over titles in each author
            inputfile = book_dir + "/" + language + "/" + author + "/" + title # Store full path for each book
            print(inputfile) # Print just to see that the function is working properly
            text = read_book(inputfile) # Read in the book
            (num_unique, counts) = word_stats(count_words(text)) # Feed text into count_words function, returning object
                                                                 # that is turned into a tuple, which is then unpacked
                                                                 # into num_unique and counts
            # Make Modifications Here: (to author and title)
            book_stats.loc[title_num] = language, author.capitalize(), title.replace(".txt", ""), sum(counts), num_unique
            title_num += 1 # Increase counter by 1 every time
book_stats.head() # Returns "  Language       Author                      Title Length Unique
                           # 1  English  Shakespeare  A Midsummer Night's Dream  16103   4345
                           # 2  English  Shakespeare                     Hamlet  28551   6776
                           # 3  English  Shakespeare                    Macbeth  16874   4780
                           # 4  English  Shakespeare                    Othello  26590   5898
                           # 5  English  Shakespeare                Richard III  48315   5535"

#####################################
# 3.2.5 READING MULTIPLE FILES - Quiz
#####################################
# Question 1: What type of object does os.listdir return?
# Solution 1: list

# Question 2: What pandas method allows you to insert a row to a dataframe?
# Solution 2: loc

# Question 3: How can you increase a numerical title_num value by 1?
# Solution 3: title_num += 1

# Question 4: How can you retrieve the first and last few rows of a pandas dataframe called stats?
# Solution 4: stats.head() and stats.tail()

################################
# 3.2.6 PLOTTING BOOK STATISTICS
################################
# Extract columns from DF using names of the columns
book_stats.Length # Gives access to 'Length' column
book_statas.Unique # Gives access to 'Unique' column

# Let's Make Some Plots:
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid') # Use a nice style

plt.scatter(book_stats.Length, book_stats.Unique) # X-axis = Length of book in words; Y-axis = No. of unique words

plt.loglog(book_stats.Length, book_stats.Unique, "bo") # Plot both axes logarithmically

book_stats[book_stats.Language == "English"] # Print all of the books that we have in English

# Plt uses the same names for colours at HTML

# Create Figure:
plt.figure(figsize = (10,10))
# English:
subset = book_stats[book_stats.Language == "English"]
plt.loglog(subset.Length, subset.Unique, "o", label = "English", color = "crimson")
# French:
subset = book_stats[book_stats.Language == "French"]
plt.loglog(subset.Length, subset.Unique, "o", label = "French", color = "forestgreen")
# German:
subset = book_stats[book_stats.Language == "German"]
plt.loglog(subset.Length, subset.Unique, "o", label = "German", color = "orange")
# Portuguese:
subset = book_stats[book_stats.Language == "Portuguese"]
plt.loglog(subset.Length, subset.Unique, "o", label = "Portuguese", color = "blueviolet")
# Legend:
plt.legend()
plt.xlabel("Book Length")
plt.ylabel("No. of Unique Words")
plt.savefig("lang_plot.png")

#######################################
# 3.2.6 PLOTTING BOOK STATISTICS - Quiz
#######################################
# Question 1: book_stats is a Pandas dataframe as defined in Video 3.2.6. Which of the following options are valid ways
            # to access the column "Length" in this dataframe? (Select all that apply.)
# Solution 1:
book_stats.Length
book_stats["Length"]

# Question 2: book_stats is a Pandas dataframe as defined in Video 3.2.6. How can you select only the rows where the
            # language is French?
# Solution 2:
book_stats[book_stats.Language == "French"]