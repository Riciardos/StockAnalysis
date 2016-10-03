"""Fourier Analysis module, anything with frequencies goes in here."""

import numpy as np
import logging


def discrete_cosine_transform(data):
    """Takes in market data and returns a list of constants of the Direct Cosine series.
    Uses the DCT-IV algorithm so the same function can be used to calculate the inverse."""

    data_length = len(data)
    f_k = np.zeros(data_length)
    f_const = np.sqrt(2/data_length)
    for k in range(0, data_length):
        fksum = 0
        omega = (np.pi/data_length)*(k + 0.5)
        for n in range(0, data_length):
            fksum += data[n]*np.cos((n + 0.5)*omega)
        f_k[k] = f_const*fksum

    return f_k


def calc_ft_error(data, ftcst, return_type ='abs'):
    # Just calculate the error between actual data and Fourier series constructed from list of constants
    # Return dictionary with info ( absolute/relative error)
    simulated_data = inverse_fourier_transform(ftcst, len(ftcst), len(data))
    diff_sum = 0

    if return_type == 'abs':
        for i in range(0, len(data)):
            diff_sum += abs(data[i] - simulated_data[i])

    if return_type == 'rel':
        for i in range(0, len(data)):
            diff_sum += abs(data[i] - simulated_data[i])/data[i]
    else:
        logging.debug('No proper type given in error calculation')

    return diff_sum


def minimize_error(data, margin, type = 'rel',):
    # TODO : find usage for this; some machine learning algorithm probably
    data_fft_cst = discrete_cosine_transform(data)

    err = calc_ft_error(data, data_fft_cst)


def inverse_fourier_transform(cst_list, num_of_terms = 10, data_length = 128, order_type = "normal"):
    # Takes in numpy array of Fourier Transform constants
    # Needs number of terms, number of data points it needs to map to and the order type:
    # Normal is counting from term zero upwards, "descending" sorts the terms from largest to smallest
    # TODO : Don't use this, use discrete_cosine_transform for now

    assert num_of_terms < len(cst_list[0]), logging.debug("Number of terms exceeds number of constants")
    a_n = cst_list[0]
    b_n = cst_list[1]

    if order_type == "descending":
        a_n = np.sort(a_n)[::-1]
        b_n = np.sort(b_n)[::-1]

    data = np.zeros(data_length)
    omega = 2*np.pi/data_length
    for i in range(0,data_length):
        for n in range(0,num_of_terms):
            data[i] += (a_n[n]*np.cos(n*omega*i) + b_n[n]*np.sin(n*omega*i))

    return data
