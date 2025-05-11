import os
import json
from code.extract import fetch_311_data

def test_fetch_311_data_saves_json():
    # Run the extract
    data = fetch_311_data(limit=100)

    # Check file exists
    assert os.path.exists("cache/raw_311_data.json"), "raw_311_data.json not found"

    # Check file is not empty
    with open("cache/raw_311_data.json", "r") as f:
        loaded = json.load(f)
    assert len(loaded) > 0, "Extracted data is empty"

    # Check data matches what was returned
    assert isinstance(data, list), "Returned data is not a list"
    assert data == loaded, "Saved and returned data do not match"