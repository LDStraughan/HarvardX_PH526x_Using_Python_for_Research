##########################################
# 3.3.1 INTRODUCTION TO KNN CLASSIFICATION
##########################################
# Statistical Learning = Collection of mathematical & computational tools to understand data
# Supervised Learning = Goal is to estimate or predict an output based on one or more inputs
# Inputs = Predictors; Independent Variables; Features; Variables; etc.
# Outputs = Response Variables/Dependent Variables
# Regression Problems = Quantitative results (numbers)
# Classification Problems = Qualitative results (words)

# This Case Study's Goal = Set up classifier such that when it's presented with a new observation whose category is
                         # unknown, it will attempt to assign that observation to a category/class.
# kNN = k-Nearest Neighbour
#       Given a positive integer k and a new data point, it first identifies those k points in the data that are nearest
#       to the point and classifies the new data point as belonging to the most common class among those k neighbours.

#################################################
# 3.3.1 INTRODUCTION TO KNN CLASSIFICATION - Quiz
#################################################
# Question 1: How does the  k -Nearest Neighbors classifier classify observations?
# Solution 1: According to the most common class among the nearest  k  neighbors

###############################################
# 3.3.2 FINDING THE DISTANCE BETWEEN TWO POINTS
###############################################
# Write a Function that takes 2 points and computes the distance between them
# Distance = Euclidean distance (solid geometry)
# Pythagorean theorem: d**2 = (x2-x1)**2 + (y2-y1)**2
# Pythagorean theorem: d = sqrt((x2-x1)**2 + (y2-y1)**2)

# Use NumPy for Vectors
# Row vectors are easier to deal with in NumPy than Column vectors
import numpy as np
p1 = np.array([1,1]) # Define data point 1
p2 = np.array([4,4]) # Define data point 2
p2 - p1 # Returns "array([3, 3])"
np.power(p2-p1, 2) # Raise to the power of 2 # Returns "array([9, 9], dtype=int32)"
np.sqrt(np.sum(np.power(p2-p1, 2))) # Sum & square root it # Returns "4.242640687119285" - Pythagorean theorem

# Define function for Pythagorean theorem:
def distance(p1,p2):
    """Find the distance between p1 and p2."""
    return np.sqrt(np.sum(np.power(p2 - p1, 2))) # Pythagorean theorem

p1 = np.array([1, 1])  # Define data point 1
p2 = np.array([4, 4])  # Define data point 2
distance(p1, p2) # Returns "4.242640687119285"

######################################################
# 3.3.2 FINDING THE DISTANCE BETWEEN TWO POINTS - Quiz
######################################################
# Question 1: How is the distance measure we use (as in Video 3.3.2) defined between points (a1, b1) and (a2, b2)?
# Solution 1: sqrt((a1−a2)**2+(b1−b2)**2)

#####################
# 3.3.3 MAJORITY VOTE
#####################
# Majority Vote = Given an array or sequence of votes (e.g. 1, 2, 3), we need to determine how many times each occurs &
# then find most common event.
# What is actually determined is the Plurality Vote, because the most common vote does not need to represent a majority
# of votes. We have used the standard naming convention of majority vote here.

# Build a Majority Vote Function:
# It's very much like our count words function

def majority_vote(votes):
    """Count the votes and return observation with the highest count."""
    vote_counts = {} # Create Dictionary - Keys = Observations; Values = No. of times observation was voted for
    for vote in votes:              # Have we seen this vote before?
        if vote in vote_counts:     # Yes:
            vote_counts[vote] += 1      # Increase counter by 1
        else:                       # No:
            vote_counts[vote] = 1       # Add vote to counter
    return vote_counts

votes = [1,2,3,1,2,3,1,2,3,3,3,3]
vote_counts = majority_vote(votes)
max(vote_counts.keys()) # Which observation occurred the most? - same as max(vote_counts) - Returns "3"
max(vote_counts.values()) # How many votes does the top observation have?  - Returns "6"

# Items Method in Dictionaries:
winners = [] # Keep track of keys that correspond to the highest values
max_count = max(vote_counts.values()) # Keep track of the amount of votes (values) that the winners have
for vote, count in vote_counts.items():
    if count == max_count: # Does the current entry have the maximum number of votes?
        winners.append(vote) # If so, append the vote/observation to 'winners' list
    print(vote, count) # Prints the key and the value point associated with the key as a tuple

