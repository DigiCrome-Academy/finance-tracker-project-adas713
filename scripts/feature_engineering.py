import pandas as pd
import yaml
from pathlib import Path

# Load params
params = yaml.safe_load(open("params.yaml"))["feature_engineering"]
window = params["moving_average_window"]

# Load cleaned data
df = pd.read_csv("data/processed/transactions_clean.csv")

# Example feature: rolling average of amounts
df["amount_ma"] = df["amount"].rolling(window=window, min_periods=1).mean()

# Save features
features_path = Path("data/features/transactions_features.csv")
features_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(features_path, index=False)
