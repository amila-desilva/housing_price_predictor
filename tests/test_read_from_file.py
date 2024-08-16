import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils.read_from_file import read_from_file


def test_read_from_file_success(tmp_path):
    # Create a temporary file with sample data
    file_path = tmp_path / "test_data.xlsx"
    df_expected = pd.DataFrame({
        'ID': [1, 2],
        'Value': ['A', 'B']
    })
    df_expected.to_excel(file_path, index=False)

    # Test reading the file
    df_result = read_from_file(file_path)

    # Check if the returned DataFrame matches the expected DataFrame
    pd.testing.assert_frame_equal(df_result, df_expected)


def test_read_from_file_no_file():
    # Test reading a non-existent file
    df_result = read_from_file("non_existent_file.xlsx")
    
    # Check if the function returns None
    assert df_result is None


def test_read_from_file_invalid_file(tmp_path):
    # Create an invalid Excel file
    file_path = tmp_path / "invalid_file.xlsx"
    with open(file_path, 'w') as f:
        f.write("This is not a valid Excel file")

    # Test reading the invalid file
    df_result = read_from_file(file_path)
    
    # Check if the function returns None
    assert df_result is None
