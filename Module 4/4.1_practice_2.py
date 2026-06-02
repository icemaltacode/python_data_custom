# Exercise Setup
import pandas as pd
mlb = pd.read_csv("Module 4/data/baseball.csv")
height_in = mlb['Height'].tolist()

## ---- START HERE ---- 

# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
# Note: 1 inch = 0.0254 meters
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)