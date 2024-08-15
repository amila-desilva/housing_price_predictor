import pandas as pd

def write_to_file(data, file_path: str):
    """
    Writes data to an Excel file.
    
    Args:
        data (pd.DataFrame or list of dict): The data to write to the file.
        file_path (str): The path to the file to write.
    """
    try:
        if isinstance(data, pd.DataFrame):
            data.to_excel(file_path, index=False)
        elif isinstance(data, list):
            df = pd.DataFrame(data)
            df.to_excel(file_path, index=False)
        else:
            print("Unsupported data type. Please provide a pandas DataFrame or a list of dictionaries.")
    except Exception as e:
        print(f"Error writing to the file: {e}")
        raise
