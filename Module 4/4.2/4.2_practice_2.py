"""
Writing the Data
================

A report with only headers isn't much use. Time to fill it with the actual
players.

The baseball dataset is loaded for you with pandas as `data`, already trimmed
to the four columns you need. A workbook with a header row in "Players" is set
up for you too.

Loop over the rows of `data` and append each one to the worksheet, then save.
When you open report.xlsx you should see the header followed by 1015 players.
"""

# region setup
import pandas as pd
from openpyxl import Workbook

data = pd.read_csv("Module 4/data/baseball.csv")[["Name", "Height", "Weight", "Age"]]

wb = Workbook()
ws = wb.active
ws.title = "Players"
ws.append(["Name", "Height", "Weight", "Age"])
# endregion

## ---- START HERE ----

# Append each row of the dataset to the worksheet.
# Hint: data.itertuples(index=False) yields one row at a time,
#       and ws.append(row) writes a whole row in one go.
for row in data.itertuples(index=False):
    pass  # replace this with ws.append(...)

# Save the workbook as "report.xlsx"

