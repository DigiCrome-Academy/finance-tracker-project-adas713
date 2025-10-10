import pandas as pd
import yaml
import json
from pathlib import Path

# Load params
params = yaml.safe_load(open("params.yaml"))["data_cleaning"]
min_amount = params["min_amount"]
date_format = params["date_format"]

# Load data
raw_path = Path("data/raw/transactions.csv")
df = pd.read_csv(raw_path)

# Data cleaning
df = df.dropna(subset=["date", "amount"])
df = df[df["amount"] >= min_amount]

# Validate date format
def validate_date(date_str):
    try:
        pd.to_datetime(date_str, format=date_format)
        return True
    except Exception:
        return False

df = df[df["date"].apply(validate_date)]

# Save cleaned data
processed_path = Path("data/processed/transactions_clean.csv")
processed_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(processed_path, index=False)

# Save metrics
metrics = {
    "rows_before": int(len(pd.read_csv(raw_path))),
    "rows_after": int(len(df)),
    "invalid_rows_removed": int(len(pd.read_csv(raw_path)) - len(df)),
}
Path("metrics").mkdir(exist_ok=True)
with open("metrics/data_quality.json", "w") as f:
    json.dump(metrics, f, indent=2)
