##############
# CASE STUDY 3
##############
#In the nine exercises in this case study, we will analyze a dataset consisting of an assortment of wines classified as
# "high quality" and "low quality" and will use  k -Nearest Neighbors classification to determine whether or not other
# information about the wine helps us correctly guess whether a new wine will be of high quality.
# You will need this sample code for the case study:
import numpy as np, random, scipy.stats as ss

def majority_vote_fast(votes):
    mode, count = ss.mstats.mode(votes)
    return mode

def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

def find_nearest_neighbors(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]

def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote_fast(outcomes[ind])[0]

###############
# EXERCISES 1-5
###############
#   Exercise 1:
#       Our first step is to import the dataset.
#       Instructions:
#       Read in the data as a pandas dataframe using pd.read_csv.
#       This code will get you started:
#           import pandas as pd
#           # write your code here!
#       Taking a look at the first 5 rows of the dataset, how many wines in those 5 rows are considered high quality?
#   Solution 1:
        import pandas as pd
        data = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@wine.csv",
                   index_col=0)
        data.head() # Answer = 1

#   Exercise 2:
#       Next, we will inspect the dataset and perform some mild data cleaning.
#       Instructions:
#       In order to get all numeric data, we will change the color column to an is_red column.
#           - If color == 'red', we will encode a 1 for is_red.
#           - If color == 'white', we will encode a 0 for is_red.
#       Create this new column, is_red. Drop the color column as well as quality and high_quality. We will predict the
#       quality of wine using the numeric data in a later exercise
#       Store this all numeric data in a pandas dataframe called numeric_data.
#       How many red wines are in the dataset?
#   Solution 2:
        data[data.color == "red"].count() # Answer = 1599
        # Make desired changes:
        data["is_red"] = (data["color"] == "red").astype(int)
        numeric_data = data.drop("color", axis=1)
        numeric_data.groupby('is_red').count()

#   Exercise 3:
#       We want to ensure that each variable contributes equally to the kNN classifier, so we will need to scale the
#       data by subtracting the mean of each variable (column) and dividing each variable (column) by its standard
#       deviation. Then, we will use principal components to take a linear snapshot of the data from several different
#       angles, with each snapshot ordered by how well it aligns with variation in the data. In this exercise, we will
#       scale the numeric data and extract the first two principal components.
#       Instructions:
#       Scale the data using the sklearn.preprocessing function scale() on numeric_data.
#       Convert this to a pandas dataframe, and store it as numeric_data.
#       Include the numeric variable names using the parameter columns = numeric_data.columns.
#       Use the sklearn.decomposition module PCA() and store it as pca.
#       Use the fit_transform() function to extract the first two principal components from the data, and store them as
#       principal_components.
#       Note: You may get a DataConversionWarning, but you can safely ignore it.
#       Fill in this code as you work:
#           import sklearn.preprocessing
#           scaled_data =
#           numeric_data =
#           import sklearn.decomposition
#           pca =
#           principal_components =
#       What is the shape of the new dataset?
#   Solution 3:
        import sklearn.preprocessing # Import preprocessing function
        scaled_data = sklearn.preprocessing.scale(numeric_data) # Scale the data
        numeric_data = pd.DataFrame(scaled_data, columns = numeric_data.columns) # Convert to DataFrame
        import sklearn.decomposition # Import decomposition module
        pca = sklearn.decomposition.PCA(n_components=2) # PCA = Principle Component Analysis
        principal_components = pca.fit_transform(numeric_data) # Extract the principle components
        principal_components.shape # Returns "(6497, 2)"

#   Exercise 4:
#       In Exercise 4, we will plot the first two principal components of the covariates in the dataset. The high and
#       low quality wines will be colored using red and blue, respectively.
#       Instructions:
#       The first two principal components can be accessed using principal_components[:,0] and
#       principal_components[:,1]. Store these as x and y respectively, and make a scatter plot of these first two
#       principal components.
#       Consider how well the two groups of wines are separated by the first two principal components.
#       Fill in your code where indicated to make the plot:
#           import matplotlib.pyplot as plt
#           from matplotlib.colors import ListedColormap
#           from matplotlib.backends.backend_pdf import PdfPages
#           observation_colormap = ListedColormap(['red', 'blue'])
#           x = # Enter your code here!
#           y = # Enter your code here!
#           plt.title("Principal Components of Wine")
#           plt.scatter(x, y, alpha = 0.2,
#               c = data['high_quality'], cmap = observation_colormap, edgecolors = 'none')
#           plt.xlim(-8, 8); plt.ylim(-8, 8)
#           plt.xlabel("Principal Component 1")
#           plt.ylabel("Principal Component 2")
#           plt.show()
#       Could you easily draw a linear boundary between the high and low quality wines using the first two principal
#       components?
#   Solution 4:
        import matplotlib.pyplot as plt
        from matplotlib.colors import ListedColormap
        from matplotlib.backends.backend_pdf import PdfPages
        observation_colormap = ListedColormap(['red', 'blue'])
        x = principal_components[:,0]
        y = principal_components[:,1]
        plt.title("Principal Components of Wine")
        plt.scatter(x, y, alpha = 0.2,
            c = data['high_quality'], cmap = observation_colormap, edgecolors = 'none')
        plt.xlim(-8, 8); plt.ylim(-8, 8)
        plt.xlabel("Principal Component 1")
        plt.ylabel("Principal Component 2")
        plt.show()
        plt.savefig("principal_comp_wine.png")
        # Answer = No