# Final Function:
import random # If we have a tie, we want to pick one at random
def majority_vote(votes):
    """Count the votes and return observation with the highest count."""
    vote_counts = {} # Create Dictionary - Keys = Observations; Values = No. of times observation was voted for
    for vote in votes:              # Have we seen this vote before?
        if vote in vote_counts:     # Yes:
            vote_counts[vote] += 1      # Increase counter by 1
        else:                       # No:
            vote_counts[vote] = 1       # Add vote to counter
    winners = []  # Keep track of keys that correspond to the highest values
    max_count = max(vote_counts.values())  # Keep track of the amount of votes (values) that the winners have
    for vote, count in vote_counts.items():
        if count == max_count:  # Does the current entry have the maximum number of votes?
            winners.append(vote)  # If so, append the vote/observation to 'winners' list
    return random.choice(winners) # If there's a tie, pick one at random
votes = [1,2,3,1,2,3,1,2,3,3,3,3,2,2,2]
winner = majority_vote(votes)
winner # Returns "2" - It was a tie between 2 & 3

# Mode = Most commonly occurring element in a sequence
# Let's find the Mode:
import scipy.stats as ss
def majority_vote_short(votes):
    """Return the most common element in votes."""
    mode, count = ss.mstats.mode(votes)
    return mode
votes = [1,2,3,1,2,3,1,2,3,3,3,3,2,2,2]
winner = majority_vote(votes)
winner # Returns "2" - It will always return number 2

############################
# 3.3.3 MAJORITY VOTE - Quiz
############################
# Question 1: What does the items method for dictionaries return?
# Solution 1: A dict_items object with elements consisting of tuples of key, value pairs

# Question 2: What will random.choice() return for a list containing only one object? (Assume that the random module has
            # already been imported.)
# Solution 2: This code returns the single element every time.

##################################
# 3.3.4 FINDING NEAREST NEIGHBOURS
##################################
# Identifying the Nearest Neighbours:

# loop over all points
    # compute the distance between point p and every other point
# sort distances and return those k points that are nearest to p

points = np.array([[1,1], [1,2], [1,3], [2,1], [2,2] ,[2,3], [3,1], [3,2], [3,3]]) # Test data set - array expect 1 list
p = np.array([2.5, 2]) # Define point 'p'

import matplotlib.pyplot as plt
plt.style.use('bmh') # This is a really nice style!!
plt.plot(points[:,0],points[:,1], "o") # x = all the rows in column 0; y = all the rows in column 1; use green circles
plt.plot(p[0], p[1], "o") # Plot 'p'

distances = np.zeros(points.shape[0]) # Empty array to hold all our distances - same no. of elements as rows in 'points'
for i in range(len(distances)): # Loop as many times as there are distances
    distances[i] = distance(p, points[i]) # 'i' in 'distances' will be the distance between p and 'i' in 'points'
distances
points[4] # Returns "array([2, 2])"
distances[4] # Returns "0.5" - Distance between point[4] and 'p'
points[7] # Returns "array([3, 2])"
distances[7] # Returns "0.5" - Distance between point[7] and 'p'

# We can sort the distances array to give shorter distances
# Instead, we want a vector that would sort the array - We can take the first k elements of that array and know the
# corresponding points are th K Nearest Neighbours
# np.argsort does this ^^
ind = np.argsort(distances) # Sort distances and store them in 'ind'
ind # An array of indices - Returns "array([4, 7, 3, 5, 6, 8, 1, 0, 2], dtype=int64)"
distances[ind] # Extract elements in distances at locations given by 'ind'
distances[ind[0:2]] # 2 nearest points - Returns "array([0.5, 0.5])"

def find_nearest_neighbours(p, points, k=5): # If user only specifies p and points, Python will use 5 for k
    """Find the k nearest neighbours of point p and return their indices."""
    distances = np.zeros(points.shape[0])  # Empty array to hold our distances - same no. elements as rows in 'points'
    for i in range(len(distances)):  # Loop as many times as there are distances
        distances[i] = distance(p, points[i])  # 'i' in 'distances' will be the distance between p and 'i' in 'points'
    ind = np.argsort(distances)
    return ind[:k] # Return first 'k' elements
