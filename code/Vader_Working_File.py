"""
Temp docstring
"""
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import nltk

nltk.download('vader_lexicon')

VAR = 0.5

#d_f = pd.read_csv('Reddit_Test.csv')

sia = SentimentIntensityAnalyzer()
class VaderReddit():
    """
    temp docstring
    """
    def __init__(self) -> None:
        pass

    @staticmethod
    def add_vader_scores(d_f):
        """
        temp docstring
        """
        d_f['Negative'] = d_f['Comment'].apply(lambda x:sia.polarity_scores(str(x))['neg'])
        d_f['Neutral'] = d_f['Comment'].apply(lambda x:sia.polarity_scores(str(x))['neu'])
        d_f['Positive'] = d_f['Comment'].apply(lambda x:sia.polarity_scores(str(x))['pos'])
        d_f['Compound'] = d_f['Comment'].apply(lambda x:sia.polarity_scores(str(x))['compound'])



    @staticmethod
    def add_vader_weighted_sentiments(d_f):
        """
        temp docstring
        """
        d_f['Weighted_Sentiment_Neg'] = d_f.apply(lambda row: (row['Negative']*row['Compound']
                                                            if row['Compound'] > 0 or row['Compound'] < 0
                                                            else row['Negative'] * VAR
                                                        ), axis=1)
        d_f['Weighted_Sentiment_Neu'] = d_f.apply(lambda row: (row['Neutral']*row['Compound']
                                                            if row['Compound'] > 0 or row['Compound'] < 0
                                                            else row['Neutral'] * VAR
                                                        ), axis=1)
        d_f['Weighted_Sentiment_Pos'] = d_f.apply(lambda row: (row['Positive']*row['Compound']
                                                            if row['Compound'] > 0 or row['Compound'] < 0
                                                            else row['Positive'] * VAR
                                                        ), axis=1)

        d_f['Sum_Weights'] = d_f.apply(lambda row: (row['Weighted_Sentiment_Neg'] + row['Weighted_Sentiment_Neu']
                                                + row['Weighted_Sentiment_Pos']), axis=1)

    @staticmethod
    def get_subset(stock_name, d_f):
        """
        temp docstring
        """
        d_f_sub = d_f.loc[d_f['Tags'] == stock_name]
        return d_f_sub

    @staticmethod
    def get_score(d_f_sub):
        """
        temp docstring
        """
        d_f_grp = d_f_sub.groupby('Date')['Sum_Weights'].aggregate(['sum','count'])
        d_f_grp['Sentiment_Score'] = d_f_grp.apply(lambda x: (x['sum']/x['count']), axis=1)
        return d_f_grp
