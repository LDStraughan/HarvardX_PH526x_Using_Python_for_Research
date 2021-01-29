###################################
# 4.1.1 GETTING STARTED WITH PANDAS
###################################
# Classify scotch whiskies based on flavour characteristics
# Attempt to cluster whiskies into groups that are similar in flavour
# Dataset contains whiskies from several distilleries
# Has tasting ratings of one single malt scotch whisky from almost every active whisky distillery in Scotland
        # 86 Malt Whiskies
        # Scored between 0-4
        # From 10 tasters
        # 12 taste categories
            # E.g. Sweet, smoky, medicinal, spicy, etc.

# Pandas = Provides data structures & functions for working with structured data (primarily tabular data)
# Pandas is built on top of NumPy
# 2 Basic Structures:
#       1) Series - 1-D array-like object
#       2) Data Frame - 2-D array-like object
#       Both contain metadata - additional info about data

# Series:
import pandas as pd
x = pd.Series([6,3,8,6])
x # Right column = Data Array; Left column = Index (Array of Data Labels) - This is the default Index
x = pd.Series([6,3,8,6], index=["q", "w", "e", "r"]) # Specify the Index
x # Index has been specified
x["w"] # Returns "3"
x[["r", "w"]] # Returns "r    6
                       # w    3"
# Common way of constructing a Series object is by passing a Dictionary
age = {"Tim":29, "Jim":31, "Pam":27, "Sam":35}
x = pd.Series(age) # Use 'age' Dictionary to create Series
x # Returns "Tim    29
           # Jim    31
           # Pam    27
           # Sam    35" - Index = Dictionary Keys

# Data Frames:
# Represent table-like data - have row and column index
# Common way of constructing a Data Frame object is by passing a Dictionary - Values = List/NumPy Arrays of equal length
data = {'name': ['Tim', 'Jim', 'Pam', 'Sam'],
        'age': [29, 31, 27, 35],
        'ZIP': ['02115', '02130', '67700', '00100']}
x = pd.DataFrame(data, columns=["name", "age", "ZIP"])
x # Returns "  name  age    ZIP
           # 0  Tim   29  02115
           # 1  Jim   31  02130
           # 2  Pam   27  67700
           # 3  Sam   35  00100" - We didn't specify an Index
x["name"] # Both return the same thing
x.name # Both return the same thing

# We often need to re-index a Series or Data Frame object to re-order the data in the object
x = pd.Series([6,3,8,6], index=["q", "w", "e", "r"])
x.index # Returns "Index(['q', 'w', 'e', 'r'], dtype='object')"
sorted(x.index) # Returns "['e', 'q', 'r', 'w']"
x.reindex(sorted(x.index)) # Argument = Array or List of New Indices

# Series & DF object support arithmetic operations like addition
# If we add 2 Series objects together, entries with the same index are added together
# If indices don't match, Pandas introduces NaN (not a number object)
x = pd.Series([6,3,8,6], index=["q", "w", "e", "r"])
y = pd.Series([7,3,5,2], index=["e", "q", "r", "t"])
x + y # Returns "e    15.0
               # q     9.0
               # r    11.0
               # t     NaN
               # w     NaN" - Both have e, q & r; Only 1 has t or w
# Arithmetic works the same way for Data Frames

##########################################
# 4.1.1 GETTING STARTED WITH PANDAS - Quiz
##########################################
# Question 1: What is Pandas?
# Solution 1: A Python library designed to query and manipulate annotated data tables

# Question 2: What keyword allows you to specify names to indices in a pd.Series?
# Solution 2: index

# Question 3: In pandas, what does the reindex method do?
# Solution 3: Reorders the indices of a pandas Series object according to its argument

#################################
# 4.1.2 LOADING & INSPECTING DATA
#################################
# Let's inspect whiskies.txt & regions.txt
import numpy as np
import pandas as pd

# CSV file = Comma Separated Values file - Entries in each row are separated by commas
whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt") # Add into 'whisky' object as new column
whisky.head() # First 5 rows of Data Frame
whisky.tail() # Last 5 rows of Data Frame

# iloc method = Index a data frame by Location
whisky.iloc[0:10] # Specify the first 10 Rows
whisky.iloc[5:10, 0:5] # Rows 5-10 (RowID 6-10); Columns = 0-5 (1-5)
whisky.columns
flavours = whisky.iloc[:, 2:14]
flavours

########################################
# 4.1.2 LOADING & INSPECTING DATA - Quiz
########################################
# Question 1: What command reads in csv files in pandas?
# Solution 1: pd.read_csv

