"""
What percent of sales occurred at each store type?
==================================================

While .groupby() is useful, you can calculate grouped summary statistics without it.

Walmart distinguishes three types of stores: "supercenters," "discount stores," and 
"neighborhood markets," encoded in this dataset as type "A," "B," and "C." 
In this exercise, you'll calculate the total sales made at each store type, 
without using .groupby(). You can then use these numbers to see what proportion of Walmart's 
total sales were made at each type.

sales is available and pandas is imported as pd.
"""

# region setup
import pandas as pd
sales = pd.read_csv('Module 8/data/sales_subset.csv')
# endregion

## ---- START HERE ----

# Calculate the total weekly_sales over the whole dataset.
sales_all = ____["____"].____()

# Subset for type "A" stores, and calculate their total weekly sales.
sales_A = ____[____["____"] == "____"]["____"].____()

# Do the same for type "B" stores
sales_B = ____

# Do the same for type "C" stores
sales_C = ____

# Combine the A/B/C results into a list, and divide by sales_all to get the proportion of sales by type.
sales_propn_by_type = [sales_A, ____, ____] / ____
print(sales_propn_by_type)
