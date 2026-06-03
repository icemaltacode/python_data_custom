"""
Baseball players' height
========================

You are a huge baseball fan. You decide to call the MLB (Major League Baseball) and ask 
around for some more statistics on the height of the main players. 
They pass along data on more than a thousand players, which is stored as a regular 
Python list: height_in. The height is expressed in inches. 
Can you make a numpy array out of it and convert the units to meters?

height_in is already available and the numpy package is loaded, so you can start straight 
away (Source: stat.ucla.edu).
"""

# region setup
import pandas as pd
mlb = pd.read_csv("Module 4/data/baseball.csv")
height_in = mlb['Height'].tolist()
# endregion

## ---- START HERE ----

# Import numpy
import numpy as np

# Create a numpy array from height_in. Name this new array np_height_in.


# Print out np_height_in.


# Multiply np_height_in by 0.0254 to convert from inches to meters.
# Store the result in a new array, np_height_m.


# Print out np_height_m and check whether the output makes sense.
