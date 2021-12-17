"""tests for the vader score of reddit scrapping functions"""

import numpy as np
from pandas._testing import assert_frame_equal
import pandas as pd
import unittest

from vader_working_file import VaderReddit as vd
df = pd.DataFrame({'Date': [11/30/2021], 'Tags': ['$AMC'], 'Comment': ['The one time I buy $AMC it just pissed my money away']})

class Test_vader_reddit_score(unittest.TestCase):
    def test_smoke(self):
        """Simple smoke test to make sure function runs"""
        vd.add_vader_scores(df)
        return
     
    def test_smoke(self):
        """Simple smoke test to make sure function runs"""
        vd.add_vader_weighted_sentiments(df)
        return

    def test_smoke(self):
        """Simple smoke test to make sure function runs"""
        df_1 = vd.get_subset('$AMC',df)
        return df_1

    def test_smoke(self):
        """Simple smoke test to make sure function runs"""
        df_1 = vd.get_subset('$AMC',df)
        vd.get_score(df_1)
        return

    def test_dataframe_equal(self):
        """edge test to make sure dataframe is as expected"""
        assert_frame_equal(vd.add_vader_scores(df), pd.DataFrame({
           'Comment': ['The one time I buy $AMC it just pissed my money away'],
           'Date': [11/30/2021], 'Subreddit': ['wallstreetbets'], 'Tags': ['$AMC'],
           'Negative': [0.296], 'Neutral': {0.704}, 'Positive': [0], 'Compound': [-0.6369]}))
        return

    def test_dataframe_equal(self):
        """edge test to make sure dataframe is as expected"""
        assert_frame_equal(vd.add_vader_weighted_sentiments(df), pd.DataFrame({
                                          ' Comment': 
                                          ['The one time I buy $AMC it just pissed my money away'], 
                                          'Date': [11/30/2021],
                                           'Subreddit': ['wallstreetbets'],
                                           'Tags': ['$AMC'], 'Negative': [0.296],
                                            'Neutral': {0.704}, 'Positive': [0],
                                            'Compound': [-0.6369], Weighted_Sentiment_Neg:
                                            [-0.1885224], Weighted_Sentiment_Neu:
                                            [-0.4483776], Weighted_Sentiment_Pos: [0],
                                            Sum_Weights: [-0.6369]}))
        return

    def test_dataframe_equal(self):
        """edge test to make sure dataframe is as expected"""
        assert_frame_equal(vd.get_subset('$AMC',df), pd.DataFrame({
                                          'Comment': ['The one time I buy $AMC it just pissed my money away'], 'Date': [11/30/2021],
                                          'Subreddit': ['wallstreetbets'],'Tags': ['$AMC'], Negative: [0.296],
                                          Neutral: {0.704}, Positive: [0], Compound: [-0.6369], Weighted_Sentiment_Neg:
                                          [-0.1885224], Weighted_Sentiment_Neu:[-0.4483776], Weighted_Sentiment_Pos: [0],
                                          Sum_Weights: [-0.6369]})
        return

    def test_dataframe_equal(self):
        """edge test to make sure dataframe is as expected"""
        assert_frame_equal(vd.get_score(df1), pd.DataFrame({'Date': [11/30/2021], 'sum': [0.3612], 'count': [1], 'Sentiment_Score': [0.3612]})
        return

    def test_no_value_passed_to_the_function(self):
        """edge test to make sure the function throws a TypeError when all the parameters
           are not passed to the function."""
        with self.assertRaises(TypeError):
            vd.get_subset(stock_name ='$AMC')
        return

     def test_no_value_passed_to_the_function(self):
         """edge test to make sure the function throws a TypeError when all the parameters
            are not passed to the function."""
          with self.assertRaises(TypeError):
              vd.get_subset(df)
          return

      def test_value_passed_outside_the_parameter_list(self):
          """edge test to make sure the function throws a TypeError when stock_name passed is
             not string type"""
           with self.assertRaises(TypeError):
               vd.get_subset(stock_name = 55, df)
           return

   def test_value_passed_outside_the_parameter_list(self):
       """edge test to make sure the function throws a TypeError when stock_name passed is
          not in the list of stock names"""
        with self.assertRaises(TypeError):
            vd.get_subset(stock_name = '$HHY', df)
        return

