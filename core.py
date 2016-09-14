# Core of Stock Analysis program.
#

# TODO : see comments


# Locate Data on the web
# Save data to disk
# Load relevant data to program
# Analyze it
# Return relevant information


import matplotlib.pyplot as plt
import fourier_analysis as fa
import data_grabber as dag
import indicators as ind


data = dag.csv_to_list('Data/CSV/Price_Data_Historical_2016-09-03_17-38.csv')
moving_average = ind.moving_average(data,30)

print(data)

cst_list = fa.discrete_fourier_transform(data, return_type="cst")
print(cst_list)

inverse_desc = fa.inverse_fourier_transform(cst_list,40,len(data),order_type="descending")
inverse_norm = fa.inverse_fourier_transform(cst_list,40,len(data),order_type="normal")

plt.plot(inverse_desc)
plt.plot(inverse_norm)
plt.plot(data)
plt.plot(moving_average)
plt.show()