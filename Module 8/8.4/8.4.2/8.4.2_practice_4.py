"""
Subsetting by row/column number
===============================

The most common ways to subset rows are the ways we've previously discussed: 
using a Boolean condition or by index labels. 
However, it is also occasionally useful to pass row numbers.

This is done using .iloc[], and like .loc[], it can take two arguments to let you 
subset by rows and columns.

pandas is loaded as pd. temperatures (without an index) is available.
"""

# region setup
import pandas as pd
temperatures = pd.read_csv('Module 8/data/temperatures.csv', index_col=0, parse_dates=["date"])
# endregion

## ---- START HERE ----

# Get the 23rd row, 2nd column (index positions 22 and 1).
print(____)

# Get the first 5 rows (index positions 0 to 5).
print(____)

# Get all rows, columns 3 and 4 (index positions 2 to 4).
print(____)

# Get the first 5 rows, columns 3 and 4.
print(____)
