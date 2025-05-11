import pandas as pd
import json
import os

def clean_311_data(input_path="cache/raw_311_data.json", output_path="cache/clean_311_data.csv"):
    # Load the raw JSON data
    with open(input_path, "r") as f:
        raw_data = json.load(f)

    # Convert to DataFrame
    df = pd.DataFrame(raw_data)

    # Drop rows with missing critical values
    df = df.dropna(subset=["created_date", "complaint_type", "borough", "latitude", "longitude"])

    # Convert date column to datetime object
    df["created_date"] = pd.to_datetime(df["created_date"], errors="coerce")

    # Drop rows where date parsing failed
    df = df.dropna(subset=["created_date"])

    # Optional: Filter to 2024+ complaints only
    df = df[df["created_date"] >= "2024-01-01"]

    # Save cleaned data to CSV
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"Saved cleaned data to {output_path} with {len(df)} rows.")
    return df

if __name__ == "__main__":
    clean_311_data()