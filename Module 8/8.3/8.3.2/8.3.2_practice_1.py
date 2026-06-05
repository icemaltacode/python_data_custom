"""
Dropping duplicates
===================

Summary statistics are exactly what they sound like - they summarize many numbers in one statistic. 
For example, mean, median, minimum, maximum, and standard deviation are summary statistics. 
Calculating summary statistics allows you to get a better sense of your data, even if there's a lot of it.

sales is available and pandas is loaded as pd.
"""

# region setup
import pandas as pd
sales = pd.read_csv('Module 8/data/sales_subset.csv')
# endregion

## ---- START HERE ----

# Remove rows of sales with duplicate pairs of store and type and save as store_types and print the head.
store_types = ____
print(store_types.head())

# Remove rows of sales with duplicate pairs of store and department and save as store_depts and print the head.
store_depts = ____
print(store_depts.head())

# Subset the rows that are holiday weeks using the is_holiday column, and drop the duplicate dates, 
# saving as holiday_dates.
holiday_dates = sales[sales[____]].drop_duplicates(____)

# Select the date column of holiday_dates, and print.
print(____)