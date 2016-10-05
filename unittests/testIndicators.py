
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

    def test_known_set(self):
        moving_average = ind.moving_average(self.real_data, 14)
        self.assertAlmostEqual(moving_average[15],413.31428571)

    def test_moving_average_constant(self):
        x = np.ones(len(self.real_data))
        moving_average = ind.moving_average(x, 14)
        self.assertEqual(1.0, moving_average[20])

    def test_rsi_period(self):
        with self.assertRaises(AssertionError):
            ind.rsi(self.real_data, -2)


if __name__ == '__main__':
    unittest.main()