"""
Counting categorical variables
==============================

Counting is a great way to get an overview of your data and to spot curiosities that you might not notice 
otherwise. In this exercise, you'll count the number of each type of store and the number of each 
department number using the DataFrames you created in the previous exercise:

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=["store", "type"])

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store", "department"])

The store_types and store_depts DataFrames you created in the last exercise are available, 
and pandas is imported as pd.
"""

# region setup
import pandas as pd
sales = pd.read_csv('Module 8/data/sales_subset.csv')
store_types = sales.drop_duplicates(subset=["store", "type"])
store_depts = sales.drop_duplicates(subset=["store", "department"])
# endregion

## ---- START HERE ----

# Count the number of stores of each store type in store_types.
store_counts = ____
print(store_counts)

# Count the proportion of stores of each store type in store_types.
store_props = ____
print(store_props)

# Count the number of stores of each department in store_depts, sorting the counts 
# in descending order.
dept_counts_sorted = ____
print(dept_counts_sorted)

# Count the proportion of stores of each department in store_depts, sorting the proportions 
# in descending order.
dept_props_sorted = ____.____(sort=____, normalize=____)
print(dept_props_sorted)
