##############################################
# 5.2.1 GENERATING EXAMPLE CLASSIFICATION DATA
##############################################
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

h = 1
sd = 1
n = 50
def gen_data(n, h, sd1, sd2):
    x1 = ss.norm.rvs(-h, sd1, n)
    y1 = ss.norm.rvs(0, sd1, n)
    x2 = ss.norm.rvs(h, sd2, n)
    y2 = ss.norm.rvs(0, sd2, n)
    return(x1, y1, x2, y2)
(x1, y1, x2, y2) = gen_data(1000, 1.5, 1, 1.5)

plt.style.use("bmh")
def plot_data(x1, y1, x2, y2):
    plt.figure()
    plt.plot(x1, y1, "o", ms=2)
    plt.plot(x2, y2, "o", ms=2)
    plt.xlabel("$X_1$")
    plt.ylabel("$X_2$")
plot_data(x1, y1, x2, y2)

#####################################################
# 5.2.1 GENERATING EXAMPLE CLASSIFICATION DATA - Quiz
#####################################################
# Question 1.a: Which of the following function calls will produce data that would be easiest to classify correctly?
# Solution 1.a: gen_data(1000, 20, .5, .5)
# Question 1.b: Which of the following function calls will produce data that would be hardest to classify correctly?
# Solution 1.b: gen_data(1000, 0, 1, 1)

###########################
# 5.2.2 LOGISTIC REGRESSION
###########################
# Logistic Regression = Binary Classifier
# Logistic Regression = Linear model that models probabilities on a non-linear scale

# Maximum Likelihood Method = Find parameter Estimates that make the observed data maximally likely

##################################
# 5.2.2 LOGISTIC REGRESSION - Quiz
##################################
# Question 1: What is one of the problems with using linear regression to predict probabilities?
# Solution 1: Linear regression may predict values outside of the interval between 0 and 1.

# Question 2: The following code creates a function that converts probability to odds:
#                 def prob_to_odds(p):
#                     if p <= 0 or p >= 1:
#                         print("Probabilities must be between 0 and 1.")
#                     return p / (1-p)
#             Assume that there are only two classes and all data points belong to one of these two classes. The
#             probability that a given data point belongs to Class 1 is 0.2.
#             What are the odds that a given data point belongs to Class 2 as given by the function above?
# Solution 2:
        def prob_to_odds(p):
            if p <= 0 or p >= 1:
                print("Probabilities must be between 0 and 1.")
            return p / (1-p)
        prob_to_odds(0.8) # Answer = 4

###################################
# 5.2.3 LOGISTIC REGRESSION IN CODE
###################################
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression() # Classifier
# Create X
X = np.vstack((np.vstack((x1, y1)).T, np.vstack((x2, y2)).T)) # hstack = stack horizontally, vstack = stack vertically
X.shape # Returns "(2000, 2)"
# Create y
n = 1000
y = np.hstack((np.repeat(1,n), np.repeat(2, n)))
y.shape
# Generate Test & Train sets
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5, random_state=1)
# Fit the classifier
clf.fit(X_train, y_train)
clf.score(X_test, y_test) # How well does the classifier perform? - Returns "0.894"
clf.predict_proba(np.array([-2,0]).reshape((1, -1))) # Estimated class probabilities - Returns "array([[0.97429063, 0.02570937]])"
clf.predict(np.array([-2,0]).reshape((1, -1))) # Predicts that it belongs to class 1 - Returns "array([1])"

##########################################
# 5.2.3 LOGISTIC REGRESSION IN CODE - Quiz
##########################################
# Question 1.a: If you have data and want to train a model, which method would you use?
# Solution 1.a: clf.fit()
# Question 1.b: If you want to compute the accuracy of your model, which method would you use?
# Solution 1.b: clf.score()
# Question 1.c: If you want to estimate the probability of a data point being in each class, which method would you use?
# Solution 1.c: clf.predict_proba()
# Question 1.d: If you want to know to which class your model would assign a new data point, which method would you use?
# Solution 1.d: clf.predict()

##########################################################
# 5.2.4 COMPUTING PREDICTIVE PROBABILITIES ACROSS THE GRID
##########################################################
# Create function:
def plot_probs(ax, clf, class_no): # Arguments = axis, classifier, class number
    xx1, xx2 = np.meshgrid(np.arange(-5, 5, 0.1), np.arange(-5, 5, 0.1)) # Use meshgrid & specify range of values
    probs = clf.predict_proba(np.stack((xx1.ravel(), xx2.ravel()), axis=1)) # Use ravel - turn into vectors & stack
    Z = probs[:,class_no] # Extract all rows but only columns that correspond to class_no argument in function
    Z = Z.reshape(xx1.shape) # Turn Z into the shape of xx1 (or xx2 - doesn't matter in this case)
    CS = ax.contourf(xx1, xx2, Z) # Plot Z at locations specified by xx1 and xx2
    cbar = plt.colorbar(CS) # Add colour bar
    plt.xlabel("$X_1$") # Add axes labels
    plt.ylabel("$X_2$") # Add axes labels

# Call function:
plt.figure(figsize=(5,8)) # Create figure of a particular size
ax = plt.subplot(211) # Create subplot
plot_probs(ax, clf, 0) # Call function - Args = axis object, classifier, class number 0
plt.title("Pred. prob for class 1") # Add title for subplot 1
ax = plt.subplot(212) # Create subplot
plot_probs(ax, clf, 1) # Call function - Args = axis object, classifier, class number 1
plt.title("Pred. prob for class 2"); # Add title for subplot 2
# As conditional probability in upper plot decreases to the right, conditional probability in bottom plot increases

#################################################################
# 5.2.4 COMPUTING PREDICTIVE PROBABILITIES ACROSS THE GRID - Quiz
#################################################################
# Question 1: What does the pattern of probabilities across the grid indicate about  X1  and  X2 ?
# Solution 1: The class probability is determined mostly by X_1.

# Question 2: The sum of the class probabilities:
# Solution 2: will always equal 1 for any number of classes.