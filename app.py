from shiny import App, ui, render
from pathlib import Path
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import requests
# will also need to import the hypothesis testing library

# reading in df

infile = Path(__file__).parent / "video_statistics.csv"
df = pd.read_csv(infile)

# maybe export to xlsx
#df = pd.read_csv('video_statistics.csv')

# import xlsx file video_statistics.xlsx
#my_df = pd.read_excel('video_statistics.xlsx')


from shiny import App, render, ui

app_ui = ui.page_fluid(


    ui.h2("Visualizing One Variable"),
    ui.input_selectize("hist", "Select a variable:", ["Views", "Likes", "Comments"]),
    ui.output_plot("marketplot"),


    ui.h2("Visualizing the Relationship Between Two Variables"),
    ui.input_selectize("var1", "Select a variable:", ["Title", "Days Since Published","Views", "Likes", "Comments","Duration", "Comment to View Ratio", "Like to View Ratio"]),
    ui.input_selectize("var2", "Select a second variable:", ["Title", "Days Since Published","Views", "Likes", "Comments","Duration", "Comment to View Ratio", "Like to View Ratio"]),


    ui.h2("Comparing Comment to View and Like to View Ratios"),
    ui.input_selectize("video1", "Select a video:", df['Title']),
    ui.input_selectize("video2", "Select a second video:", df['Title']),

)


def server(input, output, session):
    @output
    @render.plot()
    def marketplot():
        x = input.hist()
        # hist with 30 bins
        fig = plt.hist(df[x], bins=30)
        plt.title(f"Chicago High Temperature Prediction Markets for {input.targetdate()}")
        plt.xlabel("Predition Markets")
        plt.ylabel("Yes ask");
        return fig 


app = App(app_ui, server, debug = True)