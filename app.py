from shiny import App, ui, render
from pathlib import Path
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import requests
# will also need to import the hypothesis testing library (scipy.stats.ttest_ind)

# reading in df
infile = Path(__file__).parent / "video_statistics.csv"
df = pd.read_csv(infile)


from shiny import App, render, ui

# Create a scatter plot function
def create_scatter_plot(x, y):
    plt.scatter(df[x], df[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title("Scatterplot of {} vs {}".format(x, y))
    plt.show()
    return plt

app_ui = ui.page_fluid(


    ui.h2("Visualizing One Variable"),
    ui.input_selectize("hist", "Select a variable:", ["Views", "Views per Day","Likes", "Like to View Ratio","Comments","Comment to View Ratio", "Duration in Minutes"]),
    ui.output_plot("histogram"),


    ui.h2("Visualizing the Relationship Between Two Variables"),
    ui.input_selectize("var1", "Select a variable:", ["Views", "Views Per Day","Likes", "Like to View Ratio","Comments","Comment to View Ratio", "Duration in Minutes"]),
    ui.input_selectize("var2", "Select a second variable:", ["Views", "Views Per Day","Likes", "Like to View Ratio","Comments","Comment to View Ratio", "Duration in Minutes"]),
    ui.output_plot("scatterplot"),

    ui.p("I could incoporate some bivatiate analysis like R^2 here..."),


    ui.h2("Hypothesis Testing: Comparing Comment to View and Like to View Ratios"),
    ui.input_selectize("video1", "Select a video:", df['Title and Day Published']),
    ui.input_selectize("video2", "Select a second video:", df['Title']),

   
    ui.p("The comment to view ratio is the number of comments divided by the number of views. The like to view ratio is the number of likes divided by the number of views."),

)


def server(input, output, session):
    @output
    @render.plot()
    def histogram():
        x = input.hist()
        # hist with 30 bins
        fig = plt.hist(df[x], bins=30)
        plt.title("Histogram of {}".format(x))
        #plt.xlabel("Predition Markets")
        #plt.ylabel("Yes ask");
        #plt.show()
       #fig = plt.show()
        #return 

    @output
    @render.plot()
    def scatterplot():
        x = input.var1()
        y = input.var2()
        # hist with 30 bins
        fig_2 = plt.scatter(df[x], df[y])
        # title
        plt.title("Scatterplot of {} vs {}".format(x, y))
        # x and y labels
        plt.xlabel(x)
        plt.ylabel(y)

        


app = App(app_ui, server, debug = True)