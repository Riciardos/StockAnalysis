# Technical indicator functions.
import numpy as np
import logging


def moving_average(data, period):

    ma_array = np.zeros(len(data))
    sum = 0
    for j in range(0,period):
        sum += data[j]
        ma_array[j] = data[j]
    for i in range(period, len(data)):
        ma_array[i] = sum/period
        sum -= data[i - period]
        sum += data[i]

    return ma_array


def rsi(data, period):

    # TODO : Still needs to fix this completely
    assert period > 0, logging.debug("Period needs to be positive.")

    rsi_array = np.zeros_like(data)
    sum_up = 0
    sum_down = 0
    counter_up = 0
    counter_down = 0
    average_up = 1
    average_down = 1

    for i in range(period,len(data)-1):

        if data[i] <= data[i+1]:
            sum_up += data[i+1] - data[i] - (data[i - period + 1] - data[i - period])
            average_up = sum_up / period

        else:
            sum_down += data[i+1] - data[i] - (data[i - period + 1] - data[i - period])
            average_down = sum_down/period

        rsi_array[i] = 100 - (100/(1 + (average_up/average_down)))

    return rsi_array

