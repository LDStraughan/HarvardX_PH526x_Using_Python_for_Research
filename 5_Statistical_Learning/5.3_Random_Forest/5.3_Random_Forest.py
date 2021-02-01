##########################################################
# 5.3.1 TREE-BASED METHODS FOR REGRESSION & CLASSIFICATION
##########################################################
# Tree-based methods = Tree graph decision-making method - split up predictor space into simpler regions
# Random Forest = takes predictions of several trees
# We don't want identical trees - they'll just make the same prediction (hence randomisation)

# Recursive in nature - Make prediction for a previously unseen test observation by finding region of the predictor
# space where the test observation falls
# Regression - Return the MEAN of the outcomes of the training observations in that region
# Classification - Return the MODE (most common element) of the outcomes of the training in that region

# How do we know where to make the splits?
# Carve out regions in the predictor space that are maximally homogeneous in terms of their outcomes
# We consider all predictors and for each predictor, we consider all cut points
# Choose predictor-cut point combination to ensure that the decision of the predictor space has the lowest value of some
# criterion, usually called a loss function, that we're trying to minimise - i.e. maximise accuracy
# Regression - loss function = RSS (residual sum of squares)
# Classification - loss functions = Gini index & cross-entropy
# Want to make each split point so that each class within a region is as homogeneous as possible

#################################################################
# 5.3.1 TREE-BASED METHODS FOR REGRESSION & CLASSIFICATION - Quiz
#################################################################
# Question 1: The goal of a tree-based method is typically to split up the predictor or feature space such that:
# Solution 1: data within each region are as similar as possible.

# Question 2.a: For classification, how does a decision tree make a prediction for a new data point?
# Solution 2.a: It returns the mode of the outcomes of the training data points in the predictor space where the new
#               data point falls.
# Question 2.b: For regression, how does a decision tree make a prediction for a new data point?
# Solution 2.b: It returns the mean of the outcomes of the training data points in the predictor space where the new
#               data point falls.

#################################
# 5.3.2 RANDOM FOREST PREDICTIONS
#################################
# Random Forest introduce 2 types of randomness to decision trees:
#       1) Introduce randomness to DATA - each fit is to a somewhat different dataset
#               - Bagging = Bootstap Aggregation - re-sampling method involving repeatedly drawing samples from training
#                           set & refitting a model on each sample
#       2) Which PREDICTORS are used when considering making a SPLIT point
#               -  Draw a small random sample of predictors and then make a split

from sklearn.ensemble import RandomForestRegressor # Random forest regression
from sklearn.ensemble import RandomForestClassifier # Random forest classifier
# After importing the relevant model, everything proceeds in the same way as for linear and logistic regression as shown
# in the previous videos.

########################################
# 5.3.2 RANDOM FOREST PREDICTIONS - Quiz
########################################
# Question 1.a: Random forests get their name by introducing randomness to decision trees in two ways, once at the data
#               level and once at the predictor level. How is randomness at the data level introduced?
# Solution 1.a: Each tree gets a bootstrapped random sample of training data.
# Question 1.b: How is randomness at the predictor level introduced?
# Solution 1.b: Each split only uses a subset of predictors.

# Question 2.a: In a classification setting, how does a random forest make predictions?
# Solution 2.a: Each tree makes a prediction and the mode of these predictions is the prediction of the forest.
# Question 2.b: In a regression setting, how does a random forest make predictions?
# Solution 2.b: Each tree makes a prediction and the mean of these predictions is the prediction of the forest.