############################################
# 5.1.1 INTRODUCTION TO STATISTICAL LEARNING
############################################
# Statistical Learning = large collection of tools used for understanding data
# 2 Categories:
        # 1) Supervised Learning - when given set of example inputs & outputs, learn to associate inputs with outputs
        # 2) Unsupervised Learning - when given inputs only and no outputs

# Regression = Problems that have continuous outputs
# Classification = Problems that have categorical outputs (0 or 1; blue or green; etc.)

# We'll be working with Supervised Learning
# X = input variable; y = output variable - We seek some function (f of X) for predicting Y
# Best prediction depends on Loss Function - how far our predictions for Y are compared to actual Y values
# Squared Error Loss = Predict the average of all values of Y that correspond to value of X (most common in regression)
# 0-1 Loss = Compute probability of each class and assign X to highest probable class (most common in classification)

###################################################
# 5.1.1 INTRODUCTION TO STATISTICAL LEARNING - Quiz
###################################################
# Question 1: What is the difference between supervised and unsupervised learning?
# Solution 1: Supervised learning matches inputs and outputs, whereas unsupervised learning discovers structure for
#             inputs only.

# Question 2: What is the difference between regression and classification?
# Solution 2: Regression results in continuous outputs, whereas classification results in categorical outputs.

# Question 3: What is the difference between least squares loss and  0−1  loss?
# Solution 3: Least squares loss is used to estimate the expected value of outputs, whereas  0−1  loss is used to
#             estimate the probability of outputs.

##########################################
# 5.1.2 GENERATING EXAMPLE REGRESSION DATA
##########################################
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

# Generate fake data:
n = 100 # We want 100 data points
beta_0 = 5 # Parameter 1
beta_1 = 2 # Parameter 2
np.random.seed(1) # Set seed to control results
x = 10 * ss.uniform.rvs(size=n) # Generate random variables that are distributed from 0-10 interval - n = 100 variables
y = beta_0 + beta_1 * x + ss.norm.rvs(loc=0, scale=1, size=n) # betas = constant coefficient; x = variables; rvs = noise

# Plot our data:
plt.style.use("bmh")
plt.figure()
plt.plot(x, y, "o", ms=5)
xx = np.array([0, 10]) # Plot regression function
plt.plot(xx, beta_0 + beta_1 * xx) # Deterministic part of the model
plt.xlabel("x")
plt.ylabel("y")

#################################################
# 5.1.2 GENERATING EXAMPLE REGRESSION DATA - Quiz
#################################################
# Question 1: What is the approximate mean of x and y, respectively? (according to previous section)
# Solution 1:
x.mean(), y.mean() # Answer: Mean x = 4.9, mean y = 14.8

################################
# 5.1.3 SIMPLE LINEAR REGRESSION
################################
# Y = beta_0 + beta_1 * X + epsilon (Capitals = random; betas = parameters; X = random variable; epsilon = error term)
# y_hat = beta_0_hat + beta_1_hat * x (y_hat = predicted value; beta_hats = estimated from data)

# Residuals = Difference between the actual y value & estimated y value from the regression line
# i-th observation (Residuals):
# e_i = y_i - y_i_hat (e_i = difference between; y_i = observed response value; and y_i_hat = predicted response value)

# Residual Sum of Squares (RSS):
# RSS = e_1**2 + e_2**2 ... e_n**2

#######################################
# 5.1.3 SIMPLE LINEAR REGRESSION - Quiz
#######################################
# Question 1: What is the difference between Y (capital letter) and y (lowercase letter)?
# Solution 1: Y is a random variable, whereas y is a particular value.

# Question 2: The following code implements the residual sum of squares for this regression problem:
#               def compute_rss(y_estimate, y):
#                   return sum(np.power(y-y_estimate, 2))
#               def estimate_y(x, b_0, b_1):
#                   return b_0 + b_1 * x
#               rss = compute_rss(estimate_y(x, beta_0, beta_1), y)
#             Using the data from CC 5.1.2 , run the code above. What is the approximate value of rss?
# Solution 2:
        def compute_rss(y_estimate, y):
          return sum(np.power(y-y_estimate, 2))
        def estimate_y(x, b_0, b_1):
          return b_0 + b_1 * x
        rss = compute_rss(estimate_y(x, beta_0, beta_1), y)
        rss # Answer = 82

