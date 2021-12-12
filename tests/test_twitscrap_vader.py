"""tests for the twitterscraping and vader function"""

import numpy as np
import unittest

from twitter_class import add_to_df
from twitter_class import tick_list
from twitter_class import get_like_retweet_lst
from twitter_class import preprocessing
from twitter_class import vaderScoreGenerator
from twitter_class import appendToMaster
from twitter_class import get_score
from twitter_class import get_subset

class Test_twitter_scrapping_vader(unittest.TestCase):
       def test_smoke(self):
           """Simple smoke test to make sure function runs"""
           add_to_df()
       return

       def test_smoke(self):
       """Simple smoke test to make sure function runs"""
         tick_list()
       return

       def test_smoke(self):
           """Simple smoke test to make sure function runs"""
           get_like_retweet_lst()
       return

       def test_smoke(self):
           """Simple smoke test to make sure function runs"""
           preprocessing()
       return

      def test_smoke(self):
          """Simple smoke test to make sure function runs"""
          vaderScoreGenerator()
      return

      def test_smoke(self):
          """Simple smoke test to make sure function runs"""
          appendToMaster()
      return

      def test_smoke(self):
          """Simple smoke test to make sure function runs"""
          get_score()
      return

     def test_smoke(self):
         """Simple smoke test to make sure function runs"""
         get_subset()
     return

     def test_to_get_expected_vader_score(self):
         """oneshot test to make sure the function returns the expected value"""
         assert np.isclose(get_score(),)
     return

     def test_to_get_expected_master_ticker(self):
         """oneshot test to make sure the function returns the expected value"""
         assert np.isclose(get_subset(),)
     return

   def test_no_value_passed_to_the_function(self):
       """edge test to make sure the function throws a TypeError when all the parameters
          are not passed to the function."""
       with self.assertRaises(TypeError):
           add_to_df(lst = , tck = , src = , date = ,like_count = , retweet_count = )
   return

    def test_value_passed_outside_the_parameter_list(self):
        """edge test to make sure the function throws a TypeError when tick value passed is
         outside the following parameters: '$AMC','$GMC','$TSLA','$MSFT','$AAPL','$DOGE','$SHIB',
         '$ETH','$PROG','$BTC','$ADA','$NKLA','$GOOGL','$RIVN','$FB'."""
        with self.assertRaises(TypeError):
            add_to_df(lst = , df = , tck ='$APPL' , src = , date = , like_count = , retweet_count = )
    return
