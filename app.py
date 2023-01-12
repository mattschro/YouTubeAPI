from shiny import App, ui, render
from pathlib import Path
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import requests


# Part 1: ui ----
#img_output = output_image("monthlymax.png", width="100%")

app_ui = ui.page_fluid(
    # Model prediction
    ui.h2("Variable Input to Model Prediction"),
    ui.input_numeric("prcp", "Precipitation", value=0,min = 0, max = 10, step = .1),
    ui.input_numeric("snow", "Snow", value=0,min = 0, max = 10, step = .1),
    ui.input_numeric("tmin", "Minimum Temperature", value=40,min = 0, max = 75),
    ui.input_numeric("month", "Month", value=1,min = 1, max = 12),
    ui.input_numeric("threeday", "Three Day Rolling Average", value=0,min = 0, max = 90, step = .01),
    ui.input_numeric("sevenday", "Seven Day Rolling Average", value=0,min = 0, max = 90, step = .01),
    ui.output_text_verbatim("txt"),

    # Exploratory Data Analysis
    ui.h2("Exploratory Data Analysis"),
    ui.h4("Chart #1: Kalshi Categories"),
    ui.output_plot("category"),
    ui.h4("Chart #2: Number of Submarkets by Day"),
    ui.output_plot("submarket"),
    ui.h4("Chart #3: Monthly Max Temperature"),
    ui.img(src = "monthlymax.png", width="50%", height = "50%"),
    ui.h4("Chart #4: Pairplot"),
    ui.img(src = "pairplot.png", width="40%", height = "40%"),
    ui.h4("Chart #5: Kalshi Market Weather Category Distribution"),
    ui.output_plot("weather_mkts"),

     # Hist of Chicago high temperature market
    ui.h2("Kalshi's Chicago High Temperature Market"),
    ui.p("Choose a date to see Kalshi's Chicago high temperature market. You cannot chose a date that is more than two days into the future."),
    ui.p("Please consider this interactive visualization are our sixth and final exploratory data analysis chart."),
    ui.panel_sidebar(
    ui.input_date("targetdate", "Choose a date")      
    ),

    ui.panel_main(
        ui.output_text("w"),
        ui.output_plot("marketplot")
    ),

)





app = App(app_ui, server, static_assets=www_dir, debug = True)