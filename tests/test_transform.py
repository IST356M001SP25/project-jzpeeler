import os
import pandas as pd
from code.transform import clean_311_data

def test_clean_311_data_saves_csv():
    # Run the transform
    df = clean_311_data("cache/raw_311_data.json", "cache/clean_311_data.csv")

    # Check file exists
    assert os.path.exists("cache/clean_311_data.csv"), "clean_311_data.csv not found"

    # Check DataFrame has required columns
    expected_cols = {"created_date", "complaint_type", "borough", "descriptor", "latitude", "longitude"}
    assert expected_cols.issubset(df.columns), "Missing expected columns in cleaned data"

    # Check no missing values in key columns
    assert not df[["created_date", "complaint_type", "borough"]].isnull().values.any(), "Missing data in key fields"

    # Check number of rows is reasonable
    assert len(df) > 0, "Cleaned DataFrame is empty"