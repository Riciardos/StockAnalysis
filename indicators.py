# Technical indicator functions.
import numpy as np
import logging
from utils import RSILL


def moving_average(data, period):

    ma_array = np.zeros_like(data)
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
    # Need multiple stages
    # First stage: fill average up and average down
    # Second stage: calculate

    assert period > 0, logging.debug('Period needs to be positive.')

    counter, up_array, down_array = rsi_fill(data, period)

    return rsi_proc(data, counter, up_array, down_array)


def rsi_fill(data, period):
    up_array = RSILL(period)
    down_array = RSILL(period)
    counter = 0

    while up_array.is_full() is False and down_array.is_full() is False:
        if counter > len(data):
            raise RuntimeError('Ran out of data before RSI could be started')
        if data[counter] < data[counter+1]:
            up_array.add_node(data[counter+1] - data[counter])

        else:
            down_array.add_node(data[counter] - data[counter+1])

        counter += 1

    return counter, up_array, down_array


def rsi_proc(data, counter, up_array, down_array):

    rsi_array = np.zeros(len(data) - counter)
    logging.debug("Counter is %i", counter)
    for i in range(counter, len(rsi_array)-1):
        if data[i] < data[i+1]:
            up_array.add_node(data[i+1] - data[i])
        else:
            down_array.add_node(data[i] - data[i+1])

        rsi_array[i] = 100 - (100/(1 + (up_array.average()/down_array.average())))

    return rsi_array
