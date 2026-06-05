"""
DataFrame to CSV
================

You're almost there! To make things easier to read, you'll need to sort the data and export 
it to CSV so that your colleagues can read it.

pandas as pd has been imported for you, and the airline_totals DataFrame from the previous 
exercise is available.
"""

# region setup
import pandas as pd
airline_bumping = pd.read_csv('Module 8/data/airline_bumping.csv')
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000
# endregion

## ---- START HERE ----

# Sort airline_totals by the values of bumps_per_10k from highest to lowest, 
# storing as airline_totals_sorted.
airline_totals_sorted = ____

# Print your sorted DataFrame.
____

# Save the sorted DataFrame as a CSV called "airline_totals_sorted.csv"
____