ind = find_nearest_neighbours(p, points, 2); print(points[ind]) # Returns "[[2 2]
                                                                            # [3 2]]"

# Define knn Prediction Function:
def knn_predict(p, points, outcomes, k=5): # outcomes argument = classes to which k points belong
    ind = find_nearest_neighbours(p, points, k) # find knn
    return majority_vote(outcomes[ind])# predict the class of p based on majority vote

outcomes = np.array([0,0,0,0,1,1,1,1,1])
len(outcomes) # Returns "9"
knn_predict(np.array([2.5, 2.7]), points, outcomes, k=2) # Returns "1"
knn_predict(np.array([1.0, 2.7]), points, outcomes, k=2) # Returns "0"

#########################################
# 3.3.4 FINDING NEAREST NEIGHBOURS - Quiz
#########################################
# Question 1: For an np.array of dimension 2, what does the shape method return?
# Solution 1: A tuple containing the number of rows and columns

# Question 2: What does np.argsort do?
# Solution 2: It sorts an array according to a single argument and returns the sorted indices.

#################################
# 3.3.5 GENERATING SYNTHETIC DATA
#################################
#  Write a Function that generates 2 points, where 1st end points are from class 0, and 2nd end points are from class 1
# Considered SYNTHETIC DATA ^^
# Bivariates = 2 variables
# Use scipy stats module
ss.norm(0,1).rvs((5,2)) # Random variables with 5 rows and 2 columns in normal distribution - mean = 0; sd = 1
ss.norm(0,1).rvs((5,2)) # Random variables with 5 rows and 2 columns in normal distribution - mean = 1; sd = 1
np.concatenate((ss.norm(0,1).rvs((5,2)), ss.norm(0,1).rvs((5,2))), axis=0) # Concatenate the two arrays to make 1 array
                                                                           # of 10 rows & 2 columns - concatenate along
                                                                           # the rows (i.e. axis of 0)
# For function, use:
np.concatenate((ss.norm(0,1).rvs((n,2)), ss.norm(0,1).rvs((n,2))), axis=0) # n observations for both classes

# Function:
def generate_synth_data(n=50): # If user doesn't call argument, n = 50 by default
    """Create two sets of points from bivariate normal distributions."""
    points = np.concatenate((ss.norm(0,1).rvs((n,2)), ss.norm(0,1).rvs((n,2))), axis=0) # Generate 'points' vector
    outcomes = np.concatenate((np.repeat(0, n), np.repeat(1, n))) # Generate 'outcomes' vector
    return (points, outcomes) # Return a tuple consisting of points and outcomes

n = 20
(points, outcomes) = generate_synth_data(n)

plt.style.use('bmh')
plt.figure()
plt.plot(points[:n, 0], points[:n, 1], "o") # Class 1
plt.plot(points[n:, 0], points[n:, 1], "o") # Class 2
plt.savefig("bivar_data.png")

########################################
# 3.3.5 GENERATING SYNTHETIC DATA - Quiz
########################################
# Question 1: What does np.concatenate do?
# Solution 1: Takes in a tuple of np.arrays and joins them lengthwise along the specified axis

# Question 2: What is the main benefit of generating synthetic data?
# Solution 2: You know exactly how the data were generated so you know what to expect when testing code.

################################
# 3.3.6 MAKING A PREDICTION GRID
################################
# Plot Prediction Grid:
# Examine some part of the predictor space & compute class predictions for each point in the grid using knn classifier
# How does it classify all points that belong to a rectangular region of the predictor space

def make_prediction_grid(predictors, outcomes, limits, h, k): # Limits = x_min, x_max, y_min, y_max)
    """Classify each point on the prediction grid."""
    # Create meshgrid:
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys) # Generate 2 2-D arrays
    # Generate classifiers prediction corresponding to every point in the meshgrid:
    prediction_grid = np.zeros(xx.shape, dtype = int) # same shape as xx/yy; data type = int because their 0's & 1's
    for i,x in enumerate(xs): # Loop over xxs
        for j, y in enumerate(ys): # Loop over ys
            p = np.array([x,y]) # Generate point 'p' consisting of current x & y values
            prediction_grid[j,i] = knn_predict(p, predictors, outcomes, k) # Store predictions in prediction grid
                          # ^ ^ j = y, i = x - we assign y to rows and x to columns
    return (xx, yy, prediction_grid)

