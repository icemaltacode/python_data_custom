"""
Your First Workbook
====================

You've analysed the baseball data with NumPy. Now your manager wants it as an
Excel file they can open and share.

The first step is to create a workbook, give its sheet a sensible name, and
write a header row. openpyxl is already installed in your environment.

Create a new workbook, name the active sheet "Players", write the four column
headers across row 1, then save the file as "report.xlsx".
"""

# region setup
from openpyxl import Workbook
# endregion

headers = ["Name", "Height", "Weight", "Age"]

## ---- START HERE ----

# Create a new workbook: wb


# Get the active worksheet: ws


# Name the sheet "Players"


# Write each header into row 1.
# Hint: enumerate(headers, start=1) gives you (column_number, title)
for column, title in enumerate(headers, start=1):
    pass  # replace this: use ws.cell(row=..., column=..., value=...)

# Save the workbook as "report.xlsx"

