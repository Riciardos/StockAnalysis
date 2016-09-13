## FOURIER ANALYSIS OF STOCKS, INDIVIDUAL AND INDEX


import numpy as np


def discrete_fourier_transform(data, return_type ="dft"):
    # Takes in market data and returns a list of constants of the Fourier series
    # Keyword argument:
    #                   return_type : dft for full transform, the same length
    #                                 cst for constants
    # TODO : DFT

    data_length = len(data)
    f_k = np.zeros_like(data)
    for k in range(0,data_length):
        fsum = 0
        omega = 2*k*np.pi/data_length
        for n in range(0,data_length):
            fsum += data[n]*np.cos(n*omega)
        f_k[k] = fsum

    type_dic = {"dft":0,"cst":1}
    return_dic = [0,f_k]
    return return_dic[type_dic[return_type]]


def calc_ft_error(data, ftcst, return_type ="abs"):
    # Just calculate the error between actual data and Fourier series.
    # Return dictionary with info ( absolute/relative error)
    # TODO : everything

    return_dic = {"abs":0,"rel":1}
    return return_dic[return_type]


def minimize_error(data, type = "absolute"):

    data_fft_cst = fourier_transform(data)

    err = calc_ftt_error(data, data_fft_cst)
