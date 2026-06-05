"""
Subsetting columns
==================

When working with data, you may not need all of the variables in your dataset. 
Square brackets ([]) can be used to select only the columns that matter to you in an order that makes sense to you. 

To select only "col_a" of the DataFrame df, use

df["col_a"]

To select "col_a" and "col_b" of df, use

df[["col_a", "col_b"]]

homelessness is available and pandas is loaded as pd.
"""

# region setup
import pandas as pd
homelessness = pd.read_csv('Module 8/data/homelessness.csv')
# endregion

## ---- START HERE ----

# STEP 1
# Create a Series called individuals that contains only the individuals column of homelessness.
individuals = ____

# Print the head of individuals.
print(individuals.head())

# STEP 2
# Create a DataFrame called state_fam that contains only the state and family_members columns 
# of homelessness, in that order.
state_fam = ____

# Print the head of state_fam.
print(state_fam.head())

# STEP 3
# Create a DataFrame called ind_state that contains the individuals and state columns of 
# homelessness, in that order.
ind_state = ____

# print the head of ind_state.
print(ind_state.head())