###########################################
# 2.3.1 INTRODUCTION TO MATPLOTLIB & PYPLOT
###########################################
# Matplotlib = produces publication-quality figures
# Can be used in Python scripts and while using interactive mode

# Pyplot = collection of functions that make matplotlib work like matlab
# Especially useful for interactive work

# Import:
import matplotlib.pyplot as plt
plt.plot([0,1,4,9,16]) # If you don't want matplotlib object to print, add semi-colon at the end of the line
# plt.show will bring up the plot when working in Python Shell

# Give Plot 2 Arguments:
import numpy as np # Need numpy for linspace/logspace
x = np.linspace(0,10,20)
y = x**2
x # Returns "array([ 0.        ,  0.52631579,  1.05263158,  1.57894737,  2.10526316, 2.63157895,  3.15789474,
  # 3.68421053,  4.21052632,  4.73684211, 5.26315789,  5.78947368,  6.31578947,  6.84210526,  7.36842105,
  # 7.89473684,  8.42105263,  8.94736842,  9.47368421, 10.        ])"
y # Returns "array([  0.        ,   0.27700831,   1.10803324,   2.49307479, 4.43213296,   6.92520776,   9.97229917,
  # 13.5734072 , 17.72853186,  22.43767313,  27.70083102,  33.51800554, 39.88919668,  46.81440443,  54.29362881,
  # 62.32686981, 70.91412742,  80.05540166,  89.75069252, 100.        ])"
plt.plot(x,y);

# 3rd argument can specify colour, marker and line type
x = np.linspace(0, 10, 20)
y1 = x**2.0
y2 = x**1.5
plt.plot(x,y1, "bo-"); # b = blue; o = circles; - = solid line
plt.plot(x,y1, "bo-", linewidth=2, markersize=4); # Can add keyword arguments
plt.plot(x,y1, "gs-"); # g = green; s = squares

##################################################
# 2.3.1 INTRODUCTION TO MATPLOTLIB & PYPLOT - Quiz
##################################################
# Question 1: What does plt.show() do?
# Solution 1: Show a plot that is already created.

# Question 2: What does plt.plot([0,1,2],[0,1,4],"rd-") do?
# Solution 2: A plot of two connected lines, with red diamonds at the junctures.

#############################
# 2.3.2 CUSTOMISING YOUR PLOT
#############################
# Add Legend = legend()
# Add Axes = axis()
# Set Axes Labels = xlabel(), ylabel()
# Save Figure = savefig() - file format extension specifies format of the file

# Add these elements to old plots:
x = np.linspace(0, 10, 20)
y1 = x**2.0
y2 = x**1.5
plt.plot(x,y1, "bo-", linewidth=2, markersize=4, label = "First"); # Need label for legend
plt.plot(x,y2, "gs-", linewidth=2, markersize=4, label = "Second"); # Need label for legend
plt.xlabel("$X$") # $ = X in italics
plt.ylabel("$Y$") # $ = Y in italics
plt.axis([-0.5, 10.5, -5, 105]) # plt.axis([xmin, xmax, ymin, ymax])
plt.legend(loc = "upper left")
plt.savefig("myplot.pdf")

#######################################
# 2.3.3 PLOTTING USING LOGARITHMIC AXES
#######################################
# Logarithm is taken by default in base 10

# semilogx() = x-axes on log scale and y in original scale
# semilogy() = y axes on log scale and x in original scale
# loglog() = x & y on log scale

x = np.linspace(0, 10, 20)
y1 = x**2.0
y2 = x**1.5
plt.loglog(x,y1, "bo-", linewidth=2, markersize=4, label = "First"); # loglog() makes straight lines
plt.loglog(x,y2, "gs-", linewidth=2, markersize=4, label = "Second"); # loglog() makes straight lines
plt.xlabel("$X$") # $ = X in italics
plt.ylabel("$Y$") # $ = Y in italics
plt.axis([-0.5, 10.5, -5, 105]) # plt.axis([xmin, xmax, ymin, ymax])
plt.legend(loc = "upper left")

# If you want evenly spaced points on loglog, make logspace instead of linspace
x = np.logspace(-1, 1, 40) # first point = 0.1; end point = 10; 40 points
y1 = x**2.0
y2 = x**1.5
plt.loglog(x,y1, "bo-", linewidth=2, markersize=4, label = "First"); # loglog() makes straight lines
plt.loglog(x,y2, "gs-", linewidth=2, markersize=4, label = "Second"); # loglog() makes straight lines
plt.xlabel("$X$") # $ = X in italics
plt.ylabel("$Y$") # $ = Y in italics
plt.axis([-0.5, 10.5, -5, 105]) # plt.axis([xmin, xmax, ymin, ymax])
plt.legend(loc = "upper left")

##############################################
# 2.3.3 PLOTTING USING LOGARITHMIC AXES - Quiz
##############################################
# Question 1: Consider the following code:
#               x = np.logspace(0,1,10)
#               y = x**2
#               plt.loglog(x,y,"bo-")
#           What does this return?
# Solution 1: A logarithmic plot that looks like a straight line with equal spacing

#############################
# 2.3.4 GENERATING HISTOGRAMS
#############################
# Generate Histogram = plt.hist()

# Practice:
x = np.random.normal(size = 1000)
plt.hist(x); # Check online documentation for all optional parameters

plt.hist(x, density = True); # Proportion of observation per bin, rather than no. of observations
plt.hist(x, density = True, bins = np.linspace(-5, 5, 21)); # Provide location of bins

# Gamma Distribution:
x = np.random.gamma(2,3,1000000)

plt.figure()
plt.subplot(221)
plt.hist(x, bins = 30)
plt.subplot(222)
plt.hist(x, bins = 30, density = True)
plt.subplot(223)
plt.hist(x,bins = 30, cumulative = True)
plt.subplot(224)
plt.hist(x, bins = 30, density = True, cumulative = True, histtype = "step")

# Beautiful Code Example:
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

mu = 200
sigma = 25
n_bins = 50
x = np.random.normal(mu, sigma, size=100)

fig, ax = plt.subplots(figsize=(8, 4))

# plot the cumulative histogram
n, bins, patches = ax.hist(x, n_bins, density=True, histtype='step',
                           cumulative=True, label='Empirical')

# Add a line showing the expected distribution.
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
y = y.cumsum()
y /= y[-1]

ax.plot(bins, y, 'k--', linewidth=1.5, label='Theoretical')

# Overlay a reversed cumulative histogram.
ax.hist(x, bins=bins, density=True, histtype='step', cumulative=-1,
        label='Reversed emp.')

# tidy up the figure
ax.grid(True)
ax.legend(loc='right')
ax.set_title('Cumulative Step Histograms')
ax.set_xlabel('Annual rainfall (mm)')
ax.set_ylabel('Likelihood of occurrence')

plt.show()

####################################
# 2.3.4 GENERATING HISTOGRAMS - Quiz
####################################
# Question 1: Which will have wider bins, np.linspace(-5,5,21) or np.linspace(-5,5,201)?
# Solution 1: np.linspace(-5,5,21)

# Question 2: What will plt.subplot(333) do?
# Solution 2: Create a smaller subplot in the top right of the figure.

# Question 3: Will plt.subplot(3, 3, 3) create a different plot from plt.subplot(333)?
# Solution 3: No - The triple-digit integer in the first argument of plt.subplot works the same as three single-digit
                   # function arguments.