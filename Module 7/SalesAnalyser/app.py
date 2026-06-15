"""
CSV Sales Summary
-----------------
A small Tkinter desktop app that loads a CSV of sales data and shows a
quick summary: number of rows, total revenue, and the best-selling product.

This project is intentionally simple so it can later be packaged into a
standalone executable using PyInstaller. It only uses Python's standard
library (tkinter + csv).

Run with:
    python app.py
"""

import csv
import tkinter as tk
from tkinter import filedialog, messagebox


def load_sales(filename):
    """Read the CSV file and return a list of sale dictionaries.

    Each row is converted so that quantity is an int and unit_price is a
    float, ready for the calculations below.
    """
    sales = []
    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sales.append({
                "date": row["date"],
                "product": row["product"],
                "category": row["category"],
                "quantity": int(row["quantity"]),
                "unit_price": float(row["unit_price"]),
            })
    return sales


def calculate_total_revenue(sales):
    """Return the total revenue across all sales (quantity * unit_price)."""
    total = 0.0
    for sale in sales:
        total += sale["quantity"] * sale["unit_price"]
    return total


def find_best_selling_product(sales):
    """Return the product with the highest total quantity sold."""
    quantities = {}
    for sale in sales:
        product = sale["product"]
        quantities[product] = quantities.get(product, 0) + sale["quantity"]

    # max() picks the product whose total quantity is largest.
    return max(quantities, key=quantities.get)


class SalesSummaryApp:
    """The main application window."""

    def __init__(self, root):
        self.root = root
        self.root.title("CSV Sales Summary")
        self.root.geometry("500x400")
        self.root.minsize(500, 400)

        # Heading
        heading = tk.Label(root, text="CSV Sales Summary", font=("Arial", 16, "bold"))
        heading.pack(pady=15)

        # Button to choose a CSV file
        choose_button = tk.Button(root, text="Choose CSV File", command=self.choose_file)
        choose_button.pack(pady=10)

        # Labels for the results
        self.filename_label = tk.Label(root, text="No file selected")
        self.filename_label.pack(pady=5)

        self.rows_label = tk.Label(root, text="Rows: -")
        self.rows_label.pack(pady=5)

        self.revenue_label = tk.Label(root, text="Total revenue: -")
        self.revenue_label.pack(pady=5)

        self.best_seller_label = tk.Label(root, text="Best-selling product: -")
        self.best_seller_label.pack(pady=5)

    def choose_file(self):
        """Ask the user for a CSV file, process it, and update the labels."""
        filename = filedialog.askopenfilename(
            title="Choose a CSV file",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
        )

        # The user closed the dialog without choosing a file.
        if not filename:
            return

        try:
            sales = load_sales(filename)

            if not sales:
                messagebox.showwarning("Empty file", "The CSV file has no data rows.")
                return

            total_revenue = calculate_total_revenue(sales)
            best_seller = find_best_selling_product(sales)

            # Show only the file name (not the full path) for a cleaner look.
            short_name = filename.split("/")[-1].split("\\")[-1]

            self.filename_label.config(text=f"File: {short_name}")
            self.rows_label.config(text=f"Rows: {len(sales)}")
            self.revenue_label.config(text=f"Total revenue: ${total_revenue:,.2f}")
            self.best_seller_label.config(text=f"Best-selling product: {best_seller}")

        except Exception as error:
            messagebox.showerror(
                "Error",
                f"Could not load or process the CSV file.\n\n{error}",
            )


def main():
    root = tk.Tk()
    SalesSummaryApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
