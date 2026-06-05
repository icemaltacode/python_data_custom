"""
Subsetting pivot tables
=======================

A pivot table is just a DataFrame with sorted indexes, so the techniques you have 
learned already can be used to subset them. In particular, the .loc[] + slicing 
combination is often helpful.

pandas is loaded as pd. temp_by_country_city_vs_year is available.
"""

# region setup
import pandas as pd
temperatures = pd.read_csv('Module 8/data/temperatures.csv', index_col=0, parse_dates=["date"])
temperatures['date'] = pd.to_datetime(temperatures.date)
temperatures["year"] = temperatures["date"].dt.year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c", index = ["country", "city"], columns = "year")
# endregion

## ---- START HERE ----

# Use .loc[] on temp_by_country_city_vs_year to take subsets:

# From Egypt to India.
____

# From Egypt, Cairo to India, Delhi.
____

# From Egypt, Cairo to India, Delhi, and 2005 to 2010.
____
