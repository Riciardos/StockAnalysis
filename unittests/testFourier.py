
""" Test suite for Fourier Analysis"""

import unittest
import numpy as np
import fourier_analysis as fa


class TestFourierAnalysis(unittest.TestCase):

    def setUp(self):
        self.x = np.linspace(-np.pi, np.pi, 1024)
        self.cos_x = np.cos(self.x)
        self.signal = 5*np.cos(3*self.x) + 4*np.cos(8*self.x)

    def test_discrete_cosine_transform(self):
        cst_list = fa.discrete_cosine_transform(self.cos_x)
        inverse = fa.discrete_cosine_transform(cst_list)
        i = np.random.randint(0, len(cst_list))
        self.assertAlmostEqual(inverse[i], self.cos_x[i])

    def test_find_frequencies(self):
        pass
