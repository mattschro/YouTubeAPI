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

def extract_data(df, video1, video2):
    # Extract the rows for video1 and video2
    video1_data = df[(df['Title and Day Published'] == video1)]
    video2_data = df[(df['Title and Day Published'] == video2)]
    # Extract the specified columns
    #video1_data = video1_data[['Days Since Published', 'Views', 'Views per Day', 'Likes', 'Like to View Ratio', 'Comments', 'Comment to View Ratio', 'Duration in Minutes']]
    #video2_data = video2_data[['Days Since Published', 'Views', 'Views per Day', 'Likes', 'Like to View Ratio', 'Comments', 'Comment to View Ratio', 'Duration in Minutes']]
    # Create a new column 'Difference' which is the difference between the values of the extracted columns
   #video1_data['Difference'] = video1_data.sub(video2_data)
    return video1_data

# graph inputs
graph_inputs = ["Views", "Views Per Day","Likes", "Like to View Ratio","Comments","Comment to View Ratio", "Duration in Minutes", "Days Since Published"]
 
app_ui = ui.page_fluid(


    ui.h2("Visualizing One Variable"),
    ui.input_selectize("hist", "Select a variable:", graph_inputs),
    ui.output_plot("histogram"),


    ui.h2("Visualizing the Relationship Between Two Variables"),
    ui.input_selectize("var1", "Select X-Axis:", graph_inputs[::-1]),
    ui.input_selectize("var2", "Select Y-Axis:", graph_inputs),
    ui.output_plot("scatterplot"),

    ui.p("I could incoporate some bivatiate analysis like R^2 here..."),


    ui.h2("Comparing the Performance of Two Videos"),
    #ui.h2("Hypothesis Testing: Comparing Comment to View and Like to View Ratios"),
    #ui.p("Maybe Change the Title to Comparing Two Videos?"),
    ui.input_selectize("video1", "Select a video:", df['Title and Day Published']),
    ui.input_selectize("video2", "Select a second video:", df['Title and Day Published'].iloc[::-1]),
    ui.output_table("data_table"),

    ui.output_text("txt"),
    


   
    ui.p("The comment to view ratio is the number of comments divided by the number of views. The like to view ratio is the number of likes divided by the number of views."),


)


def server(input, output, session):
    @output
    @render.plot()
    def histogram():
        x = input.hist()
        # hist with 30 bins
        plt.hist(df[x], bins=30)
        plt.xlabel('Value')
        plt.ylabel('Count')
        plt.title("Histogram of {}".format(x))

    @output
    @render.plot()
    def scatterplot():
        x = 'Views'
        y = 'Duration in Minutes'
        x = input.var1()
        y = input.var2()
        # hist with 30 bins
        fig_2 = plt.scatter(df[x], df[y])
        # title
        plt.title("Scatterplot of {} vs {}".format(x, y))
        # x and y labels
        plt.xlabel(x)
        plt.ylabel(y)

    @output
    @render.table
    def data_table():
        v1 = input.video1()
        v2 = input.video2()
        
        #data = extract_data(df, video1, video2)
        #video1_data = df[df['Title and Day Published'] == video1]
        #video2_data = df[df['Title and Day Published'] == v2]

        #video1_data = df.loc[df['Title'] == video1]

        v1_df = pd.DataFrame(df.iloc[int(v1)]).T
        v2_df = pd.DataFrame(df.iloc[int(v2)]).T

        final_df = pd.concat([v1_df, v2_df], axis = 0)

        # don't display the columns Title and Day Published, Publish Time, and Duration in Seconds
        final_df = final_df.drop(columns = ['Title and Day Published', 'Publish Time (EST)', 'Duration in Seconds'])
        return final_df

    @output
    @render.text
    def txt():
        return "7"

app = App(app_ui, server, debug = True)