"""
Changes in sales over time
==========================

Line plots are designed to visualize the relationship between two numeric variables, 
where each data values is connected to the next one. They are especially useful for 
visualizing the change in a number over time since each time point is naturally 
connected to the next time point. In this exercise, you'll visualize the change in 
avocado sales over three years.

pandas has been imported as pd, and avocados is available.
"""

# region setup
import pandas as pd
avocados = pd.read_pickle('Module 8/data/avoplotto.pkl')
# endregion

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

## ---- START HERE ----

# Get the total number of avocados sold on each date. 
# The DataFrame has two rows for each date—one for organic, and one for conventional. 
# Save this as nb_sold_by_date.
nb_sold_by_date = ____

# Create a line plot of the number of avocados sold by date
____

# Show the plot
____