########################################
# 5.1.4 LEAST SQUARES ESTIMATION IN CODE
########################################
# Use matrix calculus to obtain a formula (closed-form solution) for obtaining the least-squares estimates
# Gradient Descent = numerical optimisation method used for complex models
rss = [] # list that will contain all the rss values for different values of the slopes
slopes = np.arange(-10, 15, 0.01) # We want to estimate the slope of the line (gradient descent)
for slope in slopes: # Loop over each value in the slope
    rss.append(np.sum((y - beta_0 - slope * x)**2)) # Calculate RSS & append to 'rss' list
ind_min = np.argmin(rss) # Find index in rss list that gives the lowest RSS value
ind_min # Returns "1200" - lowest RSS happens at index location 1200
print("Estimate for the Slope:", slopes[ind_min]) # Returns "Estimate for the Slope: 1.9999999999997442"
# Plot Figure:
plt.style.use("bmh")
plt.figure()
plt.plot(slopes, rss)
plt.xlabel("Slope")
plt.ylabel("RSS"); # Lowest point occurs at around 2.0

###############################################
# 5.1.4 LEAST SQUARES ESTIMATION IN CODE - Quiz
###############################################
# Question 1: Is the best estimate for the slope exactly the same as the true value 2 (when rounded to two decimal
#             places)? Rerun the code in the video, but use a finer grid for the search by specifying
#             slopes = np.arange(-10, 15, 0.001).
#             Which of the following characterizes the new estimate for the slope?
# Solution 1: Still exactly 2

########################################
# 5.1.5 SIMPLE LINEAR REGRESSION IN CODE
########################################
import statsmodels.api as sm
mod = sm.OLS(y, x) # OLS = Ordinary Least Squares
est = mod.fit()
print(est.summary()) # We didn't specify an intercept, so it starts at 0 and has a larger coefficient of 2.75

X = sm.add_constant(x) # X = same as lower-case x from before, but includes a column of 1s
mod = sm.OLS(y, X) # Define new 'mod' object with X instead of x
est = mod.fit()
print(est.summary()) # New x1 coefficient is much closer - 1.9685
# The smaller the std error, the more precisely we've estimated - In this case, 0.031
# confidence interval = Slop Estimate +/- 1.96 * standard error
1.9685 + 1.96 * 0.031, 1.9685 - 1.96 * 0.031 # Returns "(2.02926, 1.90774)" - also seen in summary output
# R-squared = Proportion of explained variance - larger the better (in this case r-squared = 0.977)

###############################################
# 5.1.5 SIMPLE LINEAR REGRESSION IN CODE - Quiz
###############################################
# Question 1: If the true intercept were negative but the regression model did not include an intercept term, what would
#             that imply for the estimated slope?
# Solution 1: The estimated slope would likely be lower than the true slope.

# Question 2: What does an estimated intercept term correspond to?
# Solution 2: The estimated outcome when the input is set to zero

# Question 3: What does an estimated slope term correspond to?
# Solution 3: The change in the estimated output when the input changes by one unit

# Question 4: You could create several datasets using different seed values and estimate the slope from each. These
#             parameters will follow some distribution.
#             What is the name used for this distribution?
# Solution 4: The sampling distribution of the parameter estimates

# Question 5: If the R**2 value is high, this indicates
# Solution 5: A good fit: the residual sum of squares is low compared to the total sum of squares.

##################################
# 5.1.6 MULTIPLE LINEAR REGRESSION
##################################
# Goal = Predict quantitative/scalar valued response, Y, on the basis of several predictor variables
# Y = beta_0 + beta_1*X_1 + beta_2*X_2 ... beta_p*X_p + epsilon (X & Y = random variables; epsilon = error term)


