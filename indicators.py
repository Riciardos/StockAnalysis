### Technical indicator functions.
import numpy as np

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


def rsi(data,period):

    # TODO : fix fast algorithm for circular lists (pop first element and add one to the end)
    
    rsi_array = np.zeros(data)
    sum_up = 0
    sum_down = 0

    for i in range(0,len(data)-1):
        if data[i] <= data[i+1]:
            sum_up += data[i+1] - data[i]

        else:
            sum_down += data[i+1] -data[i]
        average_up = sum_up/period
        average_down = sum_down/period

        rsi_array[i] = 100 - (100/(1+ (average_up/average_down)))