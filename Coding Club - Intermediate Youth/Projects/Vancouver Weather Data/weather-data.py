# Step 1: Setting Up
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("2023_vancouver_data.csv") # sets our CSV data into a Pandas DataFrame

# Step 2: Plotting the Data
data = data[data["Month"] == 1] # filter the data into January
plt.plot(data['Day'], data['Max Temp (°C)'], 'r.')
plt.plot(data['Day'], data['Mean Temp (°C)'], 'g.')
plt.plot(data['Day'], data['Min Temp (°C)'], 'b.')
plt.xlabel("Day")
plt.ylabel("Temperature (\u00b0C)")
plt.title("Temperatures in January 2023")
plt.legend(['Maximum', 'Average', 'Minimum'])

# Step 3: Best Fit Line
from statsmodels.nonparametric.smoothers_lowess import lowess
max_lowess = lowess(data["Max Temp (°C)"], data['Day'], frac=0.25)
mean_lowess = lowess(data["Mean Temp (°C)"], data['Day'], frac=0.25)
min_lowess = lowess(data["Min Temp (°C)"], data['Day'], frac=0.25)
plt.plot(data['Day'], max_lowess[:, 1], 'r-')
plt.plot(data['Day'], mean_lowess[:, 1], 'g-')
plt.plot(data['Day'], min_lowess[:, 1], 'b-')
plt.show()