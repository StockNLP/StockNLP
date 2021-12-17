"""tests for the master_dashboard functions"""

import numpy as np
import pandas as pd
import unittest
from .master_dashboard import movingaverage
from .master_dashboard import get_senti_trend
from .master_dashboard import Agent as ag

class Test_master_dash(unittest.TestCase):

    def test_smoke(self):
        """Simple smoke test to make sure function runs"""
        movingaverage([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], window_size=10)
        return

    def test_smoke_1(self):
        """Simple smoke test to make sure function runs"""
        get_senti_trend(pd.read_csv('./subs.csv'))
        return

    def test_smoke_2(self):
        """Simple smoke test to make sure function runs"""
        ag.formatPrice(2.156)
        return

    def test_smoke_3(self):
        """Simple smoke test to make sure function runs"""
        ag.sigmoid(3.68)
        return

    def test_to_get_expected_sigmoid_value(self):
        """oneshot test to make sure the function returns the expected value"""
        assert np.isclose(ag.sigmoid(3.68),0.97539)
        return

    def test_to_get_expected_formatprice(self):
        """oneshot test to make sure the function returns the expected value"""
        assert np.isclose(ag.formatPrice(2.156), '$2.15')
        return

    def test_check_return_value_of_sigmoid_is_float_type(self):
        """test to make sure the returned value of the sigmoid function is float type."""
        self.assertIsInstance(ag.sigmoid(3.68), float)
        return