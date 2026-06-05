"""
Subsetting with .loc[]
======================

The killer feature for indexes is .loc[]: a subsetting method that accepts index values. 
When you pass it a single argument, it will take a subset of rows.

The code for subsetting using .loc[] can be easier to read than standard square bracket subsetting, 
which can make your code less burdensome to maintain.

pandas is loaded as pd. temperatures and temperatures_ind are available; the latter is indexed by city.
"""

# region setup
import pandas as pd
temperatures = pd.read_csv('Module 8/data/temperatures.csv', index_col=0)
temperatures_ind = temperatures.set_index("city")
# endregion

## ---- START HERE ----

# Create a list called cities that contains "London" and "Paris".
cities = ["____", "____"]

# Use [] subsetting to filter temperatures for rows where the city column takes a value in the cities list.
print(temperatures[____])

# Use .loc[] subsetting to filter temperatures_ind for rows where the city is in the cities list.
print(temperatures_ind.loc[____])
