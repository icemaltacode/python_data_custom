"""
Parts of a DataFrame
====================

To better understand DataFrame objects, it's useful to know that they consist of three components:

    values: A two-dimensional NumPy array, accessed via the .to_numpy() method.
    columns: An index of column names, accessed via the .columns attribute.
    index: An index for the rows, accessed via the .index attribute.

You can usually think of indexes as a list of strings or numbers, though the pandas Index data type 
allows for more sophisticated options. (These will be covered later in the module.)

homelessness is available.
"""

# region setup
import pandas as pd
homelessness = pd.read_csv('Module 8/data/homelessness.csv')
# endregion

## ---- START HERE ----

# Import pandas using the alias pd.
____

# Print a 2D NumPy array of the values in homelessness.
____

# Print the column names of homelessness.
____

# Print the index of homelessness.
____