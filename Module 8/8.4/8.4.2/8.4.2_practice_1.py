"""
Slicing index values
====================

Slicing lets you select consecutive elements of an object using first:last syntax. 
DataFrames can be sliced by index values or by row/column number; we'll start with the first case. 
This involves slicing inside the .loc[] method.

Compared to slicing lists, there are a few things to remember.

- You can only slice an index if the index is sorted (using .sort_index()).
- To slice at the outer level, first and last can be strings.
- To slice at inner levels, first and last should be tuples.
- If you pass a single slice to .loc[], it will slice the rows.

pandas is loaded as pd. temperatures_ind has country and city in the index, and is available.
"""

# region setup
import pandas as pd
temperatures = pd.read_csv('Module 8/data/temperatures.csv', index_col=0)
temperatures_ind = temperatures.set_index(["country", "city"])
# endregion

## ---- START HERE ----

# Sort the index of temperatures_ind
temperatures_srt = ____

# Subset rows from Pakistan to Philippines
print(____)

# Try to subset rows from Lahore to Manila (This will return nonsense)
print(____)

# Subset rows from Pakistan, Lahore to Philippines, Manila
print(____)
