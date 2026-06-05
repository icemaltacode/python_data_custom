"""
Summarising dates
=================

Summary statistics can also be calculated on date columns that have values with the data type datetime64. 
Some summary statistics — like mean — don't make a ton of sense on dates, but others are super helpful, 
for example, minimum and maximum, which allow you to see what time range your data covers.

sales is available and pandas is loaded as pd.
"""

# region setup
import pandas as pd
sales = pd.read_csv('Module 8/data/sales_subset.csv')
# endregion

## ---- START HERE ----

# Print the maximum of the date column
____

# Print the minimum of the date column
____
