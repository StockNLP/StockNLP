"""tests for the vader score of reddit scrapping functions"""

import numpy as np
from pandas._testing import assert_frame_equal
import pandas as pd
import unittest

from vader_reddit import add_vader_scores
from vader_reddit import add_vader_weighted_sentiments
from vader_reddit import get_subset
from vader_reddit import get_score

class Test_vader_reddit_score(unittest.TestCase):
      def test_smoke(self):
          """Simple smoke test to make sure function runs"""
          add_vader_scores()
     return
     
     def test_smoke(self):
         """Simple smoke test to make sure function runs"""
         add_vader_weighted_sentiments()
     return

     def test_smoke(self):
        """Simple smoke test to make sure function runs"""
        get_subset(,)
     return

    def test_smoke(self):
        """Simple smoke test to make sure function runs"""
        get_score()
    return

    def test_dataframe_equal(self):
       """edge test to make sure dataframe is as expected"""
       pandas.testing.assert_frame_equal(add_vader_scores(), )
    return

    def test_dataframe_equal(self):
        """edge test to make sure dataframe is as expected"""
        pandas.testing.assert_frame_equal(add_vader_weighted_sentiments(), )
    return

    def test_dataframe_equal(self):
        """edge test to make sure dataframe is as expected"""
        pandas.testing.assert_frame_equal(get_subset(), )
    return

    def test_dataframe_equal(self):
        """edge test to make sure dataframe is as expected"""
        pandas.testing.assert_frame_equal(get_score(), )
    return

    def test_no_value_passed_to_the_function(self):
        """edge test to make sure the function throws a TypeError when all the parameters
           are not passed to the function."""
        with self.assertRaises(TypeError):
            get_subset(stock_name = )
     return

     def test_no_value_passed_to_the_function(self):
         """edge test to make sure the function throws a TypeError when all the parameters
            are not passed to the function."""
          with self.assertRaises(TypeError):
              get_subset(df = )
      return

      def test_value_passed_outside_the_parameter_list(self):
          """edge test to make sure the function throws a TypeError when stock_name passed is
             not string type"""
           with self.assertRaises(TypeError):
               get_subset(stock_name = 55, df = )
       return

   def test_value_passed_outside_the_parameter_list(self):
       """edge test to make sure the function throws a TypeError when stock_name passed is
          not in the list of stock names"""
        with self.assertRaises(TypeError):
            get_subset(stock_name = '$HHY', df = )
    return

