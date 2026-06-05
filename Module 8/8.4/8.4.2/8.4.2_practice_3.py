"""
Slicing time series
===================

Slicing is particularly useful for time series since it's a common thing to want to filter for data within a 
date range. Add the date column to the index, then use .loc[] to perform the subsetting. 
The important thing to remember is to keep your dates in ISO 8601 format, that is, "yyyy-mm-dd" 
for year-month-day, "yyyy-mm" for year-month, and "yyyy" for year.

Recall that you can combine multiple Boolean conditions using logical operators, such as &. 
To do so in one line of code, you'll need to add parentheses () around each condition.

pandas is loaded as pd and temperatures, with no index, is available.
"""

# region setup
import pandas as pd
temperatures = pd.read_csv('Module 8/data/temperatures.csv', index_col=0, parse_dates=["date"])
# endregion

## ---- START HERE ----

# Use Boolean conditions, not .isin() or .loc[], and the full date "yyyy-mm-dd", to 
# subset temperatures for rows where the date column is in 2010 and 2011 and print the results.
temperatures_bool = ____[(____ >= ____) & (____ <= ____)]
print(temperatures_bool)

# Set the index of temperatures to the date column and sort it.
temperatures_ind = temperatures.____.____

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011.
print(____)

# Use .loc[] to subset temperatures_ind for rows from August 2010 to February 2011.
print(____)
