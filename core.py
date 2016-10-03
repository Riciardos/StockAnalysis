# Core of Stock Analysis program.
#

# TODO : see comments


# Locate Data on the web
# Save data to disk
# Load relevant data to program
# Analyze it
# Return relevant information

import numpy as np
import matplotlib.pyplot as plt
import fourier_analysis as fa
import data_grabber as dag
import indicators as ind

datagrabber = dag.DataGrabber()
data = datagrabber.csv_to_numpy_array('Data/CSV/Price_Data_Historical_2016-09-03_17-38.csv')
moving_average = ind.moving_average(data, 14)

x = np.linspace(0, np.pi, 128)
cos_x = 2*np.cos(3*x) + np.cos(15*x)
cst_list = fa.discrete_cosine_transform(cos_x)
inverse = fa.discrete_cosine_transform(cst_list)


# inverse_desc = fa.inverse_fourier_transform(cst_list, len(cst_list), len(cos_x), order_type="descending")
# inverse_norm = fa.inverse_fourier_transform(cst_list, len(cst_list), len(cos_x), order_type="normal")

# rsi = ind.rsi(data, -14)
# plt.plot(data)
# plt.plot(rsi)
# plt.plot(inverse_desc)
# plt.plot(inverse_norm)
plt.plot(cos_x)
plt.plot(cst_list**2)
plt.plot(inverse)
# plt.plot(moving_average)
plt.show()
