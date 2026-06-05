"""
Adding new columns
==================

You aren't stuck with just the data you are given. Instead, you can add new columns to a DataFrame. 
This has many names, such as transforming, mutating, and feature engineering.

You can create new columns from scratch, but it is also common to derive them from other columns, 
for example, by adding columns together or by changing their units.

homelessness is a DataFrame containing estimates of homelessness in each U.S. state in 2018. 
The individual column is the number of homeless individuals not part of a family with children. 
The family_members column is the number of homeless individuals part of a family with children. 
The state_pop column is the state's total population.

homelessness is available and pandas is loaded as pd.
"""

# region setup
import pandas as pd
homelessness = pd.read_csv('Module 8/data/homelessness.csv')
# endregion

## ---- START HERE ----

# Add a new column to homelessness, named total, containing the sum of the individuals 
# and family_members columns.
____

# Add another column to homelessness, named p_homeless, containing the proportion of the 
# total homeless population to the total population in each state state_pop.
____

# See the result
print(homelessness)
