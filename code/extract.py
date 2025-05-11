import requests
import json
import os

def fetch_311_data(limit=5000, save_path="cache/raw_311_data.json"):
    url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"
    params = {
        "$limit": limit,
        "$order": "created_date DESC",
        "$select": "created_date, complaint_type, borough, descriptor, latitude, longitude"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "w") as f:
        json.dump(data, f)

    print(f"Saved {len(data)} records to {save_path}")
    return data


if __name__ == "__main__":
    fetch_311_data()