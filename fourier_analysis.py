"""Fourier Analysis module, anything with frequencies goes in here."""

import numpy as np
import logging


def discrete_cosine_transform(data):
    """Takes in market data and returns a list of constants of the Direct Cosine series.
    Uses the DCT-IV algorithm so the same function can be used to calculate the inverse.
    Note: is very slow, use only for small data sets. Use fast_fourier_transform for larger ones"""

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
    simulated_data = fast_fourier_transform(ftcst, len(ftcst))
    diff_sum = 0
    is_normalized = norm_check(data, simulated_data)

    if not is_normalized:
        logging.debug("FFT constants returned non normalized simulated data, thread with care.")
        norm = find_norm(data, simulated_data)
        for i in range(0,len(simulated_data)):
            simulated_data[i] *= norm

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


def fast_fourier_transform(data, n):
    """Fast Fourier Transform, a recursive DFT function that uses the Cooley-Tukey algorithm.
    n is the length of the data, needed for normalization; is assummed to be power of 2."""
    data = np.asarray(data, dtype='complex')
    data_length = data.shape[0]

    if data_length == 1:
        return data/np.sqrt(n)  # 1/sqrt(n) constant is chosen so the same function can be used to calculate inverse

    else:
        data_even = fast_fourier_transform(data[::2], n)
        data_odd = fast_fourier_transform(data[1::2], n)
        factor = np.exp(-2j*np.pi*np.arange(data_length)/data_length)
        return np.concatenate([data_even + factor[:data_length//2]*data_odd,
                              data_even - factor[:data_length//2]*data_odd])


def norm_check(data, simulated_data, error_margin = 0.01):
    """"norm_check checks if two data sets are of the same size,
    and checks if maximum values are within a error margin. Default error margin is 1%."""

    if len(data) != len(simulated_data):
        logging.debug("Length of data sets not the same")
        return False
    elif abs(1 - (max(simulated_data)/max(data))) > error_margin:
        logging.debug("Maximum values of arrays not within error_margin.")
        return False
    else:
        return True


def find_norm(data, sdata):
    """Find_norm goes over every data point of two sets, finds the ratio, and returns the average.
       Assumes data and sdata share the same length."""

    average_sum = 0

    for i in range(0, len(data)):
        average_sum += data[i]/sdata[i]

    return average_sum/len(data)
