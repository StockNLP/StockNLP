
import pandas as pd
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

var = 0.5

#df = pd.read_csv('Reddit_Test.csv')

sia = SentimentIntensityAnalyzer()  
class vaderReddit():
    def __init__(self) -> None:
        pass
     
    @staticmethod
    def add_vader_scores(df):
        df['Negative'] = df['Comment'].apply(lambda x:sia.polarity_scores(str(x))['neg'])
        df['Neutral'] = df['Comment'].apply(lambda x:sia.polarity_scores(str(x))['neu'])
        df['Positive'] = df['Comment'].apply(lambda x:sia.polarity_scores(str(x))['pos'])
        df['Compound'] = df['Comment'].apply(lambda x:sia.polarity_scores(str(x))['compound'])

    
    
    @staticmethod
    def add_vader_weighted_sentiments(df):
        df['Weighted_Sentiment_Neg'] = df.apply(lambda row: (row['Negative']*row['Compound']
                                                            if row['Compound'] > 0 or row['Compound'] < 0
                                                            else row['Negative'] * var 
                                                        ), axis=1)
        df['Weighted_Sentiment_Neu'] = df.apply(lambda row: (row['Neutral']*row['Compound']
                                                            if row['Compound'] > 0 or row['Compound'] < 0
                                                            else row['Neutral'] * var 
                                                        ), axis=1)
        df['Weighted_Sentiment_Pos'] = df.apply(lambda row: (row['Positive']*row['Compound']
                                                            if row['Compound'] > 0 or row['Compound'] < 0
                                                            else row['Positive'] * var 
                                                        ), axis=1)

        df['Sum_Weights'] = df.apply(lambda row: (row['Weighted_Sentiment_Neg'] + row['Weighted_Sentiment_Neu']
                                                + row['Weighted_Sentiment_Pos']), axis=1)

    @staticmethod
    def get_subset(stock_name, df):
        df_sub = df.loc[df['Tags'] == stock_name]
        return df_sub

    @staticmethod
    def get_score(df_sub):
        df_grp = df_sub.groupby('Date')['Sum_Weights'].aggregate(['sum','count'])
        df_grp['Sentiment_Score'] = df_grp.apply(lambda x: (x['sum']/x['count']), axis=1)
        return df_grp