#########################################
# 5.1.6 MULTIPLE LINEAR REGRESSION - Quiz
#########################################
# Question 1: Consider a multiple regression model with two inputs. The model predictions for the output y are given by
#             y_hat = β_0_hat + x_1*β_1_hat + x_2*β_2_hat
#             β_1  and  β_2  have been estimated from data. If we assume that  β_1_hat=1 , and  β_2_hat=3 .
#             What is the interpretation of  β_1_hat ?
# Solution 1: The change in the predicted outcome if x_1 is increased by 1, holding x_2 constant.

# Question 2: Consider the model and parameters in Question 1. For a given expected output prediction y_hat, what would
#             be the expected change in the prediction value if you increased x_1 by 1, and decreased x_2 by 3?
# Solution 2: -8


##########################################
# 5.1.7 SCIKIT-LEARN FOR LINEAR REGRESSION
##########################################
n = 500 # Sample size
beta_0 = 5 # Predictor 1 - Constant
beta_1 = 2 # Predictor 2 - Covariate
beta_2 = -1 # Predictor 3 - Covariate
np.random.seed(1) # Make sure you control results
x_1 = 10 * ss.uniform.rvs(size=n) # Define x_1
x_2 = 10 * ss.uniform.rvs(size=n) # Define x_2
y = beta_0 + beta_1 * x_1 + beta_2 * x_2 + ss.norm.rvs(loc=0, scale=1, size=n) # Added noise: Mean=0; Variance & std=1
# Construct X variable - Stack x_1 & x_2 as columns, turning it into a matrix
X = np.stack([x_1, x_2], axis=1)

# Plot:
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0], X[:,1], y, c=y)
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_zlabel("$y$");

# Let's FIt this model:
from sklearn.linear_model import LinearRegression
lm = LinearRegression(fit_intercept=True) # lm = Linear Model
lm.fit(X, y)
lm.intercept_ # Returns "5.154077763777254"
lm.coef_ # Returns "array([ 1.9999379 , -1.02026449])" - beta_1 = lm.coef_[0]; beta_2 = lm.coef_[1]
# Try to Predict value of X
X_0 = np.array([2, 4])
lm.predict(X_0.reshape(1, -1)) # Returns "array([5.07289561])"
# Find the Score (r-squared):
lm.score(X, y) # Returns "0.9798997316600129"


#################################################
# 5.1.7 SCIKIT-LEARN FOR LINEAR REGRESSION - Quiz
#################################################
# Question 1: In the video, we estimated the values of three parameters. Which of these estimates is closest to its true
#             value?
# Solution 1: The estimated first slope,  β_1

################################
# 5.1.8 ASSESSING MODEL ACCURACY
################################
# Mean Squared Error (MSE) = Most common measure in regression setting to evaluate performance of a model
# We want to see MSE on TEST data, not really TRAINING data
# Training Error Rate = Proportion of errors the classifier makes when applied to training data
# Test Error Rate = Proportion of errors/misclassifications the classifier makes when applies to test data
# We divide out dataset into 2 parts - Train on TRAINING set & Test on TEST set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5, random_state=1)
lm = LinearRegression(fit_intercept=True)
lm.fit(X_train, y_train)
lm.score(X_test, y_test) # Returns "0.9794930834681773"

# Overfitiing = Models that are too flexible - model starts to follow the noise in data too closely (doesn't generalise)
# Underfitting = Models that are too simple - model isn't flexible enough to learn the structure in the data

#######################################
# 5.1.8 ASSESSING MODEL ACCURACY - Quiz
#######################################
# Question 1.a: When evaluating the performance of a model in a regression setting on test data, which measure is most
#               appropriate?
# Solution 1.a: Test MSE
# Question 1.b: When evaluating the performance of a model in a classification setting on test data, which measure is
#               most appropriate?
# Solution 1.b: Test Error Rate

# Question 2: How do we expect an model that was overfit on the training data to perform on testing data?
# Solution 2: It will likely perform worse on the testing data.

# Question 3: What is the primary motivation for splitting our model into training and testing data?
# Solution 3: By evaluating how our model fits on unseen data, we can see how generalizable it is.