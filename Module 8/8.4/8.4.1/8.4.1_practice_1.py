"""
Setting and removing indexes
============================

pandas allows you to designate columns as an index. This enables cleaner code when taking subsets 
(as well as providing more efficient lookup under some circumstances).

In this chapter, you'll be exploring temperatures, a DataFrame of average temperatures in 
cities around the world. pandas is loaded as pd.
"""

# region setup
import pandas as pd
temperatures = pd.read_csv('Module 8/data/temperatures.csv', index_col=0)
# endregion

## ---- START HERE ----

# Look at temperatures
print(____)

# Set the index of temperatures to "city", assigning to temperatures_ind.
temperatures_ind = ____

# Look at temperatures_ind. How is it different from temperatures?
print(____)

# Reset the temperatures_ind index, keeping its contents
print(____)

# Reset the temperatures_ind index, dropping its contents
print(____)
