"""
Average versus median
=====================

You now know how to use numpy functions to get a better feeling for your data.

The baseball data is available as a 2D numpy array with 3 columns (height, weight, age) and 1015 rows. 
The name of this numpy array is np_baseball. After restructuring the data, however, you notice that 
some height values are abnormally high. 

Follow the instructions and discover which summary statistic is best suited if you're dealing with so-called outliers. 

np_baseball is available.
"""

# region setup
import pandas as pd
np_baseball = pd.read_csv("Module 4/data/baseball.csv")[['Height', 'Weight', 'Age']].to_numpy()
np_baseball[slice(0, 1015, 50), 0] = np_baseball[slice(0, 1015, 50), 0]*1000
import numpy as np
# endregion

import numpy as np

## ---- START HERE ----

# Create numpy array np_height_in that is equal to first column of np_baseball


# Print out the mean of np_height_in


# Print out the median of np_height_in
