[![HitCount](http://hits.dwyl.com/StockNLP/WorkingRepo.svg?style=flat-square)](http://hits.dwyl.com/StockNLP/WorkingRepo)
[![Build Status](https://travis-ci.org/{ORG-or-USERNAME}/{REPO-NAME}.png?branch=master)](https://travis-ci.org/StockNLP/WorkingRepo)
[![Known Vulnerabilities](https://snyk.io/test/github/dwyl/hapi-auth-jwt2/badge.svg?targetFile=package.json)](https://snyk.io/test/github/dwyl/hapi-auth-jwt2?targetFile=package.json)
[![License](https://img.shields.io/badge/License-MIT-<COLOR>)]
# StockNLP

## User Stories for our project:

The long term users can be like financial analysts or quantitative analysts or developers. They could leverage the current NLP model to find and make insights out of it. The main investors are retail investors. 

The researcher could take a look at the mathematical standpoint of our machine learning model. They constantly work on the model’s formulas to check the underlying model trend analysis. They can act as a checks and balances wing for our models. The skill level of the researcher is high in terms of understanding the algorithms, performance metrics. They might not have a similar skill level in terms of coding it and optimizing it, for which there are always technical teams to help.


The users for our project can be any stock enthusiasts. The retail investors can understand the market dynamics, flow and trend. Based on the analytics insights and performance metrics, they can have a basis to formulate investment and trading strategies.
 
#### Skill level of the use case: The skill level of a common stock investor is proficiency with the stock names and navigation with a simple smart device such as a mobile, tablet or laptop. 

## Describing a use case:

### Use Case 1:

  Information User Provides: They provide the stock information that they want to check. (Which is typically like a ticker system). 

### Use Case 2: 

  Information that system provides: We as a team would use the pre-trained machine learning model to cross reference the current social media trend and compare to the model and give them an insight of the investment strategy for the next few hours. We will provide them signal strength of the stocks with visualizations.


## Specification of the Components:

### Component 1: 


  1. Name: Interactive Stock - Dashboard
  2. What it does: Displays the stock metrics, visualizations and trading strategies.
  3. Inputs (with type information): Stock Ticker Symbol (eg. $AAPL)
  4. Outputs (with type information): Sentiment Score, Stock Chart, Sentiment TimeSeries 
  5. How to use other components: The user inputs the ticker symbol and presses the process button to then get the visualizations and sentiment analytics from the data we fetch in real-time using APIs and then using NLP and machine learning to derive the sentiment metric.

### Component 2:

  1. Name: Data fetch functionality. (Our ML Model) 


### Component Specifications:

  1. Current Components of the Use Cases: 
  2. Components already available:
  3. Sub-components that are required to be implement those components that aren’t already available: Ingestion Engine, Our ML Model, Visualization Database