##############################
# 4.1.3 EXPLORING CORRELATIONS
##############################
# Find out correlations between different flavour attributes
# Use 'corr' function to compute correlations across columns of a DF
# Pearson correlation = Estimates linear correlations in the data - Straight, upward line in scatter plot
corr_flavours = pd.DataFrame.corr(flavours) # Find correlations between flavours & store in object
corr_flavours_col = ['Body', 'Sweetness', 'Smoky', 'Medicinal', 'Tobacco', 'Honey', 'Spicy', 'Winey', 'Nutty', 'Malty', 'Fruity', 'Floral']
import matplotlib.pyplot as plt
plt.style.use("bmh")
plt.figure(figsize=(10,10)) # 10x10 figure (large)
plt.title("Whisky Flavour Correlation")
plt.pcolor(corr_flavours)
plt.colorbar()
plt.xticks(np.arange(12), corr_flavours_col, rotation=90)
plt.yticks(np.arange(12), corr_flavours_col)
plt.gcf().subplots_adjust(bottom=0.12,left=0.12)
plt.savefig("corr_flavours.png")
# Smoky & Medicinal are very close
# Floral Flavour is the opposite of Body (Full Body), Smoky & Medicinal

# Look at the correlation among Whiskies across Flavours - Correlation between different Distilleries
corr_whisky = pd.DataFrame.corr(flavours.transpose())
plt.style.use("bmh")
plt.figure(figsize=(500,500)) # 10x10 figure (large)
plt.title("Whisky Correlation")
plt.pcolor(corr_whisky)
plt.axis("tight")
plt.colorbar()
plt.gcf().subplots_adjust(bottom=0.12,left=0.12)
plt.savefig("corr_whisky.png")

#####################################
# 4.1.3 EXPLORING CORRELATIONS - Quiz
#####################################
# Question 1: How can you find a correlation matrix of a pd.Dataframe?
# Solution 1: pd.DataFrame.corr

# Question 2: How can you plot a correlation matrix by color?
# Solution 2: plt.pcolor

# Question 3: What is the matplotlib.pyplot function that plots a colorbar on the side of a plot?
# Solution 3: plt.colorbar()

##############################################
# 4.1.4 CLUSTERING WHISKIES BY FLAVOUR PROFILE
##############################################
# Spectral Co-Clustering = Simultaneously find two sets of clusters (eigenvalues/eigenvectors)
from sklearn.cluster.bicluster import SpectralCoclustering as scc
model = scc(n_clusters=6, random_state=0)
model.fit(corr_whisky)
model.rows_ # Array with n_row clusters * n_rows in the correlation matrix - True or False
np.sum(model.rows_, axis=1) # 0 = rows, 1 = columns - Returns "array([ 5, 20, 19,  6, 19, 17])" - Clusters 0-5
model.row_labels_ # Numbers indicate which cluster it belongs to

#####################################################
# 4.1.4 CLUSTERING WHISKIES BY FLAVOUR PROFILE - Quiz
#####################################################
# Question 1: What is spectral co-clustering?
# Solution 1: A method for finding clusters of objects by the similarity of their attributes

# Question 2: How many clusters do we find in the whisky dataset used in Video 4.1.4?
# Solution 2: 6

######################################
# 4.1.5 COMPARING CORRELATION MATRICES
######################################
# Draw clusters as groups discovered in 'whisky' df
# Also, rename indices to match the sorting
        # 1st) Extract group labels from the model, append them to whisky table & specify index
        # 2nd) Reorder the rows in increasing order by group labels (Cluster 0-5)
        # 3rd) Reset index of Data Frame
whisky["Group"] = pd.Series(model.row_labels_, index=whisky.index) # 1st
whisky = whisky.iloc[np.argsort(model.row_labels_)] # 2nd
whisky = whisky.reset_index(drop=True) # 3rd
correlations = pd.DataFrame.corr(whisky.iloc[:, 2:14].transpose()) # Recalculate the correlation matrix
correlations = np.array(correlations) # Turn into NumPy array

# Plot original correlations (corr_whiky) with recalculated correlations (correlations)
plt.style.use("classic")
plt.figure(figsize=(14,7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title("Original")
plt.axis("tight")
plt.subplot(122)
plt.pcolor(correlations)
plt.title("Rearranged")
plt.axis("tight")
plt.savefig("correlations.png")

#############################################
# 4.1.5 COMPARING CORRELATION MATRICES - Quiz
#############################################
# Question 1: Consider the following code:
#                       import pandas as pd
#                       data = pd.Series([1,2,3,4])
#                       data = data.ix[[3,0,1,2]]
#             What does data[0] return? Why?
# Solution 1:
              import pandas as pd
              data = pd.Series([1,2,3,4])
              data = data.iloc[[3,0,1,2]] # Changed ix to iloc because ix has been depricated
              data[0] # 1: data.iloc alters the order of appearance, but leaves the indices the same.

# Question 2: Consider the following code:
#                       import pandas as pd
#                       data = pd.Series([1,2,3,4])
#                       data = data.ix[[3,0,1,2]]
#                       data = data.reset_index(drop=True)
#             What does data[0] return? Why?
# Solution 2:
              import pandas as pd
              data = pd.Series([1,2,3,4])
              data = data.iloc[[3,0,1,2]] # Changed ix to iloc because ix has been depricated
              data = data.reset_index(drop=True)
              data[0] # 4: The 0th index of the data has been reordered to index 3 of the original, which is 4.