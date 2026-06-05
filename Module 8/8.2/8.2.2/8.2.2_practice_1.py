"""
Sorting rows
============

Finding interesting bits of data in a DataFrame is often easier if you change the order of the rows. 
You can sort the rows by passing a column name to .sort_values().

In cases where rows have the same value (this is common if you sort on a categorical variable), 
you may wish to break the ties by sorting on another column. 
You can sort on multiple columns in this way by passing a list of column names.

Sort on … 	        Syntax
------------------------------------------------------------
one column 	      |   df.sort_values("breed")
multiple columns  |   df.sort_values(["breed", "weight_kg"])

By combining .sort_values() with .head(), you can answer questions in the form, "What are the top cases where…?".

homelessness is available and pandas is loaded as pd.
"""

# region setup
import pandas as pd
homelessness = pd.read_csv('Module 8/data/homelessness.csv')
# endregion

## ---- START HERE ----

# STEP 1
# Sort homelessness by the number of homeless individuals in the individuals column, from smallest to largest, 
# and save this as homelessness_ind.
homelessness_ind = ____

# Print the head of the sorted DataFrame.
print(____)

# STEP 2
# Sort homelessness by the number of homeless family_members in descending order. 
# Save this as homelessness_fam
homelessness_fam = ____

# Print the head of the sorted DataFrame.
print(homelessness_fam.head())

# Sort homelessness first by region (ascending), and then by number of family members (descending). 
# Save this as homelessness_reg_fam.
homelessness_reg_fam = ____

# Print the top few rows
print(homelessness_reg_fam.head())