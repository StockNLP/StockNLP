"""tests for the master_dash functions"""

import numpy as np
import unittest

from master_dash import get_candlestick_chart
from master_dash import movingaverage
from master_dash import bbands
from master_dash import get_reddit_data
from master_dash import get_senti_trend

class Test_master_dash(unittest.TestCase):
    def test_smoke(self):
        """Simple smoke test to make sure function runs"""
        get_candlestick_chart()
    return

   def test_smoke(self):
       """Simple smoke test to make sure function runs"""
       movingaverage()
   return

   def test_smoke(self):
       """Simple smoke test to make sure function runs"""
       bbands()
   return

   def test_smoke(self):
       """Simple smoke test to make sure function runs"""
       get_reddit_data()
   return

   def test_smoke(self):
       """Simple smoke test to make sure function runs"""
         get_senti_trend()
   return

   def test_to_get_expected_bbands(self):
       """oneshot test to make sure the function returns the expected value"""
       assert np.isclose(bbands(),)
   return

   def test_to_get_expected_master_ticker(self):
       """oneshot test to make sure the function returns the expected value"""
       assert np.isclose(get_subset(),)
   return

   def test_wrong_value_passed_as_the_windows(self):
       """edge test to make sure the function throws a TypeError when windows value
          is not equal to 10"""
       with self.assertRaises(TypeError):                                                                                                                                                movingaverage(interval = , windows = 7)
   return

   def test_wrong_value_passed_as_the_window_size(self):
       """edge test to make sure the function throws a TypeError when windows value
          is not equal to 10"""
       with self.assertRaises(TypeError):
           bbands(price = , window_size = 12, num_of_std=5)
    return

   def test_wrong_value_passed_as_the_num_of_std(self):
       """edge test to make sure the function throws a TypeError when num_of_std value
          is not equal to 5"""
       with self.assertRaises(TypeError):
           bbands(price = , window_size = 10, num_of_std=8)
   return

   def test_wrong_value_passed_as_the_window_size_num_of_std(self):
       """edge test to make sure the function throws a TypeError when windows value
          is not equal to 10 and num_of_std is not equal to 5"""
       with self.assertRaises(TypeError):
           bbands(price = , window_size = 12, num_of_std=4)
   return
