import streamlit as st
import pandas_datareader.data as web
import pandas as pd
from datetime import datetime
import numpy as np
from reddit_scraper_module import RedditData as rd
from Vader_Working_File import vaderReddit as vd
from psaw import PushshiftAPI
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import plotly.express as px
sia = SentimentIntensityAnalyzer()


st.title("Welcome to StockNLP's Dashboard 🚀")
st.markdown("Here, we show you the ongoing sentiment of any stock of your choosing. We then run a simulated trade and **show you the money!** 💰💰💰")
USER_INPUT = st.text_input("Please enter a stock ticker symbol like so: '$AMC'")

STOCK_INPUT = USER_INPUT[1:].lower()

DF = web.DataReader(STOCK_INPUT, 'yahoo', datetime(2016, 1, 1), datetime.today()) 


INCREASING_COLOR = '#12AF4A'
DECREASING_COLOR = '#D83916'

def get_candlestick_chart():
    '''
        This is a function that takes no parameters and makes a candlestick visualization with the given stock user input.
    '''
    data=[dict(
        type='candlestick',
        open=DF.Open,
        high = DF.High,
        low = DF.Low,
        close = DF.Close,
        x = DF.index,
        yaxis = 'y2',
        name = STOCK_INPUT,
        increasing = dict(line = dict(color = INCREASING_COLOR)),
        decreasing = dict(line = dict(color = DECREASING_COLOR)),
    )]

    layout = dict()

    fig = dict(data=data, layout=layout)


    fig['layout'] = dict()
    fig['layout']['plot_bgcolor'] = 'rgb(255,255,255)'
    fig['layout']['xaxis'] = dict(rangeselector = dict(visible = True))
    fig['layout']['yaxis'] = dict(domain = [0, 0.2], showticklabels = False)
    fig['layout']['yaxis2'] = dict(domain = [0.2, 0.8])
    fig['layout']['legend'] = dict(orientation = 'h', y=0.9, x=0.3, yanchor='bottom')
    fig['layout']['margin'] = dict(t=40, b=40, r=40, l=40)


    range_selector = dict(
        visible = True,
        x = 0, y = 0.9,
        bgcolor = 'rgba(150, 200, 250, 0.4)',
        font = dict(size = 13),
        buttons=list([
            dict(count=1,
                label='reset',
                step='all'),
            dict(count=1,
                label='1yr',
                step='year',
                stepmode='backward'),
            dict(count=3,label='3 mo',step='month',stepmode='backward'),
            dict(count=1,label='1 mo',step='month',stepmode='backward'),
            dict(step='all')
        ]))
        
    fig['layout']['xaxis']['rangeselector'] = range_selector

    def movingaverage(interval, window_size=10):
        window = np.ones(int(window_size))/float(window_size)
        return np.convolve(interval, window, 'same')

    mv_y = movingaverage(DF.Close)
    mv_x = list(DF.index)

    # Clip the ends
    mv_x = mv_x[5:-5]
    mv_y = mv_y[5:-5]

    fig['data'].append(dict(x=mv_x, y=mv_y, type='scatter', mode='lines',
                            line = dict( width = 1),
                            marker = dict( color = '#E377C2'),
                            yaxis = 'y2', name='Moving Average'))



    colors = []

    for i in range(len(DF.Close)):
        if i != 0:
            if DF.Close[i] > DF.Close[i-1]:
                colors.append(INCREASING_COLOR)
            else:
                colors.append(DECREASING_COLOR)
        else:
            colors.append(DECREASING_COLOR)


    #VOLUME BAR CHARTS
    fig['data'].append(dict(x=DF.index, y=DF.Volume,                   
                            marker=dict(color=colors),
                            type='bar', yaxis='y', name='Volume'))


    def bbands(price, window_size=10, num_of_std=5):
        rolling_mean = price.rolling(window=window_size).mean()
        rolling_std = price.rolling(window=window_size).std()
        upper_band = rolling_mean + (rolling_std*num_of_std)
        lower_band = rolling_mean - (rolling_std*num_of_std)
        return rolling_mean, upper_band, lower_band

    bb_avg,bb_upper,bb_lower = bbands(DF.Close)

    fig['data'].append(dict(x=DF.index, y=bb_upper, type='scatter', yaxis='y2',
                            line = dict(width = 1),
                            marker=dict(color='#ccc'), hoverinfo='none',
                            legendgroup='Bollinger Bands', name='Bollinger Bands'))

    fig['data'].append(dict(x=DF.index, y=bb_lower, type='scatter', yaxis='y2',
                            line = dict(width = 1),
                            marker=dict(color='#ccc'), hoverinfo='none',
                            legendgroup='Bollinger Bands', showlegend=False))
    return fig


# We get the candlestick chart with the following call and display it within streamlit with the 'plotly_chart' call. 
chart = get_candlestick_chart()
st.plotly_chart(chart)

def get_reddit_data():
    '''
        This is a helper function used inside the has_special_chars() function that takes
        in a string as an input and returns boolean True if the passed string contains a
        special character.
    '''
    df_reddit = pd.DataFrame(columns = ['Date','Comment', 'Tags'])
    #subreddits = ['wallstreetbets', 'robinhood', 'stocks', 'investing']
    #channel = str(input('Please input which subreddit you want to search: '+ str(subreddits) ))
    start_time = int(datetime(2021, 10, 1).timestamp())
    api = PushshiftAPI()
    df_master = pd.read_csv('/Users/yash/Downloads/reddit_working.csv', index_col = 0)
    submissions = list(api.search_submissions(after=start_time,
                       subreddit='wallstreetbets',
                       filter=['author', 'title', 'subreddit', 'subscribers',
                               'comment_score_hide_mins', 'created_utc'],
                       limit=100))
    tag, comment, date = rd.cashtags(submissions)
    rd.add_to_df(tag, comment, date, df_reddit)
    vd.add_vader_scores(df_reddit)
    vd.add_vader_weighted_sentiments(df_reddit)
    df_master = df_master.append(df_reddit)
    df_master.to_csv("/Users/yash/Downloads/reddit_working.csv")
    master_df = pd.read_csv("/Users/yash/Downloads/reddit_working.csv", index_col = 0)
    print(df_reddit)
    red_score = vd.get_subset(USER_INPUT, master_df)
    print(red_score)
    red_final = vd.get_score(red_score)
    print(red_final)
    return pd.DataFrame(red_final).reset_index()

score_reddit = get_reddit_data()


def get_senti_trend(df):
    fig = px.line(df, x=df['Date'], y=df['Sentiment_Score'], title='Sentiment Trend')
    return fig
fig = get_senti_trend(score_reddit)
#print(fig)
st.plotly_chart(fig)   

   