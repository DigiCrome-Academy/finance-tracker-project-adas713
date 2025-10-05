import pandas as pd
import yaml
import json
from pathlib import Path

# Load params
params = yaml.safe_load(open("params.yaml"))
forecast_months = params["analysis"]["forecast_months"]
allocation_strategy = params["budget"]["allocation_strategy"]

# Load data
features = pd.read_csv("data/features/transactions_features.csv")
market = pd.read_csv("data/raw/market_data.csv")
#budget = pd.read_json("data/raw/budget_data.json")


with open("data/raw/budget_data.json") as f:
    budget = json.load(f)

# --- Portfolio analysis placeholder ---
# In real use, replace with portfolio calculations
portfolio_return = features["amount"].mean() / 1000
risk = features["amount"].std() / 100

if allocation_strategy == "equal":
    adherence = 0.9
elif allocation_strategy == "high_risk":
    adherence = 0.7
else:  # low_risk
    adherence = 0.95

# Save portfolio performance metrics
Path("metrics").mkdir(exist_ok=True)
with open("metrics/portfolio_performance.json", "w") as f:
    json.dump({
        "expected_return": portfolio_return,
        "risk": risk,
        "forecast_months": forecast_months
    }, f, indent=2)

# Save budget adherence metrics
with open("metrics/budget_adherence.json", "w") as f:
    json.dump({
        "allocation_strategy": allocation_strategy,
        "adherence_score": adherence
    }, f, indent=2)

# Save insights JSON
Path("data/analysis").mkdir(parents=True, exist_ok=True)
with open("data/analysis/insights.json", "w") as f:
    json.dump({
        "portfolio_return": portfolio_return,
        "risk": risk,
        "allocation_strategy": allocation_strategy
    }, f, indent=2)
