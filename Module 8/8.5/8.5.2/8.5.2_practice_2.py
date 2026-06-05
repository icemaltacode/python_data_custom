"""
Removing missing values
=======================

Now that you know there are some missing values in your DataFrame, you have a few options 
to deal with them. One way is to remove them from the dataset completely. 
In this exercise, you'll remove missing values by removing all rows that contain missing values.

pandas has been imported as pd and avocados_2016 is available.
"""

# region setup
import pandas as pd
import matplotlib.pyplot as plt
avocados_2016 = pd.read_pickle('Module 8/data/avocados_2016.pkl')
# endregion

## ---- START HERE ----

# Remove the rows of avocados_2016 that contain missing values and store 
# the remaining rows in avocados_complete.
avocados_complete = ____

# Verify that all missing values have been removed from avocados_complete. 
# Calculate each column that has NAs and print.
print(____)