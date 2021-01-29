#############################################
# 4.2.1 INTRODUCTION TO GPS TRACKING OF BIRDS
#############################################
# Data comes from LifeWatch INBO project
# Consists of migration data from 3 gulls: Eric; Nico; Sanne
# 8 columns and includes variables such as: latitude; longitude; altitude; time stamps, etc.
import pandas as pd
birddata = pd.read_csv("bird_tracking.csv")
birddata.head()
birddata.info()

##################################
# 4.2.2 SIMPLE DATA VISUALISATIONS
##################################
# Plot longitude & latitude
import matplotlib.pyplot as plt
import numpy as np

# Just for Eric:
ix = birddata.bird_name == "Eric"
x, y = birddata.longitude[ix], birddata.latitude[ix]
plt.figure(figsize=(7,7))
plt.plot(x,y, ".")

# For all 3 birds:
bird_names = pd.unique(birddata.bird_name)
plt.style.use("bmh")
plt.figure(figsize=(7, 7))
for bird_name in bird_names:
    ix = birddata.bird_name == bird_name
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    plt.plot(x, y, ".", label=bird_name)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.savefig("3bird_traj.png")

#########################################
# 4.2.2 SIMPLE DATA VISUALISATIONS - Quiz
#########################################
# Question 1: Which pandas function extracts all the unique values in a pd.Series?
# Solution 1: pd.unique

##############################
# 4.2.3 EXAMINING FLIGHT SPEED
##############################
ix = birddata.bird_name == "Eric"
speed = birddata.speed_2d[ix]
plt.hist(speed)
plt.hist(speed[:10])

np.isnan(speed).any() # Returns "True" - Some entries are not numbers
np.sum(np.isnan(speed)) # NumPy returns boolean array - when we SUM over it, it treats "True" as 1 - Returns "85"
ind = np.isnan(speed)
~ind # bitwise complement - Turns each element of "True" into "False" and vice versa

ix = birddata.bird_name == "Eric"
speed = birddata.speed_2d[ix]
ind = np.isnan(speed)
plt.hist(speed[~ind]) # Only print the ones that are "True"/numbers

plt.figure(figsize=(8,4))
speed = birddata.speed_2d[birddata.bird_name == "Eric"]
ind = np.isnan(speed)
plt.hist(speed[~ind], bins=np.linspace(0,30,20), normed=True)
plt.xlabel("2D speed (m/s)")
plt.ylabel("Frequency");
plt.savefig("eric_hist.png")

# How to make plot with Pandas:
birddata.speed_2d.plot(kind="hist", range=[0,30])
plt.xlabel("2D speed (m/s)")
plt.savefig("pd_eric_hist.png")

#####################################
# 4.2.3 EXAMINING FLIGHT SPEED - Quiz
#####################################
# Question 1: Which numpy method returns True for values that are not numericals?
# Solution 1: np.isnan

######################
# 4.2.4 USING DATETIME
######################
# Datetime = used for Timestamped Events
birddata.date_time[0:3] # Date = y-m-d

# If we want to operate on time & date stamps, we need to convert them into Daytime objects
import datetime
time_1 = datetime.datetime.today() # Takes the current date & time
time_2 = datetime.datetime.today()
time_2 - time_1 # Tell us how much time has passed

# Let's play around
date_str = birddata.date_time[0]
type(date_str) # Returns "str"
date_str[:-3] # We're unconcerned with the last 3 characters
datetime.datetime.strptime(date_str[:-3], "%Y-%m-%d %H:%M:%S") # 1st arg = String to format; 2nd arg = How to format 1st

