"""
Setting multi-level indexes
===========================

Indexes can also be made out of multiple columns, forming a multi-level index (sometimes called 
a hierarchical index). There is a trade-off to using these.

The benefit is that multi-level indexes make it more natural to reason about nested categorical 
variables. For example, in a clinical trial, you might have control and treatment groups. 
Then each test subject belongs to one or another group, and we can say that a test subject is 
nested inside the treatment group. Similarly, in the temperature dataset, the city is located 
in the country, so we can say a city is nested inside the country.

The main downside is that the code for manipulating indexes is different from the code for 
manipulating columns, so you have to learn two syntaxes and keep track of how your data is represented.

pandas is loaded as pd. temperatures is available.
"""

# region setup
import pandas as pd
temperatures = pd.read_csv('Module 8/data/temperatures.csv', index_col=0)
temperatures_ind = temperatures.set_index("city")
# endregion

## ---- START HERE ----

# Set the index of temperatures to the "country" and "city" columns, and assign this to temperatures_ind.
temperatures_ind = ____

# Specify two country/city pairs to keep: "Brazil"/"Rio De Janeiro" and "Pakistan"/"Lahore", 
# assigning to rows_to_keep.
rows_to_keep = [____]

# Print and subset temperatures_ind for rows_to_keep using .loc[].
print(temperatures_ind.____)
