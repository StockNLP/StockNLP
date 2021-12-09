[![HitCount](http://hits.dwyl.com/StockNLP/WorkingRepo.svg?style=flat-square)](http://hits.dwyl.com/StockNLP/WorkingRepo)
[![Build Status](https://travis-ci.org/{ORG-or-USERNAME}/{REPO-NAME}.png?branch=master)](https://travis-ci.org/StockNLP/WorkingRepo)
[![Known Vulnerabilities](https://snyk.io/test/github/dwyl/hapi-auth-jwt2/badge.svg?targetFile=package.json)](https://snyk.io/test/github/dwyl/hapi-auth-jwt2?targetFile=package.json)
# StockNLP

A package to give investors actionable insights on stock market trends on popular stocks that were heavily influenced by the investors on social media.

## Project Contributors

Yash Patel, Moses, Nelson, Aditya and Samartha

## Project Objective:

In recent months, we have witnessed a significant shift in stock market prices through social media influence. Tweets and reddit submissions by popular personalities have influenced and increased the stock prices of certain stocks such as $AMC, $GME, $DOGE, etc over 100% over their all time price. This phenomenon drew our team’s attention to study the social media trend on the stock market. As social media is vast and to scope our project, we are studying the social media sentiment of two prominent platforms Twitter and Reddit. 

Our primary objective involves developing an interactive dashboard for the retail and institutional investors to analyze the effect of social media sentiment along with stock metrics to draw meaningful and insightful actions / observations. 

## Requirements

The project requires authorization to Twitter and Reddit API. For reddit, our team used PushShift.io API. Please click on this [link](https://github.com/pushshift/api) for more information. In the case of Twitter, please apply for the developer account. The approval time might take 2-24 hours depending on the nature of the request. Please visit this [link](https://developer.twitter.com/en/portal/dashboard) for more information. The project also requires a latest python version (3.9.x). ).

## Directory Structure
```
 .
 ├── code
 │   ├── twitter_class
 │   └── reddit_scraper_module
 │   └── yfinance_automated_script
 │   └── yfinance_download
 ├── data
 │   ├── Reddit Data
 │   └── Twitter Data
 │   └── Stock Data
 ├── examples
 │   └── RedditScraping copy
 │   └── RedditScraping
 │   └── Twitter_automated_script
 │   └── Vader Sentiment scores
 │   └── Vader_Working_File
 │   └── yfinance_automated_script
 │   └── yfinance_download
 ├── tests
 │   └── test_redditscraping
 │   └── test_rl
 │   └── test_twitscrap_vader
 │   └── test_vaderreddit
 │   └── test_yfinancescraping
 ├── LICENSE
 ├── README.md
 ├── app.py
 ├── environment.yml
 ├── requirements.txt
 └── setup.py
 ```
## Installation 

The package Stock NLP can be installed using the following instructions.

 1. Please open the terminal of your choice.
 2. Clone the repository using: `git clone  https://github.com/StockNLP` 
 3. Change the directory to StockNLP root directory, by running the command: `cd StockNLP`
 4. Now, set up a new virtual environment using the command: `conda create -n stockNLP`
 5. Activate the stockNLP virtual environment by running the command: `conda activate stockNLP`
 6. Install the package requirements by using the command: `pip/conda install -r requirements.txt`

## Tool
StockNLP contains social media submissions sentiment scores through specific modules that contain three classes of functions and a main.

 1. We have a main function that calls the APIs of Twitter and Reddit to extract the social media submissions. We subsequently point them to respective TwitterData and RedditData classes.
 2. The TwitterData and RedditData class files have helper functions that help to preprocess the data and get them into a working dataframe.
 3. The Vader class apparently adds the sentiment scores and metrics to the workable data frame that is extracted in the previous step.
 4. We then pass this extracted dataframe from the deep learning model that factors the sentiment score into a simulated trading model.


## Mission

The mission for the prject are as follows:

  1. Obtain data from Twitter and Reddit submissions primarily to obtain the sentiment score on popular stocks.
  2. Preprocess the available data so that it can readily be used by the deep learning models.
  3. Perform sentiment analysis on the data and obtain weighted polarity scores for each input.
  4. Train a machine learning algorithm to capture the “bullish” or “bearish” market sentiment based on the developed model
  5. Report back to the user about the existing hot stock in the market
  6. Prepare a User Interface that is dynamic to show the trend of a particular stock using social media sentiment as a metric. 


## User Stories for our project:

The long term users can be like financial analysts or quantitative analysts or developers. They could leverage the current NLP model to find and make insights out of it. The main investors are retail investors. 

The researcher could take a look at the mathematical standpoint of our machine learning model. They constantly work on the model’s formulas to check the underlying model trend analysis. They can act as a checks and balances wing for our models. The skill level of the researcher is high in terms of understanding the algorithms, performance metrics. They might not have a similar skill level in terms of coding it and optimizing it, for which there are always technical teams to help.


The users for our project can be any stock enthusiasts. The retail investors can understand the market dynamics, flow and trend. Based on the analytics insights and performance metrics, they can have a basis to formulate investment and trading strategies.
 
#### Skill level of the use case: The skill level required by a common stock investor is proficiency with the stock names and navigation with a simple smart device such as a mobile, tablet or laptop. The user further requires an ability to read a dynamic graphs in the dashboard.

## Description a use case:

**Information User Provides:** They provide the stock information that they want to check. (Which is typically like a ticker system). 

**Information that system provides:** We as a team would use the pre-trained machine learning model to cross reference the current social media trend and compare to the model and give them an insight of the investment strategy for the next few hours. We will provide them signal strength of the stocks with visualizations.

## Contribution

If you are interested in making contributions to the repository, please add your contributions and generate a pull request.

## Acknowledgement 

This project is created as a part of CSE 583- Software Development for Data Scientists at University of Washington - Seattle. We thank Prof. David Beck and Anant Mittal for extending their support and encouragement for this project.

