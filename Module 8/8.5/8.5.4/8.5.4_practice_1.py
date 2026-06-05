"""
CSV to DataFrame
================

You work for an airline, and your manager has asked you to do a competitive analysis and 
see how often passengers flying on other airlines are involuntarily bumped from their flights. 
You got a CSV file (airline_bumping.csv) from the Department of Transportation containing 
data on passengers that were involuntarily denied boarding in 2016 and 2017, but it doesn't 
have the exact numbers you want. In order to figure this out, you'll need to get the 
CSV into a pandas DataFrame and do some manipulation!

pandas is imported for you as pd. "airline_bumping.csv" is in your working directory.
"""

# region setup
import pandas as pd
# endregion

## ---- START HERE ----

# Read the CSV file "Module 8/data/airline_bumping.csv" and store it as a 
# DataFrame called airline_bumping.
airline_bumping = ____

# Print the first few rows of airline_bumping.
print(____)

# For each airline group, select the nb_bumped, and total_passengers columns, 
# and calculate the sum (for both years). 
# Store this as airline_totals.
airline_totals = airline_bumping.groupby(____)[[____]].____

# Create a new column of airline_totals called bumps_per_10k, which is the number of 
# passengers bumped per 10,000 passengers in 2016 and 2017.
airline_totals["bumps_per_10k"] = ____ / ____ * 10000

# Print airline_totals to see the results of your manipulations.
____