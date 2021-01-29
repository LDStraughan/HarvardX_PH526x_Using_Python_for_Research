##############
# CASE STUDY 4
##############
# In this case study, we have prepared step-by-step instructions for you on how to prepare plots in Bokeh, a library
# designed for simple, interactive plotting.  We will demonstrate Bokeh by continuing the analysis of Scotch whiskies.
# Before you start the exercises, run the following code to get everything you'll need set up:
from sklearn.cluster.bicluster import SpectralCoclustering
import numpy as np, pandas as pd
whisky = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@whiskies.csv", index_col=0)
correlations = pd.DataFrame.corr(whisky.iloc[:,2:14].transpose())
correlations = np.array(correlations)
whisky
correlations
###############
# EXERCISES 1-3
###############
#   Exercise 1: In this exercise, we provide a basic demonstration of an interactive grid plot using Bokeh. Make sure to
#               study this code now, as we will edit similar code in the exercises that follow.
#       Instructions:
#       - Execute the following code and follow along with the comments. We will later adapt this code to plot the
#       correlations among distillery flavor profiles as well as plot a geographical map of distilleries colored by
#       region and flavor profile.
#       - Once you have plotted the code, hover, click, and drag your cursor on the plot to interact with it.
#       Additionally, explore the icons in the top-right corner of the plot for more interactive options!
#   Solution 1:
# The first value is the x coordinate, and the second value is the y coordinate.
        # Let's store these in separate lists.
        import bokeh
        xs, ys = zip(*grid)
        print(xs)
        print(ys)
        # Now we will make a list of colors, alternating between red and blue.
        colors = [plot_colors[i%2] for i in range(len(grid))]
        print(colors)
        # Finally, let's determine the strength of transparency (alpha) for each point,
        # where 0 is completely transparent.
        alphas = np.linspace(0, 1, len(grid))
        # Bokeh likes each of these to be stored in a special dataframe, called
        # ColumnDataSource.  Let's store our coordinates, colors, and alpha values.
        source = ColumnDataSource(
            data = {
                "x": xs,
                "y": ys,
                "colors": colors,
                "alphas": alphas,
            }
        )
        # We are ready to make our interactive Bokeh plot!
        from bokeh.plotting import figure, output_file, show
        from bokeh.models import HoverTool
        output_file("Basic_Example.html", title="Basic Example")
        fig = figure(tools="hover")
        fig.rect("x", "y", 0.9, 0.9, source=source, color="colors",alpha="alphas")
        hover = fig.select(dict(type=HoverTool))
        hover.tooltips = {
            "Value": "@x, @y",
            }
        show(fig)

#   Exercise 2: In Exercise 2, we will create the names and colors we will use to plot the correlation matrix of whisky
#               flavors. Later, we will also use these colors to plot each distillery geographically.
#
#       Instructions:
#       - Create a dictionary region_colors with regions as keys and cluster_colors as values.
#       - Print region_colors.
#       Use this code to get started:
#           cluster_colors = ['#0173b2', '#de8f05', '#029e73', '#d55e00', '#cc78bc', '#ca9161']
#           regions = ["Speyside", "Highlands", "Lowlands", "Islands", "Campbelltown", "Islay"]
#           region_colors = ## ENTER CODE HERE! ##
#       What color is associated with the key "Campbelltown" in the region_colors dictionary?
#   Solution 2:
        cluster_colors = ['#0173b2', '#de8f05', '#029e73', '#d55e00', '#cc78bc', '#ca9161']
        regions = ["Speyside", "Highlands", "Lowlands", "Islands", "Campbelltown", "Islay"]
        region_colors = dict(zip(regions, cluster_colors))
        region_colors # Answer = #cc78bc

#   Exercise 3: correlations is a two-dimensional np.array with both rows and columns corresponding to distilleries and
#               elements corresponding to the flavor correlation of each row/column pair. In this exercise, we will
#               define a list correlation_colors, with string values corresponding to colors to be used to plot each
#               distillery pair. Low correlations among distillery pairs will be white, high correlations will be a
#               distinct group color if the distilleries from the same group, and gray otherwise.
#       Instructions:
#       - Edit the code to define correlation_colors for each distillery pair to have input 'white' if their correlation
#       is less than 0.7.
#       - whisky is a pandas dataframe, and Group is a column consisting of distillery group memberships. For distillery
#       pairs with correlation greater than 0.7, if they share the same whisky group, use the corresponding color from
#       cluster_colors. Otherwise, the correlation_colors value for that distillery pair will be defined as 'lightgray'.
#   Solution 3:
        distilleries = list(whisky.Distillery)
        correlation_colors = []
        for i in range(len(distilleries)):
            for j in range(len(distilleries)):
                if correlations.iloc[i, j] <= 0.7:
                    correlation_colors.append('white')         # Use white
                else:                                          # Otherwise,
                    if whisky.Group[i] == whisky.Group[j]:
                        correlation_colors.append(cluster_colors[whisky.Group[i]]) # Colour by group
                    else:                                      # Otherwise,
                        correlation_colors.append('lightgray') # Use lightgray

