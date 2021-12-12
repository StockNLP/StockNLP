"""Tests for the redditscrapping functions"""

import numpy as np
import unittest

from reddit_scraper_module import has_numbers
from reddit_scraper_module import get_subreddit_column
from reddit_scraper_module import cashtags 
from reddit_scraper_module import add_to_df
from reddit_scraper_module import has_special_chars
from reddit_scraper_module import have_special_chars

class Testredditscrapping(unittest.TestCase):

    def test_smoke(self):
        """Simple smoke test to make sure function runs"""
        has_numbers('$AMC')
        return

    def test_smoke(self):
        """Simple smoke test to make sure function runs"""
        get_subreddit_column(robinhood, )
    return

    def test_smoke(self):
        """Simple smoke test to make sure function runs"""
        cashtags(, )
    return

    def test_data_value_passed_is_not_string(self):
       """edge test to make sure the function throws a TypeError when parameter
          value passed to the is not a string type."""
       with self.assertRaises(TypeError):
           has_numbers(55)
    return

    def test_smoke(self):
        """Simple smoke test to make sure function runs"""
        add_to_df(, )
     return

    def test_smoke(self):
        """Simple smoke test to make sure function runs"""
        has_special_chars(, )
    return

   def test_smoke(self):
       """Simple smoke test to make sure fucntion runs"""
       have_special_chars(, )
   return

   def test_check_return_value_of_have_special_chars_is_bool_type(self):
        """test to make sure the returned value of the have_special_chars function is boolean type."""
       self.assertIsInstance(have_special_chars(), bool)
    return
        
   def test_substring_is_string(self):
       """edge test to make sure the function throws a ValueError when the sub_string is not string."""
        with self.assertRaises(ValueError):
            have_special_chars(5)
   return

   def test_substring_is_string(self):
       """edge test to make sure the function throws a ValueError when the input_string is not string."""
       with self.assertRaises(ValueError):
            has_special_chars(5)
   return

   def test_check_return_value_of_has_special_chars_is_uppercase(self):
       """edge test to make sure the returned value of the has_special_chars is uppercase."""
       self.assertIsInstance(has_special_chars(), has_special_chars().upper())
   return
