"""
Efficient summaries
===================

While pandas and NumPy have many functions, sometimes, you may need a different function to summarize your data.

The .agg() method allows you to apply your own custom functions to a DataFrame, as well as apply functions to 
more than one column of a DataFrame at once, making your aggregations super-efficient. 

For example,

df['column'].agg(function)

In the custom function for this exercise, "IQR" is short for inter-quartile range, 
which is the 75th percentile minus the 25th percentile. 
It's an alternative to standard deviation that is helpful if your data contains outliers.

sales is available and pandas is loaded as pd.
"""

# region setup
import pandas as pd
sales = pd.read_csv('Module 8/data/sales_subset.csv')
# endregion

# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

## ---- START HERE ----

# STEP 1
# Use the custom iqr function defined for you along with .agg() to print the IQR of 
# the temperature_c column of sales.
print(____)

# STEP 2
# Update the column selection to use the custom iqr function with .agg() to print the 
# IQR of temperature_c, fuel_price_usd_per_l, and unemployment, in that order.
print(sales[["temperature_c", ____, ____]].agg(iqr))

# STEP 3
# Update the aggregation functions called by .agg(): include iqr and "median" in that order.
# Start with the code on line 40, and modify