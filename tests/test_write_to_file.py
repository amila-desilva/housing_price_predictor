import pytest
import pandas as pd
from unittest import mock
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils.write_to_file import write_to_file


def test_write_to_file_success(tmp_path):
    # Create a temporary file path
    file_path = tmp_path / "test_output.xlsx"

    # Create a sample DataFrame to write
    df_to_write = pd.DataFrame({
        'ID': [1, 2],
        'Value': ['A', 'B']
    })

    # Test writing the DataFrame to the file
    write_to_file(df_to_write, file_path)

    # Read the file back and verify the content
    df_result = pd.read_excel(file_path)
    pd.testing.assert_frame_equal(df_result, df_to_write)


def test_write_to_file_no_permission(tmp_path):
    # Create a temporary file path
    file_path = tmp_path / "test_output.xlsx"

    # Simulate a permission error by mocking the pandas to_excel method
    with mock.patch("pandas.DataFrame.to_excel", side_effect=PermissionError):
        # Create a sample DataFrame to write
        df_to_write = pd.DataFrame({
            'ID': [1, 2],
            'Value': ['A', 'B']
        })

        # Test writing the DataFrame to the file and ensure the PermissionError is raised
        with pytest.raises(PermissionError):
            write_to_file(df_to_write, file_path)
