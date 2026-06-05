"""
Cumulative statistics
=====================

Cumulative statistics can also be helpful in tracking summary statistics over time. 
In this exercise, you'll calculate the cumulative sum and cumulative max of a department's weekly sales, 
which will allow you to identify what the total sales were so far as well as what the highest weekly sales 
were so far.

A DataFrame called sales_1_1 has been created for you, which contains the sales data for department 1 of store 1. 

pandas is loaded as pd.
"""

# region setup
import pandas as pd
sales = pd.read_csv('Module 8/data/sales_subset.csv')
sales_1_1 = sales.query("department == 1 & store == 1")
# endregion

## ---- START HERE ----

# Sort the rows of sales_1_1 by the date column in ascending order.
sales_1_1 = ____

# Get the cumulative sum of weekly_sales and add it as a new column of sales_1_1 called cum_weekly_sales.
sales_1_1[____] = ____

# Get the cumulative maximum of weekly_sales, and add it as a column called cum_max_sales.
____

# Print the date, weekly_sales, cum_weekly_sales, and cum_max_sales columns.
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])
