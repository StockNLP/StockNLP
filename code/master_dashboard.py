"""
This is the main working file for the StockNLP Project where we are importing the Reddit,
Twitter and the Vader module. Here, we will get a user input from the dashboard in the form
of a String of Stock Ticker Input and we will use as a parameter to get values from the
RedditAPI Module, Twitter API Module, and then map the values to Vader Module.
Parallely, we will also get the values from the Pandas.io Yahoo API using
the stock input asas search parameter and use the stock price data to run the
reinforcement learning algorithm at the end of this file. The results of the findings will
be disdplayed on the dashboad in 3 components:
1) The stock candlestick chart (Using the Yahoo API)
2) Sentiment Trend Chart (Using the Reddit, Twitter and Vader Modules)
3) Reinforcement Learning Algorithm (Using the RL Algorithm in this file)
"""
#pylint: disable=wrong-import-order
#pylint: disable=wrong-import-position
from datetime import datetime
import streamlit as st
import pandas_datareader.data as web
import pandas as pd
import os
import sys
sys.setrecursionlimit(30000)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
from psaw import PushshiftAPI
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import plotly.express as px
sia = SentimentIntensityAnalyzer()
from reddit_scraper_module import RedditData as rd
from vader_working_file import VaderReddit as vd
import math
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense
from keras.optimizers import Adam
import random
from collections import deque
import keras.backend.tensorflow_backend as tb
#pylint: disable= protected-access
tb._SYMBOLIC_SCOPE.value = True
#pylint: disable=line-too-long
#pylint: disable=redefined-outer-name
#pylint: disable=trailing-whitespace
#pylint: disable=bad-option-value
#pylint: disable=too-many-locals
#pylint: disable=use-dict-literal
#pylint: disable=unused-variable
#pylint: disable=too-many-instance-attributes
#pylint: disable=consider-using-with
#pylint: disable=simplifiable-if-expression
#pylint: disable=too-many-statements
st.title("Welcome to StockNLP's Dashboard 🚀")
st.markdown("Here, we show you the ongoing sentiment of any stock of your choosing. We then run"
            + "a simulated trade and **show you the money!** 💰💰💰")
USER_INPUT = st.text_input("Please enter a stock ticker symbol like so: '$AMC'")

#Converts $TSLA to tsla
STOCK_INPUT = USER_INPUT[1:].lower()

#Dataframe of the stock values using the Yahoo API from 1/1/2019 until today.
DF = web.DataReader(STOCK_INPUT, 'yahoo', datetime(2019, 1, 1), datetime.today())
#Saves the obtained Dataframe to a .csv for later use in the Reinforcement Learning Algorithm
DF.to_csv('/Users/yash/Downloads/'+STOCK_INPUT+'.csv')

#Number of Stocks we are looking at
WINDOW = 1
#Number iterations of the RL Algorithm
EPISODE = 1

INCREASING_COLOR = '#12AF4A'
DECREASING_COLOR = '#D83916'

