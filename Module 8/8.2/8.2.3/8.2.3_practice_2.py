"""
Combo-attack!
=============

You've seen the four most common types of data manipulation: sorting rows, subsetting columns, 
subsetting rows, and adding new columns. In a real-life data analysis, you can mix and match 
these four manipulations to answer a multitude of questions.

In this exercise, you'll answer the question, "Which state has the highest number of homeless 
individuals per 10,000 people in the state?" Combine your new pandas skills to find out.
"""

# region setup
import pandas as pd
homelessness = pd.read_csv('Module 8/data/homelessness.csv')
# endregion

## ---- START HERE ----

# Add a column to homelessness, indiv_per_10k, containing the number of homeless individuals 
# per ten thousand people in each state, using state_pop for state population.
homelessness["indiv_per_10k"] = 10000 * ____ / ____ 

# Subset rows where indiv_per_10k is higher than 20, assigning to high_homelessness.
high_homelessness = ____

# Sort high_homelessness by descending indiv_per_10k, assigning to high_homelessness_srt.
high_homelessness_srt = ____

# Select only the state and indiv_per_10k columns of high_homelessness_srt and save as result. 
result = ____

# Look at the result.
print(result)
