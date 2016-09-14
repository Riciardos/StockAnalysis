## FOURIER ANALYSIS OF STOCKS, INDIVIDUAL AND INDEX


import numpy as np


def discrete_fourier_transform(data, return_type ="cst"):
    # Takes in market data and returns a list of constants of the Fourier series
    # Keyword argument:
    #                   return_type : dft for full transform, the same length
    #                                 cst for constants
    # TODO : integrate inverse dft

    data_length = len(data)
    f_k = np.zeros(data_length//2)
    f_l = np.zeros(data_length//2)
    f_const = 2/data_length
    for k in range(0,data_length//2):
        fksum = 0
        flsum = 0
        omega = f_const*k*np.pi
        for n in range(0,data_length):
            fksum += data[n]*np.cos(n*omega)
            flsum += data[n]*np.sin(n*omega)
        f_k[k] = f_const*fksum
        f_l[k] = f_const*flsum

    type_dic = {"dft":0,"cst":[f_k,f_l]}

    return type_dic[return_type]


def calc_ft_error(data, ftcst, return_type ="abs"):
    # Just calculate the error between actual data and Fourier series.
    # Return dictionary with info ( absolute/relative error)
    # TODO : everything

    return_dic = {"abs":0,"rel":1}
    return return_dic[return_type]


def minimize_error(data, type = "absolute"):

    data_fft_cst = fourier_transform(data)

    err = calc_ftt_error(data, data_fft_cst)


def inverse_fourier_transform(cst_list, num_of_terms = 10, data_length = 128, order_type = "normal"):
    # Takes in numpy array of Fourier Transform constants
    # Needs number of terms, number of data points it needs to map to and the order type:
    # Normal is counting from term zero upwards, "Largest" sorts the terms from largest to smallest

    assert num_of_terms < len(cst_list[0]) , "Number of terms exceeds number of constants"
    a_n = cst_list[0]
    b_n = cst_list[1]

    if order_type == "descending":
        a_n = np.sort(a_n)[::-1]
        b_n = np.sort(b_n)[::-1]

    data = np.zeros(data_length)
    omega = 2*np.pi/data_length
    for i in range(0,data_length):
        for n in range(0,num_of_terms):
            data[i] += 0.5*(a_n[n]*np.cos(n*omega*i) + b_n[n]*np.sin(n*omega*i))

    return data