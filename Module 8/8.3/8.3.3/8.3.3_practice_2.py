"""
Calculations with .groupby()
============================

The .groupby() method makes life much easier. In this exercise, you'll perform the same calculations 
as last time, except you'll use the .groupby() method. 
You'll also perform calculations on data grouped by two variables to see if sales differ by store type 
depending on if it's a holiday week or not.

sales is available and pandas is loaded as pd.
"""

# region setup
import pandas as pd
sales = pd.read_csv('Module 8/data/sales_subset.csv')
# endregion

## ---- START HERE ----

# STEP 1
# Group sales by "type", take the sum of "weekly_sales", and store as sales_by_type.
sales_by_type = ____.____("____")["____"].____()

# Calculate the proportion of sales at each store type by dividing by the sum of sales_by_type. 
# Assign to sales_propn_by_type.
sales_propn_by_type = ____ / sum(____)
print(sales_propn_by_type)

# STEP 2
# Group sales by "type" and "is_holiday", take the sum of weekly_sales, and store as sales_by_type_is_holiday.
sales_by_type_is_holiday = ____
print(sales_by_type_is_holiday)
