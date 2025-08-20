"""Utility for reading login data from an Excel file."""
import os
import openpyxl

def get_login_data(file_path="testdata/login_data.xlsx"):
    """
    Read login data from the specified Excel file.
    Returns a list of tuples (username, password, expected).
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Excel file not found: {file_path}")
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(row)
    return data
