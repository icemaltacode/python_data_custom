"""
Subsetting rows by categorical variables
========================================

Subsetting data based on a categorical variable often involves using the or operator (|) 
to select rows from multiple categories. 

This can get tedious when you want all states in one of three different regions, for example. 
Instead, use the .isin() method, which will allow you to tackle this problem by writing one 
condition instead of three separate ones.

colors = ["brown", "black", "tan"]
condition = dogs["color"].isin(colors)
dogs[condition]

homelessness is available and pandas is loaded as pd.
"""

# region setup
import pandas as pd
homelessness = pd.read_csv('Module 8/data/homelessness.csv')
# endregion

canu = ["California", "Arizona", "Nevada", "Utah"]

## ---- START HERE ----

# Filter homelessness for cases where the USA census state is in the list of Mojave states, 
# canu, assigning to mojave_homelessness. 
mojave_homelessness = homelessness[____]

# View the printed result.
print(mojave_homelessness)