#   Exercise 4: In Exercise 4, we will edit the given code to make an interactive grid of the correlations among
#               distillery pairs based on the quantities found in previous exercises. Most plotting specifications are
#               made by editing ColumnDataSource, a bokeh structure used for defining interactive plotting inputs. The
#               rest of the plotting code is already complete.
#       Instructions:
#       - correlation_colors is a list of string colors for each pair of distilleries. Set this as color in
#       ColumnDataSource.
#       - Define correlations in source using correlations from the previous exercise. To convert correlations from a
#       np.array to a list, use the flatten() method. This correlation coefficient will be used to define both the color
#       transparency as well as the hover text for each square.
#   Solution 4:
        from bokeh.models import ColumnDataSource
        from bokeh.plotting import figure, output_file, show
        from bokeh.models import HoverTool
        from bokeh.io import export_png
        source = ColumnDataSource(
            data = {
                "x": np.repeat(distilleries,len(distilleries)),
                "y": list(distilleries)*len(distilleries),
                "colors": correlation_colors,
                "correlations": correlations.values.flatten(),
            }
        )
        output_file("Whisky Correlations.html", title="Whisky Correlations")
        fig = figure(title="Whisky Correlations",
            x_axis_location="above", x_range=list(reversed(distilleries)), y_range=distilleries,
            tools="hover,box_zoom,reset")
        fig.grid.grid_line_color = None
        fig.axis.axis_line_color = None
        fig.axis.major_tick_line_color = None
        fig.axis.major_label_text_font_size = "5pt"
        fig.xaxis.major_label_orientation = np.pi / 3
        fig.rect('x', 'y', .9, .9, source=source,
             color='colors', alpha='correlations')
        hover = fig.select(dict(type=HoverTool))
        hover.tooltips = {
            "Whiskies": "@x, @y",
            "Correlation": "@correlations",
        }
        show(fig) # Answer = Blue

#   Exercise 5: In this exercise, we give a demonstration of plotting geographic points.
#       Instructions:
#       - Run the following code, to be adapted in the next section. Compare this code to that used in plotting the
#       distillery correlations.
#   Solution 5:
        points = [(0,0), (1,2), (3,1)]
        xs, ys = zip(*points)
        colors = ['#0173b2', '#de8f05', '#029e73']
        output_file("Spatial_Example.html", title="Regional Example")
        location_source = ColumnDataSource(
            data={
                "x": xs,
                "y": ys,
                "colors": colors,
            }
        )
        fig = figure(title = "Title",
            x_axis_location = "above", tools="hover, save")
        fig.plot_width  = 300
        fig.plot_height = 380
        fig.circle("x", "y", size=10, source=location_source,
             color='colors', line_color = None)
        hover = fig.select(dict(type = HoverTool))
        hover.tooltips = {
            "Location": "(@x, @y)"
        }
        show(fig)

#   Exercise 6: In Exercise 6, we will define a function location_plot(title, colors) that takes a string title and a
#               list of colors corresponding to each distillery and outputs a Bokeh plot of each distillery by latitude
#               and longitude. It will also display the distillery name, latitude, and longitude as hover text.
#       Instructions:
#       - Adapt the given code beginning with the first comment and ending with show(fig) to create the function
#       location_plot(), as described above.
#       - Region is a column of in the pandas dataframe whisky, containing the regional group membership for each
#       distillery. Make a list consisting of the value of region_colors for each distillery, and store this list as
#       region_cols.
#       - Use location_plot to plot each distillery, colored by its regional grouping.
#       Consider the bottom green point of the given plot. What is the distillery associated with this point?
#   Solution 6:
        def location_plot(title, colors):
            output_file(title+".html")
            location_source = ColumnDataSource(
                data = {
                    "x": whisky[" Latitude"],
                    "y": whisky[" Longitude"],
                    "colors": colors,
                    "regions": whisky.Region,
                    "distilleries": whisky.Distillery
                }
            )
            fig = figure(title = title,
                x_axis_location = "above", tools="hover, save")
            fig.plot_width  = 400
            fig.plot_height = 500
            fig.circle("x", "y", size=9, source=location_source, color='colors', line_color = None)
            fig.xaxis.major_label_orientation = np.pi / 3
            hover = fig.select(dict(type = HoverTool))
            hover.tooltips = {
                "Distillery": "@distilleries",
                "Location": "(@x, @y)"
            }
            show(fig)

        region_cols = [region_colors[i] for i in list(whisky.Region)]
        location_plot("Whisky Locations and Regions", region_cols) # Answer = Bladnoch

#   Exercise 7: In Exercise 7, we will use this function to plot each distillery, colored by region and taste
#               coclustering classification, respectively.
#       Instructions:
#       - Create the list region_cols consisting of the color in region_colors that corresponds to each whisky in
#       whisky.Region.
#       - Similarly, create a list classification_cols consisting of the color in cluster_colors that corresponds to
#       each cluster membership in whisky.Group.
#       - Create two interactive plots of distilleries, one using region_cols and the other with colors defined by
#       classification_cols. Consider how well the coclustering groupings match the regional groupings.
#       Consider the classification_cols plot. What color is the point associated with the distillery Bladnoch?
#   Solution 7:
        region_cols = [region_colors[i] for i in list(whisky.Region)]
        classification_cols = [cluster_colors[i] for i in list(whisky.Group)]

        location_plot("Whisky Locations and Regions", region_cols)
        location_plot("Whisky Locations and Groups", classification_cols)      # Answer = Blue