#   Exercise 5:
#       In Exercise 5, we will create a function that calculates the accuracy between predictions and outcomes.
#       Instructions:
#       Create a function accuracy(predictions, outcomes) that takes two lists of the same size as arguments and returns
#       a single number, which is the percentage of elements that are equal for the two lists.
#       Use accuracy to compare the percentage of similar elements in the x and y numpy arrays defined below.
#       Print your answer.
#       Here's the sample code to get you started:
#           import numpy as np
#           np.random.seed(1) # do not change this!
#           x = np.random.randint(0, 2, 1000)
#           y = np.random.randint(0 ,2, 1000)
#           def accuracy(predictions, outcomes):
#               # write your code here!
#       What is the accuracy of the x predictions on the "true" outcomes y?
#   Solution 5:
        import numpy as np
        np.random.seed(1) # do not change this!
        x = np.random.randint(0, 2, 1000)
        y = np.random.randint(0 ,2, 1000)
        def accuracy(predictions, outcomes):
            return 100*np.mean(predictions == outcomes)
        accuracy(x,y) # Returns "51.5"

#   Exercise 6:
#       The dataset remains stored as data. Because most wines in the dataset are classified as low quality, one very
#       simple classification rule is to predict that all wines are of low quality. In this exercise, we determine the
#       accuracy of this simple rule.
#       Instructions:
#       Use accuracy() to calculate how many wines in the dataset are of low quality. Do this by using 0 as the first
#       argument, and data["high_quality"] as the second argument.
#       Print your result.
#       What proportion of wines in the dataset are of low quality?
#   Solution 6:
        accuracy(0, data["high_quality"]) # Returns "36.69385870401724"

#   Exercise 7
#       In Exercise 7, we will use the kNN classifier from scikit-learn to predict the quality of wines in our dataset.
#
#       Instructions:
#       - Use knn.predict(numeric_data) to predict which wines are high and low quality and store the result as
#       library_predictions.
#       - Use accuracy to find the accuracy of your predictions, using library_predictions as the first argument and
#       data["high_quality"] as the second argument.
#       - Print your answer. Is this prediction better than the simple classifier in Exercise 6?
#       Here's the sample code to get you started:
#           from sklearn.neighbors import KNeighborsClassifier
#           knn = KNeighborsClassifier(n_neighbors = 5)
#           knn.fit(numeric_data, data['high_quality'])
#           # Enter your code here!
#       What is the accuracy of the KNN classifier? Please round your answer to the nearest integer.
#   Solution 7:
        from sklearn.neighbors import KNeighborsClassifier
        knn = KNeighborsClassifier(n_neighbors = 5)
        knn.fit(numeric_data, data['high_quality'])
        library_predictions = knn.predict(numeric_data)
        accuracy(library_predictions, data["high_quality"])

#   Exercise 8:
#       Unlike the scikit-learn function, our homemade kNN classifier does not take any shortcuts in calculating which
#       neighbors are closest to each observation, so it is likely too slow to carry out on the whole dataset. In this
#       exercise, we will select a subset of our data to use in our homemade kNN classifier.
#       Instructions:
#       Fix the random generator using random.seed(123), and select 10 rows from the dataset using
#       random.sample(range(n_rows), 10). Store this selection as selection.
#       Use this sample code to get started:
#           n_rows = data.shape[0]
#           # Enter your code here
#       What is the 10th random row selected?
#   Solution 8:
        n_rows = data.shape[0]
        random.seed(123)
        selection = random.sample(range(n_rows), 10)
        selection # Answer = 4392

#   Exercise 9:
#       We are now ready to use our homemade kNN classifier and compare the accuracy of our results to the baseline.
#       Instructions:
#       For each predictor p in predictors[selection], use knn_predict(p, predictors[training_indices,:],
#       outcomes[training_indices], k=5) to predict the quality of each wine in the prediction set, and store
#       these predictions as a np.array called my_predictions. Note that knn_predict is already defined as in the
#       Case 3 videos.
#       Using the accuracy function, compare these results to the selected rows from the high_quality variable in data
#       using my_predictions as the first argument and data.high_quality.iloc[selection] as the second argument.
#       Store these results as percentage.
#       Print your answer.
#   Solution 9:
        predictors = np.array(numeric_data)
        training_indices = [i for i in range(len(predictors)) if i not in selection]
        outcomes = np.array(data["high_quality"])

        my_predictions = np.array([knn_predict(p, predictors[training_indices,:], outcomes[training_indices], k=5) for p in predictors[selection]])
        percentage = accuracy(my_predictions, data["high_quality"])
        print(percentage) # Answer = 70%