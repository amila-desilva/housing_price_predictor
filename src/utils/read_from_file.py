import pandas as pd

def read_from_file(file_name: str):
    """
    Reads data from an Excel file and returns it as a pandas DataFrame.
    
    Args:
        file_name (str): The path to the file to read.
    
    Returns:
        pd.DataFrame: The data read from the file.
    """
    try:
        print(f"Attempting to read file: {file_name}")
        df = pd.read_excel(file_name)
        print("File read successfully.")
        return df
    except Exception as e:
        print(f"Error reading the file: {file_name}. Exception: {e}")
        return None
