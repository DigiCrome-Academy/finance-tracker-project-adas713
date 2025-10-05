# scripts/generate_sample_data.py
import pandas as pd
import numpy as np
import json
from datetime import datetime, timedelta
import os

# Ensure directories exist
os.makedirs("data/raw", exist_ok=True)

# 1. transactions.csv — 1000+ sample transactions
np.random.seed(42)
categories = ["Food", "Transport", "Entertainment", "Bills", "Shopping", "Healthcare"]
start_date = datetime(2023, 1, 1)

transactions = []
for i in range(1200):
    date = start_date + timedelta(days=np.random.randint(0, 365))
    transactions.append({
        "id": i + 1,
        "amount": round(np.random.uniform(5, 500), 2),
        "category": np.random.choice(categories),
        "date": date.strftime("%Y-%m-%d")
    })

pd.DataFrame(transactions).to_csv("data/raw/transactions.csv", index=False)

# 2. market_data.csv — stock price data
tickers = ["AAPL", "GOOG", "TSLA", "MSFT", "AMZN"]
market_data = []
for ticker in tickers:
    for day in range(365):
        date = start_date + timedelta(days=day)
        market_data.append({
            "ticker": ticker,
            "date": date.strftime("%Y-%m-%d"),
            "close": round(np.random.uniform(100, 500), 2)
        })

pd.DataFrame(market_data).to_csv("data/raw/market_data.csv", index=False)

# 3. budget_data.json — budget configurations
budget_data = {
    "Food": 500,
    "Transport": 200,
    "Entertainment": 300,
    "Bills": 400,
    "Shopping": 250,
    "Healthcare": 150
}

with open("data/raw/budget_data.json", "w") as f:
    json.dump(budget_data, f, indent=4)

print("Sample datasets created in data/raw/")
