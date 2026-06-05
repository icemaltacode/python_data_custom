"""
Sorting by index values
=======================

Previously, you changed the order of the rows in a DataFrame by calling .sort_values(). 
It's also useful to be able to sort by elements in the index. For this, you need to use .sort_index().

pandas is loaded as pd. temperatures_ind has a multi-level index of country and city, and is available.
"""

# region setup
import pandas as pd
temperatures = pd.read_csv('Module 8/data/temperatures.csv', index_col=0)
temperatures_ind = temperatures.set_index(["country", "city"])
# endregion

## ---- START HERE ----

# Sort temperatures_ind by index values
print(____)

# Sort temperatures_ind by index values at the city level
print(____)

# Sort temperatures_ind by country then descending city
print(____)
