"""
Explore the baseball data
=========================

Because the mean and median are so far apart, you decide to complain to the MLB. 
They find the error and send the corrected data over to you. 
It's again available as a 2D NumPy array np_baseball, with three columns.

The Python script in the editor already includes code to print out informative messages 
with the different summary statistics and numpy is already loaded as np. 

Can you finish the job? np_baseball is available.
"""

# region setup
import pandas as pd
np_baseball = pd.read_csv("Module 4/data/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy()
import numpy as np
# endregion

# The code to print out the mean height is already included
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

## ---- START HERE ----

# Complete the code for the median height
med = ____
print("Median: " + str(med))

# Use np.std() on the first column of np_baseball to calculate stddev
stddev = ____
print("Standard Deviation: " + str(stddev))

# Do big players tend to be heavier? Use np.corrcoef() to store the correlation 
# between the first and second column of np_baseball in corr
corr = ____
print("Correlation: " + str(corr))