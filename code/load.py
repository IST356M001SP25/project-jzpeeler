import pandas as pd

def load_clean_data(filepath="cache/clean_311_data.csv"):
    df = pd.read_csv(filepath, parse_dates=["created_date"])
    return df


if __name__ == "__main__":
    df = load_clean_data()
    print(df.head())