"""
Replacing missing values
========================

Another way of handling missing values is to replace them all with the same value. 
For numerical variables, one option is to replace values with 0— you'll do this here. 
However, when you replace missing values, you make assumptions about what a missing 
value means. In this case, you will assume that a missing number sold means that no sales 
for that avocado type were made that week.

In this exercise, you'll see how replacing missing values can affect the distribution 
of a variable using histograms. You can plot histograms for multiple variables at a time 
as follows:

dogs[["height_cm", "weight_kg"]].hist()

pandas has been imported as pd and matplotlib.pyplot has been imported as plt. 
The avocados_2016 dataset is available.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt
avocados_2016 = pd.read_pickle('Module 8/data/avocados_2016.pkl')
# endregion

# A list has been created, cols_with_missing, containing the names of columns with missing 
# values: "small_sold", "large_sold", and "xl_sold".
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

## ---- START HERE ----

# Create histograms showing the distributions cols_with_missing
avocados_2016[____].____

# Show the plot
____

# Replace the missing values of avocados_2016 with 0s and store the result as avocados_filled.
avocados_filled = ____

# Create a histogram of the cols_with_missing columns of avocados_filled.
____

# Show the plot
____