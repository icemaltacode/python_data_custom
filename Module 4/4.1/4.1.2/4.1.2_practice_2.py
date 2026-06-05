"""
Baseball data in 2D form
========================

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

## ---- START HERE ----

# Use np.array() to create a 2D numpy array from baseball. Name it np_baseball.
np_baseball = ____

# Print out the shape attribute of np_baseball.