# Meshgrid = takes 2+ coordinate vectors & returns 2 matrices - 1st contains x values, 2nd y values for each grid point

# Enumerate = when dealing with sequences & we want 2 things simultaneously - elements in sequence & their index values
seasons = ["spring", "summer", "fall", "winter"]
list(enumerate(seasons)) # Sequence of tuples - inside, 1st object = Index & 2nd object= Element

for ind, season, in enumerate(seasons):
    print(ind, season) # Returns "0 spring
                                # 1 summer
                                # 2 fall
                                # 3 winter"

#######################################
# 3.3.6 MAKING A PREDICTION GRID - Quiz
#######################################
# Question 1: What does np.arrange do?
# Solution 1: Creates regularly spaced values between the 1st and 2nd argument, with spacing given in the 3rd argument

# Question 2: What does enumerate do?
# Solution 2: Takes an iterable and returns a new iterable with tuples as elements, where the first index of each
            # tuple is the index of the tuple in the iterable

####################################
# 3.3.7 PLOTTING THE PREDICTION GRID
####################################
# Create Plot Prediction Grid Function:
def plot_prediction_grid (xx, yy, prediction_grid, filename):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    plt.savefig(filename)

(predictors, outcomes) =  generate_synth_data() # Generate synthetic data
predictors.shape # Returns "(100, 2)"
outcomes.shape # Returns "(100,)"

k = 5; filename= "knn_synth_5.png"; limits = (-3,4,-3,4); h = 0.1
(xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k)
plot_prediction_grid(xx, yy, prediction_grid, filename)

# Bias-Variance Trade-Off = It is suboptimal to use k values that are too large or too small

###############################
# 3.3.8 APPLYING THE KNN METHOD
###############################
# SciKitLearn = open source machine learning library for Python
# We'll use the knn classifier

# Dataset = Iris
        # 150 different iris flowers - 50 from each of 3 different species
        # Each flower = sepal length, sepal width, petal length, petal width

from sklearn import datasets
iris = datasets.load_iris()

iris["data"] # 150 rows = 150 observations; # 4 columns = 4 covariates

predictors = iris.data[:, 0:2] # We want all of the rows but only the first 2 covariates
outcomes = iris.target # Want we want to be able to predict
iris

plt.style.use('bmh')
plt.plot(predictors[outcomes==0][:,0], predictors[outcomes==0][:,1], "o") # Blue Dots
plt.plot(predictors[outcomes==1][:,0], predictors[outcomes==1][:,1], "o") # Red Dots
plt.plot(predictors[outcomes==2][:,0], predictors[outcomes==2][:,1], "o") # Purple Dots
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title('Iris Dataset')
plt.legend(iris.target_names, loc='lower right')
plt.savefig("iris.png")

k = 5; filename= "iris_grid.png"; limits = (4,8,1.5,4.5); h = 0.1
(xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k)
plot_prediction_grid(xx, yy, prediction_grid, filename)

# Scikit Predictions:
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(predictors, outcomes)
sk_predictions = knn.predict(predictors)
sk_predictions.shape # Returns "(150,)"

# My Predictions:
my_predictions = np.array([knn_predict(p, predictors, outcomes, 5) for p in predictors])
my_predictions.shape # Returns "(150,)"

# Compare Predictions:
100*np.mean(sk_predictions == my_predictions) # Returns "96.0" - 96%!!
100*np.mean(sk_predictions == outcomes) # Returns "83.3" - 83%
100*np.mean(my_predictions == outcomes) # Returns "84.6" - 85% - WHOOP WHOOP!!

######################################
# 3.3.8 APPLYING THE KNN METHOD - Quiz
######################################
# Question 1: What are the four variables in the iris dataset described in Video 3.3.8?
# Solution 1: Sepal length, sepal width, petal length, petal width

# Question 2: How many different species are contained in the iris dataset described in Video 3.3.8?
# Solution 2: 3

# Question 3: How often do the predictions from the homemade and scikit-learn kNN classifiers accurately predict the
            # class of the data in the iris dataset described in Video 3.3.8?
# Solution 3: Approximately 85% of the time