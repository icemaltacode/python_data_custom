"""
Pivoting on one variable
========================

Pivot tables are the standard way of aggregating data in spreadsheets.

In pandas, pivot tables are essentially another way of performing grouped calculations. 
That is, the .pivot_table() method is an alternative to .groupby().

In this exercise, you'll perform calculations using .pivot_table() to replicate the 
calculations you performed in the last lesson using .groupby().

sales is available and pandas is imported as pd.
"""

# region setup
import pandas as pd
sales = pd.read_csv('Module 8/data/sales_subset.csv')
# endregion

## ---- START HERE ----

# STEP 1
# Get the mean weekly_sales by type using .pivot_table() and store as mean_sales_by_type.
mean_sales_by_type = sales.____

# Print mean_sales_by_type
print(mean_sales_by_type)

# STEP 2
# Get the mean and median of weekly_sales by type using .pivot_table() and store as mean_med_sales_by_type.
mean_med_sales_by_type = sales.pivot_table(____)

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# STEP 3
# Get the mean of weekly_sales by type and is_holiday using .pivot_table() and store as mean_sales_by_type_holiday.
mean_sales_by_type_holiday = sales.pivot_table(____)

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)