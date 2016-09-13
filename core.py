# Core of Stock Analysis program.
#

""""TO DO LIST"""


# Locate Data on the web
# Save data to disk
# Load relevant data to program
# Analyze it
# Return relevant information


import matplotlib.pyplot as plt
import fourier_analysis as fa
import data_grabber as dag

data = dag.csv_to_list('Data/CSV/Price_Data_Historical_2016-09-03_17-38.csv')
data = data[4:]
data_points = []
for i in range(0,len(data)):
    data_points.append(float(data[i][3]))

print(data_points)

cst_list = fa.discrete_fourier_transform(data_points, return_type="cst")
print(cst_list)

plt.plot(data_points)
plt.show()
plt.plot(cst_list)
plt.show()
