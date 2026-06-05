"""
Multiple grouped summaries
==========================

Earlier in this chapter, you saw that the .agg() method is useful to compute multiple statistics 
on multiple variables. It also works with grouped data. You can use built-in functions like min, 
max, mean, and median.

sales is available and pandas is imported as pd.
"""

# region setup
import pandas as pd
sales = pd.read_csv('Module 8/data/sales_subset.csv')
# endregion

## ---- START HERE ----

# Get the min, max, mean, and median of weekly_sales for each store type using .groupby() and .agg(). 
# Store this as sales_stats.
sales_stats = ____

# Print sales_stats
print(sales_stats)

# Get the min, max, mean, and median of unemployment and fuel_price_usd_per_l for each store type. 
# Store this as unemp_fuel_stats.
unemp_fuel_stats = ____

# Print unemp_fuel_stats
print(unemp_fuel_stats)
