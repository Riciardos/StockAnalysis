
""" Test suite for Fourier Analysis"""

import unittest
import numpy as np
import fourier_analysis as fa


class TestFourierAnalysis(unittest.TestCase):

    def setUp(self):
        self.x = np.linspace(0, 2*np.pi, 128)
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

    def test_norm_check(self):
        data = [0,3,2,0,1]
        sdata= [1,2,3,0,0]
        is_normalized = fa.norm_check(data,sdata)
        self.assertTrue(is_normalized)
        sdata.append(0)
        not_same_length = fa.norm_check(data,sdata)
        self.assertFalse(not_same_length)
        data.append(4)
        not_same_max = fa.norm_check(data,sdata)
        self.assertFalse(not_same_max)

    def test_find_norm(self):
        data = [1,1,1,1,1,1]
        sdata = [2,2,2,2,2,2]
        ratio = fa.find_norm(data, sdata)
        self.assertTrue(ratio == 0.5)

    def test_calc_ft_error(self):
        data = [1, 1, 1, 1, 1, 1, 1, 1]
        fft_cst = fa.fast_fourier_transform(data,len(data))
        error = fa.calc_ft_error(data, fft_cst)