# Create datetime object for every row:
timestamps = [] # Create empty list
for k in range(len(birddata)): # Loop over every row in birddata - use 'k' as loop variable
    timestamps.append(datetime.datetime.strptime\
    (birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S")) # Extract datetime except for last 3 char & append to list
    timestamps[:5]
# Construct Panda Series object & insert timestamp from list into it, then Append Series as new column in birddata
birddata["timestamp"] = pd.Series(timestamps, index = birddata.index)
birddata.head()
birddata.timestamp[4] - birddata.timestamp[3] # We can perform arithmetic

# Create a list that captures elapsed time since beginning of data collection
times = birddata.timestamp[birddata.bird_name == "Eric"] # Extract timestamps for Eric
elapsed_time = [time - times[0] for time in times] # time = loop variable - Loop over every time in times and subtract
                                                   # the 1st time measurement
elapsed_time[0] # Expect it to be 0
elapsed_time[1000] # Returns "Timedelta('12 days 02:02:00')"

# How to measue time in certain units like hours or days:
elapsed_time[1000] / datetime.timedelta(days=1) # Divide object by timedelta object - Returns "12.084722222222222" Days
elapsed_time[1000] / datetime.timedelta(hours=1) # Divide object by timedelta object - Returns "290.0333333333333" Hours

# Plot
plt.plot(np.array(elapsed_time) / datetime.timedelta(days=1))
plt.xlabel("Observation")
plt.ylabel("Elapsed Time (Days)");
plt.savefig("eric_timeplot.png")

#############################
# 4.2.4 USING DATETIME - Quiz
#############################
# Question 1: What does datetime.datetime.strptime do?
# Solution 1: Takes in a date and time string, as well as an expected format string, and returns a formatted datetime
            # object.

# Question 2: How can you find the difference in time between two datetime objects time_1 and time_2?
# Solution 2: time_2 - time_1

####################################
# 4.2.5 CALCULATING DAILY MEAN SPEED
####################################
# Create a plot - y-axis = mean daily speed; x-axis = time in days
# We need to collect all of the points that occur in a single day and create the mean velocity for that day

data = birddata[birddata.bird_name == "Eric"] # Extract Eric's data
times = data.timestamp # Create 'times' object using timestamp column
elapsed_time = [time - times[0] for time in times] # Loop over every time in times and subtract the 1st time measurement
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1) # Divide object by timedelta object

next_day = 1 # Initially equal to 1 - will be updated throughout
inds = [] # Empty list to keep track of indices to be sorted
daily_mean_speed = [] # Keep track of daily mean speeds
for (i,t) in enumerate(elapsed_days): # Use enumerate to get simple counter in a loop - returns a tuple (indices, time)
    if t < next_day: # if time has not hit the next day
        inds.append(i) # append the index to inds
    else:
        daily_mean_speed.append(np.mean(data.speed_2d[inds])) # Take the indices in 'inds' & compute mean & append
                                                              # result to daily mean speed
        next_day += 1 # Increase 'next_day' by 1
        inds = [] # reset inds
plt.style.use("bmh")
plt.figure(figsize=(8,6))
plt.title("Eric's Daily Mean Speed")
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean Speed (m/s)")
plt.savefig("eric_daily_mean_speed.png")

###########################################
# 4.2.5 CALCULATING DAILY MEAN SPEED - Quiz
###########################################
# Question 1: Read in the bird_tracking.csv data (provided along with Video 4.2.1) and take a look at Sanne's flight
            # times. Which is the earliest recorded timestamp in the dataset for Sanne?
# Solution 1:
birddata = pd.read_csv("bird_tracking.csv")
sanne = birddata[birddata.bird_name == "Sanne"]
sanne.date_time.head(1) # Returns "2013-08-15 00:01:08+00"

#################################
# 4.2.6 USING THE CARTOPY LIBRARY
#################################
# Cartopy = Makes it easy to draw maps
import cartopy.crs as ccrs
import cartopy.feature as cfeature

proj = ccrs.Mercator() # Specify a specific projection to use

plt.style.use("bmh") # Use bmh style - 'cause nice
plt.figure(figsize=(10,10)) # Set up new figure
plt.title("Catrographic Projection of Bird's Flight Trajectories") # Create header title
ax = plt.axes(projection=proj) # Create axes
ax.set_extent((-25.0, 20.0, 52.0, 10.0)) # Set extent of axes on map - usually found by trial and error
ax.add_feature(cfeature.LAND) # Superimpose land behind trajectories
ax.add_feature(cfeature.OCEAN) # Superimpose ocean behind trajectories
ax.add_feature(cfeature.COASTLINE) # Superimpose coastline behind trajectories
ax.add_feature(cfeature.BORDERS, linestyle =':') # Superimpose borders behind trajectories
for name in bird_names: # Loop over all bird names
    ix = birddata["bird_name"] == name # Extract the rows from data frame that correspond to particular bird
    x, y = birddata.longitude[ix], birddata.latitude[ix] # Create x & y for longitude & latitude (respectively)
    ax.plot(x, y, ".", transform=ccrs.Geodetic(), label=name) # Introduce the transformation
plt.legend(loc="upper left") # Place legend in the upper left corner
plt.savefig("3bird_traj_map.png")

########################################
# 4.2.6 USING THE CARTOPY LIBRARY - Quiz
########################################
# Question 1: Looking at the cartopy plot from Video 4.2.6, do the birds in this dataset prefer to fly over land, sea,
            # or the coast when migrating?
# Solution 1: The coast