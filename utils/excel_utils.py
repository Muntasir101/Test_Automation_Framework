import pandas as pd

def read_test_data(excel_file, sheet_name):
    """
    Read test data from an Excel file.

    Args:
        excel_file (str): The path to the Excel file containing test data.
        sheet_name (str): The name of the sheet within the Excel file.

    Returns:
        pandas.DataFrame: A DataFrame containing the test data.
    """
    data = pd.read_excel(excel_file, sheet_name=sheet_name)
    return data

