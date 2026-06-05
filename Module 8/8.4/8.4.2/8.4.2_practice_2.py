"""
Slicing in both directions
==========================

You've seen slicing DataFrames by rows and by columns, but since DataFrames are two-dimensional objects, 
it is often natural to slice both dimensions at once. 
That is, by passing two arguments to .loc[], you can subset by rows and columns in one go.

pandas is loaded as pd. temperatures_srt is indexed by country and city, has a sorted index, and is available.
"""

# region setup
import pandas as pd
temperatures = pd.read_csv('Module 8/data/temperatures.csv', index_col=0)
temperatures_ind = temperatures.set_index(["country", "city"])
temperatures_srt = temperatures_ind.sort_index()
# endregion

## ---- START HERE ----

# Use .loc[] slicing to subset rows from India, Hyderabad to Iraq, Baghdad.
print(____)

# Use .loc[] slicing to subset columns from date to avg_temp_c.
print(____)

# Slice in both directions at once from Hyderabad to Baghdad, and date to avg_temp_c.
print(____)
