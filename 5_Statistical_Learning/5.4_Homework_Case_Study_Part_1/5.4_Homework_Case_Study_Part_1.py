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
        df.title.head()[0] # Answer = Avatar

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
        df['profitable'] = np.where(df['revenue'] > df['budget'], 1, 0)
        regression_target = 'revenue'
        classification_target = 'profitable'
        df['profitable'].value_counts() # Answer = 2585

#   Exercise 3: For simplicity, we will proceed by analyzing only the rows without any missing data. In Exercise 3, we
#               will remove rows with any infinite or missing values.
#       Instructions:
#       - Use df.replace() to replace any cells with type np.inf or -np.inf with np.nan.
#       - Drop all rows with any np.nan values in that row using df.dropna(). Do any further arguments need to be
#       specified in this function to remove rows with any such values?
#       How many movies are left in the dataset after dropping any rows with infinite or missing values?
#   Solution 3:
        df = df.replace([np.inf, -np.inf], np.nan)
        df = df.dropna(how="any")
        df.shape # Answer = 1406

#   Exercise 4: Many of the variables in our dataframe contain the names of genre, actors/actresses, and keywords. Let's
#               add indicator columns for each genre.
#       Instructions:
#       - Determine all the genres in the genre column. Make sure to use the strip() function on each genre to remove
#       trailing characters.
#       - Next, include each listed genre as a new column in the dataframe. Each element of these genre columns should
#       be 1 if the movie belongs to that particular genre, and 0 otherwise. Keep in mind that a movie may belong to
#       several genres at once.
#       - Call df[genres].head() to view your results.
#       How many genres of movies are in this dataset?
#   Solution 4:
        list_genres = df.genres.apply(lambda x: x.split(","))
        genres = []
        for row in list_genres:
                row = [genre.strip() for genre in row]
                for genre in row:
                        if genre not in genres:
                                genres.append(genre)
        for genre in genres:
                df[genre] = df['genres'].str.contains(genre).astype(int)
        df[genres].head()
        len(genres) # Answer = 20

###############
# EXERCISES 5-7
###############
#   Exercise 5: Some variables in the dataset are already numeric and perhaps useful for regression and classification.
#               In Exercise 5, we will store the names of these variables for future use. We will also take a look at
#               some of the continuous variables and outcomes by plotting each pair in a scatter plot. Finally, we will
#               evaluate the skew of each variable.
#       Instructions:
#       - Call plt.show() to observe the plot generated by the code given below. Which of the covariates and/or outcomes
#       are correlated with each other?
#       - Call skew() on the columns outcomes_and_continuous_covariates in df. Is the skew above 1 for any of these
#       variables?
#       Here is the code to get you started:
#       continuous_covariates = ['budget', 'popularity', 'runtime', 'vote_count', 'vote_average']
#       outcomes_and_continuous_covariates = continuous_covariates + [regression_target, classification_target]
#       plotting_variables = ['budget', 'popularity', regression_target]
#       axes = pd.plotting.scatter_matrix(df[plotting_variables], alpha=0.15, \
#               color=(0,0,0), hist_kwds={"color":(0,0,0)}, facecolor=(1,0,0))
#       # show the plot.
#       # determine the skew.
#       Which continuous covariate appears to be the most skewed?
#   Solution 5:
        continuous_covariates = ['budget', 'popularity', 'runtime', 'vote_count', 'vote_average']
        outcomes_and_continuous_covariates = continuous_covariates + [regression_target, classification_target]
        plotting_variables = ['budget', 'popularity', regression_target]
        axes = pd.plotting.scatter_matrix(df[plotting_variables], alpha=0.15, \
               color=(0,0,0), hist_kwds={"color":(0,0,0)}, facecolor=(1,0,0))
        plt.show()
        print(df[outcomes_and_continuous_covariates].skew()) # Answer = popularity

#   Exercise 6: It appears that the variables budget, popularity, runtime, vote_count, and revenue are all right-skewed.
#               In Exercise 6, we will transform these variables to eliminate this skewness. Specifically, we will use
#               the np.log10() method. Because some of these variable values are exactly 0, we will add a small positive
#               value to each to ensure it is defined; this is necessary because log(0) is negative infinity.
#       Instructions:
#       For each above-mentioned variable in df, transform value x into np.log10(1+x).
#       What is the new value of skew() for the covariate runtime? Please provide the answer to 3 decimal points.
#   Solution 6:
        for covariate in ['budget', 'popularity', 'runtime', 'vote_count', 'revenue']:
                df[covariate] = df[covariate].apply(lambda x: np.log10(1 + x))
        print(df[outcomes_and_continuous_covariates].skew()) # Answer = 0.530

#   Exercise 7: Now we're going to save our dataset to use in Part 2 of this case study.
#
#       Instructions:
#       Use to_csv() to save the df object as movies_clean.csv.
#       What is the correct way to save the df object?
#   Solution 7:
        df.to_csv("movies_clean.csv")