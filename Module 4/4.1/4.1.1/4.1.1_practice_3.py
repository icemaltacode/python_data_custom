"""
Subsetting NumPy Arrays
=======================

Subsetting (using the square bracket notation on lists or arrays) works exactly the same with both lists and arrays.

This exercise already has two lists, height_in and weight_lb, loaded in the background for you. 
These contain the height and weight of the MLB players as regular lists. 
It also has two numpy array lists, np_weight_lb and np_height_in prepared for you.
"""

# region setup
import pandas as pd
mlb = pd.read_csv("Module 4/data/baseball.csv")
height_in = mlb['Height'].tolist()
weight_lb = mlb['Weight'].tolist()
# endregion

import numpy as np

np_weight_lb = np.array(weight_lb)  # Baseball player weights
np_height_in = np.array(height_in)  # Baseball player heights

## ---- START HERE ---- 

# Subset np_weight_lb by printing out the element at index 50.


# Print out a sub-array of np_height_in that contains the elements at index 100 up to and including index 110.
