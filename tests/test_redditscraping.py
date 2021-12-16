"""Tests for the redditscrapping functions"""
import sys
sys.path.insert(1,'/.../StockNLP/code/')
import unittest
import pandas as pd
from reddit_scraper_module import RedditData as rd

class Testredditscrapping(unittest.TestCase):
    def test_smoke(self):
        """Simple smoke test to make sure function runs"""
        rd.has_numbers('$AMC')
        return

    def test_smoke(self):
        """Simple smoke test to make sure function runs"""
        rd.get_subreddit_column('robinhood', lst = [1,2,3,4,5,6,7,8])
        return

    def test_data_value_passed_is_not_string(self):
        """edge test to make sure the function throws a TypeError when parameter
          value passed to the is not a string type.
        """
        with self.assertRaises(TypeError):
            rd.has_numbers(55)
        return
    def test_smoke(self):
        """Simple smoke test to make sure function runs"""
        rd.add_to_df(tag_values = ["$Foo", "$Bar", "$Foe"], comments = ["FOO", "BAR", "FIE"],date=[1/1/2021,1/2/2021,2/2/2021], df_data=pd.DataFrame(columns=['Tags', 'Comments', 'Date']))
        return
    def test_smoke(self):
        """Simple smoke test to make sure function runs
        """
        rd.has_special_chars("$TSL:A")
        return

    def test_substring_is_string(self):
        """edge test to make sure the function throws a ValueError when the sub_string is not string.
        """
        with self.assertRaises(TypeError):
            rd.__have_special_chars(5)
        return

    def test_substring_is_string(self):
        """edge test to make sure the function throws a ValueError when the input_string is not string.
        """
        with self.assertRaises(TypeError):
            rd.has_special_chars(5)
        return
