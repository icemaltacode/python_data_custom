# CSV Sales Summary

A simple desktop application built with Python and Tkinter. It lets you choose
a CSV file of sales data and instantly shows a short summary.

This project is used to demonstrate how a normal Python program can later be
packaged into a standalone executable using **PyInstaller**.

## What the app does

When you open a CSV file, the app displays:

- The selected file name
- The total number of rows
- The total revenue (`quantity * unit_price` for every row, summed up)
- The best-selling product (the product with the highest total quantity sold)

The CSV file must have these columns:

```csv
date,product,category,quantity,unit_price
```

A sample `sales.csv` file is included so you can try it straight away.

## How to run it normally

Make sure you have Python 3 installed, then run:

```bash
python app.py
```

The app only uses Python's standard library, so there is nothing extra to
install to run it.

## How to install PyInstaller

PyInstaller is the tool that turns the Python script into a standalone
executable. Install it with pip:

```bash
pip install pyinstaller
```

## How to build the executable

From inside the project folder, run:

```bash
pyinstaller --onefile --windowed --name "CSV Sales Summary" app.py
```

- `--onefile` bundles everything into a single executable file.
- `--windowed` hides the console window (useful for GUI apps).
- `--name` sets the name of the generated executable.

When the build finishes, the executable will be created inside the **`dist`**
folder. You can run it directly without needing Python installed.
