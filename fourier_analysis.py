## FOURIER ANALYSIS OF STOCKS, INDIVIDUAL AND INDEX



import math


def fourier_transform(data, return_type ="fft"):
    # Takes in market data and returns a list of constants of the Fourier series
    # Keyword argument:
    #                   return_type : fft for full transform, the same length
    # TODO : FFT
    return_dic = {"fft":0,"cst":1}
    return return_dic[return_type]

def calc_ftt_error(data, fttcst):
    # Just calculate the error between actual data and Fourier series.
    # Return dictionary with info ( absolute/relative error)
    #TODO : everything

    return None

def minimize_error(data, type = "absolute"):

    data_fft_cst = fourier_transform(data)

    err = calc_ftt_error(data, data_fft_cst)

    