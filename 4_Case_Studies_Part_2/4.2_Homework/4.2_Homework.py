##############
# CASE STUDY 5
##############
# In this case study, we will continue taking a look at patterns of flight for each of the three birds in our dataset.
# We will group the flight patterns by bird and date, and plot the mean altitude for these groupings.
# In order to do the homework, you should start by reading in the data using the following code:
import pandas as pd
import numpy as np
birddata = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@bird_tracking.csv",
                       index_col=0)
birddata.head()

###############
# EXERCISES 1-4
###############
#   Exercise 1: In Exercise 1, we will group the dataframe by birdname and then find the average speed_2d for each bird.
#               pandas makes it easy to perform basic operations on groups within a dataframe without needing to loop
#               through each value in the dataframe.
#       Instructions:
#       Fill in the code to find the mean altitudes of each bird using the pre-loaded birddata dataframe.
#       Here is the code:
#           # First, use `groupby()` to group the data by "bird_name".
#           grouped_birds =
#           # Now calculate the mean of `speed_2d` using the `mean()` function.
#           mean_speeds =
#           # Find the mean `altitude` for each bird.
#           mean_altitudes =
#       What is the mean speed for Sanne?
#   Solution 1:
        # First, use `groupby()` to group the data by "bird_name".
        grouped_birds = birddata.groupby("bird_name")
        grouped_birds.first()
        # Now calculate the mean of `speed_2d` using the `mean()` function.
        mean_speeds = grouped_birds.speed_2d.mean()
        mean_speeds
        # Find the mean `altitude` for each bird.
        mean_altitudes = grouped_birds.altitude.mean()
        mean_altitudes
        # Answer = 2.450434

#   Exercise 2: In Exercise 2, we will group the flight times by date and calculate the mean altitude within that day.
#       Instructions:
#       Convert birddata.date_time to the pd.datetime format, and store as birddata["date"].
#       Fill in the code below to find the mean altitudes for each day:
#           # Convert birddata.date_time to the `pd.datetime` format.
#           birddata.date_time =
#           # Create a new column of day of observation
#           birddata["date"] =
#           # Use `groupby()` to group the data by date.
#           grouped_bydates =
#           # Find the mean `altitude` for each date.
#           mean_altitudes_perday =
#       What is the mean altitude of the birds on 2013-09-12?
#   Solution 2:
        # Convert birddata.date_time to the `pd.datetime` format.
        birddata.date_time = pd.to_datetime(birddata.date_time)
        # Create a new column of day of observation
        birddata["date"] = birddata.date_time.dt.date
        # Use `groupby()` to group the data by date.
        grouped_bydates = birddata.groupby("date")
        # Find the mean `altitude` for each date.
        mean_altitudes_perday = grouped_bydates.altitude.mean()
        mean_altitudes_perday[28] # Answer = 75.64609053497942

#   Exercise 3: In Exercise 3, we will group the flight times by both bird and date, and calculate the mean altitude for
#               each.
#       Instructions:
#       Note that birddata already contains the date column. To find the average speed for each bird and day, create a
#       new grouped dataframe called grouped_birdday that groups the data by both bird_name and date.
#       Fill in the following code for this exercise:
#           # Use `groupby()` to group the data by bird and date.
#           grouped_birdday =
#           # Find the mean `altitude` for each bird and date.
#           mean_altitudes_perday =
#       What is the mean altitude of the bird Eric on 2013-08-18?
#   Solution 3:
        # Use `groupby()` to group the data by bird and date.
        grouped_birdday = birddata.groupby(["bird_name", "date"])
        # Find the mean `altitude` for each bird and date.
        mean_altitudes_perday = grouped_birdday.altitude.mean()
        mean_altitudes_perday # Answer = 121.353659

#   Exercise 4: In Exercise 4, we will find the average speed for each bird and day.
#       Instructions:
#       Store the average speeds for each bird and day as three pandas Series objects, one for each bird, then use the
#       plotting code provided to plot the average speeds for each bird.
#       Here is the code to moldify for this exercise:
#           import matplotlib.pyplot as plt
#           eric_daily_speed  = # Enter your code here.
#           sanne_daily_speed = # Enter your code here.
#           nico_daily_speed  = # Enter your code here.
#           eric_daily_speed.plot(label="Eric")
#           sanne_daily_speed.plot(label="Sanne")
#           nico_daily_speed.plot(label="Nico")
#           plt.legend(loc="upper left")
#           plt.show()
#       What is the mean speed of the bird Nico on 2014-04-04?
#   Solution 4:
        import matplotlib.pyplot as plt
        plt.style.use("bmh")
        plt.title("Birds' Daily Speeds")
        eric_daily_speed  = grouped_birdday.speed_2d.mean()["Eric"]
        sanne_daily_speed = grouped_birdday.speed_2d.mean()["Sanne"]
        nico_daily_speed  = grouped_birdday.speed_2d.mean()["Nico"]
        eric_daily_speed.plot(label="Eric")
        sanne_daily_speed.plot(label="Sanne")
        nico_daily_speed.plot(label="Nico")
        plt.legend(loc="upper left")
        plt.show()
        plt.savefig("bird_daily_speeds.png")

        key = pd.to_datetime('2014-04-04').date()
        nico_daily_speed[key] # Answer = 2.8324654508684057