"""
2D Arithmetic
=============

2D numpy arrays can perform calculations element by element, like numpy arrays.

np_baseball is coded for you; it's again a 2D numpy array with 3 columns representing height (in inches), 
weight (in pounds) and age (in years). 

baseball is available as a regular list of lists and updated is available as 2D numpy array.
"""

# region setup
import pandas as pd
import numpy as np
baseball = pd.read_csv("Module 4/data/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy().tolist()
n = len(baseball)
updated = np.array(pd.read_csv("Module 4/data/update.csv", header = None))
import numpy as np
# endregion

import numpy as np

np_baseball = np.array(baseball)

## ---- START HERE ----

# You managed to get hold of the changes in height, weight and age of all baseball players. 
# It is available as a 2D numpy array, updated. Add np_baseball and updated and print out the result.


# You want to convert the units of height and weight to metric (meters and kilograms, respectively). 
# As a first step, create a numpy array with three values: 0.0254, 0.453592 and 1. 
# Name this array conversion


# Multiply np_baseball with conversion and print out the result.
