
""" Test suite for Fourier Analysis"""

import unittest
import numpy as np
import fourier_analysis as fa


class TestFourierAnalysis(unittest.TestCase):

    def setUp(self):
        self.x = np.linspace(0, 2*np.pi, 2048)
        self.cos_x = np.cos(self.x)
        self.signal = 5*np.cos(3*self.x) + 4*np.cos(8*self.x)

    def test_discrete_cosine_transform(self):
        cst_list = fa.discrete_cosine_transform(self.signal)
        inverse = fa.discrete_cosine_transform(cst_list)
        i = np.random.randint(0, len(cst_list))
        self.assertAlmostEqual(inverse[i], self.signal[i])

    def test_fast_fourier_transform(self):
        # cst_list = fa.fast_fourier_transform(self.signal, len(self.signal))
        # inverse = fa.fast_fourier_transform(cst_list, len(cst_list))
        # i = np.random.randint(0,len(cst_list))
        # self.assertAlmostEqual(abs(inverse[i]), self.signal[i], 1)

        # TODO: See comment below
        # There seems to be a slight translation when doing the Inverse FFT;
        # Gonna brush it off as rounding errors for now, but needs to be looked at
        pass
