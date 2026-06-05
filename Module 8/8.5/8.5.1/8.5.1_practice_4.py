"""
Price of conventional vs. organic avocados
==========================================

Creating multiple plots for different subsets of data allows you to compare groups. 
In this exercise, you'll create multiple histograms to compare the prices of 
conventional and organic avocados.

matplotlib.pyplot has been imported as plt and pandas has been imported as pd.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt
avocados = pd.read_pickle('Module 8/data/avoplotto.pkl')
# endregion

## ---- START HERE ----

# Subset avocados for the "conventional" type and create a histogram of the avg_price column.
avocados[____][____].____

# Create a histogram of avg_price for "organic" type avocados.
avocados[____][____].____

# Add a legend to your plot, with the names "conventional" and "organic".
plt.legend(____)

# Show your plot
____

# Modify your code to adjust the transparency of both histograms to 0.5 
# to see how much overlap there is between the two distributions.
avocados[____][____].____

# Modify histogram transparency to 0.5
avocados[____][____].____

# Show the updated plot
plt.show()

# Modify your code to use 20 bins in both histograms.
avocados[____][____].____

# Modify bins to 20
avocados[____][____].____

# Show the updated plot
plt.show()