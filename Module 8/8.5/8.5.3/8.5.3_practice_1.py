"""
List of dictionaries
====================

You recently got some new avocado data from 2019 that you'd like to put in a DataFrame 
using the list of dictionaries method. Remember that with this method, 
you go through the data row by row.

date 	        small_sold 	large_sold
"2019-11-03" 	10376832 	7835071
"2019-11-10" 	10717154 	8561348

pandas as pd is imported.
"""

# region setup
import pandas as pd
# endregion

## ---- START HERE ----

# Create a list of dictionaries with the new data called avocados_list.
avocados_list = [
    {____: ____, ____: ____, ____: ____},
    {____: ____, ____: ____, ____: ____},
]

# Convert the list into a DataFrame called avocados_2019.
avocados_2019 = ____

# Print your new DataFrame.
____