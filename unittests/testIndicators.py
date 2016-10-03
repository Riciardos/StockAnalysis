
# TODO : Everything

"""Test suite for indicators.py"""

import unittest
import logging
import data_grabber as dag
import indicators as ind
import numpy as np


class TestIndicators(unittest.TestCase):

    def setUp(self):
        datagrabber = dag.DataGrabber()
        self.real_data = datagrabber.csv_to_numpy_array('Data/CSV/Price_Data_Historical_2016-09-03_17-38.csv')

    def test_moving_average_constant(self):
        x = np.ones(len(self.real_data))
        moving_average = ind.moving_average(self.real_data, 14)

    def test_rsi_period(self):
        with self.assertRaises(AssertionError):
            ind.rsi(self.real_data, -2)


if __name__ == '__main__':
    unittest.main()