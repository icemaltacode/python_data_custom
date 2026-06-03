"""
Subsetting 2D NumPy Arrays
==========================

You realize that it makes more sense to restructure all this information in a 2D numpy array.

You have a Python list of lists. In this list of lists, each sublist represents the height and weight of a single baseball player. 
The name of this list is baseball and it has been loaded for you already (although you can't see it).

Store the data as a 2D array to unlock numpy's extra functionality.
"""

# region setup
import pandas as pd
baseball = pd.read_csv("Module 4/data/baseball.csv")[['Height', 'Weight']].to_numpy().tolist()
import numpy as np
# endregion

import numpy as np

np_baseball = np.array(baseball)

## ---- START HERE ----

# Print out the 50th row of np_baseball


# Make a new variable, np_weight_lb, containing the entire second column of np_baseball


# Select the height (first column) of the 124th baseball player in np_baseball and print it out
