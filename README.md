# YouTubeAPI
 
This project scrapes data from the MrBeast main channel and MrBeast Gaming channel using the YouTube API. The raw data is then cleaned, some new variables are made, and the code is setup to determine the daily views, comments, and likes for each video on both channels. 

- 'ViewsPrediction.ipynb' uses different statistical model to predict the number of views on each video on the main MrBeast channel
- 'app.py' is the code for the Python for Shiny dashboard was made for the MrBeast Gaming channel. It compares metrics about the channel (such as views per day, comments, duration in minutes, days since published, etc.).
- 'MrBeast.ipynb' is the code for accessing the main channel's (MrBeast) data from the YouTube API, as well as cleaning that data. There is also a function that determines the daily difference in number of views, likes, and comments. Thus, it can determine the popularity of videos on the channel each day. This code (slightly modified) is running daily on AWS Lambda. This data can be analyzed in the future once the Lambda function has been collecting data for a couple of months.
- 'MrBeastGaming.ipynb' is the same thing as 'MrBeast.ipynb' except it is for his side channel MrBeastGaming
- MrBeast/MrBeastGaming folders have the daily statistics and differences. These are incomplete right now and will be updated in the future after teh AWS Lambda function has had some time to collect data.

A video going over the Shiny for Python dashboard can be found here: https://user-images.githubusercontent.com/70669547/212502659-2ac6ae8f-3a15-4e53-8219-e4102e373017.mov. Due to some technical issues, this dashboard is not accessible from the internet and can only run locally, but that is in the process of being fixed.