def main():
    """[This is the main function that implements all of the functions on the backend of the 
        dashboard and the builds the frontend of the dashboard.]
    """
    def get_candlestick_chart():
        """[]

        Returns:
            [plotly chart]: [This function takes in the yahoo stock data and creates an interactive candlestick chart
            with a range slider and 3 custom indicators.]
        """
        
        data=[dict(
            type = 'candlestick',
            open = DF.Open,
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
        fig['layout']['plot_bgcolor'] = 'rgb(246,246,246)'
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
            """This function calculates the moving average for a given interval period of stock prices.

            Args:
                interval ([list]): [range of value to calculate within certain period]
                window_size (int, optional): [Range interval ]. Defaults to 10.

            Returns:
                [type]: [np.convolve list of moving average values]
            """
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
        #pylint: disable=consider-using-enumerate
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


        def bol_bands(price, window_size=10, num_of_std=5):
            rolling_mean = price.rolling(window=window_size).mean()
            rolling_std = price.rolling(window=window_size).std()
            upper_band = rolling_mean + (rolling_std*num_of_std)
            lower_band = rolling_mean - (rolling_std*num_of_std)
            return rolling_mean, upper_band, lower_band
        #pylint: disable=unused-variable
        bb_avg,bb_upper,bb_lower = bol_bands(DF.Close)

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
        red_score = vd.get_subset(USER_INPUT, master_df)
        red_final = vd.get_score(red_score)
        return pd.DataFrame(red_final).reset_index()

    score_reddit = get_reddit_data()

    def get_senti_trend(data_frame):
        fig = px.line(data_frame, x=data_frame['Date'], y=data_frame['Sentiment_Score'],template = "plotly_dark", title='Sentiment Trend')
        return fig
    fig = get_senti_trend(score_reddit)
    #print(fig)
    st.plotly_chart(fig)   

        
    class Agent:
        """[This is the Agent class of the reinforcement learning algorithm. It holds the functions to create the 
            deep learning model, the action and the expected_replay.]
        """
        def __init__(self, state_size, is_eval=False, model_name=""):
            self.state_size = state_size
            self.action_size = 3
            self.memory = deque(maxlen=1000)
            self.inventory = []
            self.model_name = model_name
            self.is_eval = is_eval
            self.gamma = 0.95
            self.epsilon = 1.0
            self.epsilon_min = 0.01
            self.epsilon_decay = 0.995
            self.model = load_model(model_name) if is_eval else self._model()
            
        def _model(self):
            model = Sequential()
            model.add(Dense(units=64, input_dim=self.state_size, activation="relu"))
            model.add(Dense(units=32, activation="relu"))
            model.add(Dense(units=8, activation="relu"))
            model.add(Dense(self.action_size, activation="linear"))
            model.compile(loss="mse", optimizer=Adam(lr=0.001))
            return model
        
        def act(self, state):
            """[defines what action should be taken based on state.]

            Args:
                state ([np.array of doubles]): [gets the reward/penalty array]

            Returns:
                [int]: [buy/hold/sell decision as an integer]
            """
            if not self.is_eval and random.random() <= self.epsilon:
                return random.randrange(self.action_size)
            options = self.model.predict(state)
            return np.argmax(options[0])
    
        def exp_replay(self, batch_size):
            """[Function to test model replay]

            Args:
                batch_size ([int]): [size of the batch.]
            """
            mini_batch = []
            len_memory = len(self.memory)
            for i in range(len_memory - batch_size + 1, len_memory):
                mini_batch.append(self.memory[i])
            for state, action, reward, next_state, done in mini_batch:
                target = reward
                if not done:
                    target = reward + self.gamma * np.amax(self.model.predict(next_state)[0])
                target_f = self.model.predict(state)
                target_f[0][action] = target
                self.model.fit(state, target_f, epochs=1, verbose=0)
            if self.epsilon > self.epsilon_min:
                self.epsilon *= self.epsilon_decay

    def format_price(number):
        """[It takes a float value and converts it to 2 decimal places and appends a '$' in front.
                            Returns the converted value.]

        Args:
            number ([float]): [The raw float value with multiple decimal places.]
        """
        #pylint: disable=consider-using-f-string
        return("-$" if number<0 else "$")+"{0:.2f}".format(abs(number))

    def sigmoid(x_value):
        """[takes in a value and gives applies the sigmoid function to it]

        Args:
            x_value ([int]): [price of stock]

        Returns:
            [float]: [returns the sigmoid value of the passed parameter]
        """
        return 1/(1+math.exp(-x_value))


    def get_state(data, t_value, n_value):
        """[gets the state of the environment]

        Args:
            data ([list]): [list of stock prices]
            t_value ([double]): [reward values]
            n_value ([double]): [penalty values]

        Returns:
            [np.array of doubles]: [penalty and reward array]
        """
        d_value = t_value - n_value + 1
        block = data[d_value:t_value + 1] if d_value >= 0 else -d_value * [data[0]] + data[0:t_value + 1]
        res = []
        for i in range(n_value - 1):
            res.append(sigmoid(block[i + 1] - block[i]))
        return np.array([res])


    def get_stock_data_vec(key):
        #pylint: disable=unspecified-encoding
        """[This function gets the stock csv file based on ticker input]

        Args:
            key ([string]): [stock ticker input in lower case like so: amc, tsla]

        Returns:
            [vector]: [vector of each line of csv file that is parsed.]
        """
        vec = []
        path = '/Users/yash/Downloads/'
        lines = open(path+key+".csv","r").read().splitlines()
        for line in lines[1:]:
            #print(float(line.split(",")[4]))
            vec.append(float(line.split(",")[4]))
            #print(vec)
        return vec


    window_size = WINDOW
    episode_count = EPISODE
    window_size = int(window_size)
    episode_count = int(episode_count)
    agent = Agent(window_size)
    data = get_stock_data_vec(STOCK_INPUT)
    line = len(data) - 1
    batch_size = 32
    st.title("Trading Algorithm Magic!")
    for epoch in range(episode_count + 1):
        print ("Episode " + str(epoch) + "/" + str(episode_count))
        st.markdown("Episode " + str(epoch) + "/" + str(episode_count))
        state = get_state(data, 0, window_size + 1)
        total_profit = 0
        agent.inventory = []
        for time_value in range(line):
            action = agent.act(state)
            # sit
            next_state = get_state(data, time_value + 1, window_size + 1)
            reward = 0
            if action == 1: # buy
                agent.inventory.append(data[time_value])
                print("Buy: " + format_price(data[time_value]))
                st.markdown("Buy: " + str(format_price(data[time_value])))
            elif action == 2 and len(agent.inventory) > 0: # sell
                bought_price = agent.inventory.pop(0)
                reward = max(data[time_value] - bought_price, 0)
                total_profit += data[time_value] - bought_price
                print("Sell: " + format_price(data[time_value]) + " | Profit: " + 
                        format_price(data[time_value] - bought_price))
                st.markdown("Sell: " + str(format_price(data[time_value])) + " | Profit: " + str(format_price(data[time_value] - bought_price)))
                if (data[time_value] - bought_price) > 0:
                    st.markdown(f'<p style="background-color:#12AF4A;font-size:18px;border-radius:5%;">{format_price(data[time_value] - bought_price)}</p>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<p style="background-color:#D83916;font-size:18px;border-radius:5%;">{format_price(data[time_value] - bought_price)}</p>', unsafe_allow_html=True)
            done = True if time_value == line - 1 else False
            agent.memory.append((state, action, reward, next_state, done))
            
            
            state = next_state
            if done:
                print("--------------------------------")
                st.markdown("--------------------------------")
                print("Total Profit: " + format_price(total_profit))
                st.markdown("Total Profit: " + str(format_price(total_profit)))
                print("--------------------------------")
                st.markdown("--------------------------------")
            if len(agent.memory) > batch_size:
                agent.exp_replay(batch_size)

if __name__=='__main__':
    main()
    
