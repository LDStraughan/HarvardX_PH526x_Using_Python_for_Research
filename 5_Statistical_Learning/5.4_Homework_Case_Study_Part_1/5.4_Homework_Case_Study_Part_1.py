#####################
# CASE STUDY 7 PART 1
#####################
# The movie dataset on which this case study is based is a database of 5000 movies catalogued by The Movie Database
# (TMDb). The information available about each movie is its budget, revenue, rating, actors and actresses, etc. In this
# case study, we will use this dataset to determine whether any information about a movie can predict the total revenue
# of a movie. We will also attempt to predict whether a movie's revenue will exceed its budget.
# In Part 1 of this case study, we will inspect, clean, and transform the data.

###############
# EXERCISES 1-4
###############
#   Exercise 1: First, we will import several libraries. scikit-learn (sklearn) contains helpful statistical models,
#               and we'll use the matplotlib.pyplot library for visualizations. Of course, we will use numpy and pandas
#               for data manipulation throughout.
#       Instructions:
#       Read and execute the given code, then call df.head() to take a look at the data.
#       Here's the import code:
#           import pandas as pd
#           import numpy as np
#           from sklearn.model_selection import cross_val_predict
#           from sklearn.linear_model import LinearRegression
#           from sklearn.linear_model import LogisticRegression
#           from sklearn.ensemble import RandomForestRegressor
#           from sklearn.ensemble import RandomForestClassifier
#           from sklearn.metrics import accuracy_score
#           from sklearn.metrics import r2_score
#           import matplotlib.pyplot as plt
#           df = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@movie_data.csv", index_col=0)
#           # Enter code here.
#       What is the title of the first movie in this dataset?
#   Solution 1:
        import pandas as pd
        import numpy as np
        from sklearn.model_selection import cross_val_predict
        from sklearn.linear_model import LinearRegression
        from sklearn.linear_model import LogisticRegression
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import accuracy_score
        from sklearn.metrics import r2_score
        import matplotlib.pyplot as plt
        df = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@movie_data.csv", index_col=0)
        pd.set_option('display.max_columns', None)
        df.head() # Answer = Avatar

#   Exercise 2: In Exercise 2, we will define the regression and classification outcomes. Specifically, we will use the
#               revenue column as the target for regression. For classification, we will construct an indicator of
#               profitability for each movie.
#       Instructions:
#       - Create a new column in df called profitable, defined as 1 if the movie revenue (revenue) is greater than the
#       movie budget (budget), and 0 otherwise.
#       - Next, define and store the outcomes we will use for regression and classification. Define regression_target as
#       the string 'revenue'. Define classification_target as the string 'profitable'.
#       How many movies in this dataset are defined as profitable (value 1)?
#   Solution 2:
