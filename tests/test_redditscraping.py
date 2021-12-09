"""Tests for the stocknlp function"""

import numpy as np
import unittest

from redditscraping_copy import has_numbers
from redditscraping_copy import flatten_list

class Testredditscrapping(unittest.TestCase):

    def test_smoke(self):
        """Simple smoke test to make sure function runs"""
        has_numbers('$AMC')
        return
#    def test_smoke(self):
#       """Simple smoke test to make sure function runs"""
#        get_subreddit_column(robinhood, )
#       return
#    def test_smoke(self):
#        """Simple smoke test to make sure function runs"""
#       cashtags(, )
#        return
    def test_smoke(self):
       """Simple smoke test to make sure function runs"""
       flatten_list(['$AMC'],['$AMC is going up'],[2/1/1999])
       return
    def test_data_value_passed_is_not_string(self):
       """test to make sure the function throws a TypeError when parameter value passed to the is not a string type."""
       with self.assertRaises(TypeError):
           has_numbers(55)
       return
#    def test_smoke(self):
#       """Simple smoke test to make sure function runs"""
#        add_to_df(, )
#       return
#    def test_smoke(self):
#       """Simple smoke test to make sure function runs"""
#       has_special_chars(, )
#        return
#   def test_smoke(self):
#      """Simple smoke test to make sure fucntion runs"""
        

