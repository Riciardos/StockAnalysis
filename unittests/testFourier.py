
# TODO : EVERYTHING

""" Test suite for Fourier Analysis"""

import unittest
import numpy as np
import fourier_analysis as fa


class TestFourierAnalysis(unittest.TestCase):

    def setUp(self):
        self.x = np.linspace(-np.pi, np.pi, 201)
        self.sin_x = np.sin(x)

    def test_discrete_fourier_transform(self):
        constant = [1.0]
        self.assertEqual()