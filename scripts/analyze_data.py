# analyze_data.py

import pandas as pd
import numpy as np
import yaml
import json
from pathlib import Path
from src.analyzer import FinancialAnalyzer

# ------------------------
# Load parameters
# ------------------------
params = yaml.safe_load(open("params.yaml"))
forecast_months = params["analysis"]["forecast_months"]
allocation_strategy = params["budget"]["allocation_strategy"]

# ------------------------
# Load data
# ------------------------
features = pd.read_csv("data/features/transactions_features.csv")
market = pd.read_csv("data/raw/market_data.csv")
with open("data/raw/budget_data.json") as f:
    budget_data = json.load(f)

# ------------------------
# Prepare FinancialAnalyzer
# ------------------------
expenses = features["amount"].to_numpy()
# If you have income data, replace zeros with actual values
incomes = np.zeros_like(expenses)
fa = FinancialAnalyzer(expenses=expenses, incomes=incomes)

# ------------------------
# Portfolio metrics
# ------------------------
portfolio_metrics = fa.calculate_portfolio_metrics(returns=expenses/1000)
portfolio_return = portfolio_metrics["average_return"]
risk = portfolio_metrics["volatility"]
sharpe_ratio = portfolio_metrics["sharpe_ratio"]

# ------------------------
# Budget adherence
# ------------------------
category_totals = features.groupby("category")["amount"].sum()
category_names = category_totals.index.tolist()
category_expenses = category_totals.to_numpy()

# Build budget limits array from budget_data
budget_limits = np.array([budget_data.get(cat, 0) for cat in category_names])

# Compute overspending / adherence using FinancialAnalyzer
adherence_dict = fa.recommend_budget_changes(category_expenses, category_names, budget_limits)

# Simple adherence score: % of categories within budget
within_budget = sum(1 for val in adherence_dict.values() if val <= 0)
adherence_score = within_budget / len(category_names) if category_names else 0

# ------------------------
# Save metrics
# ------------------------
Path("metrics").mkdir(exist_ok=True)
with open("metrics/portfolio_performance.json", "w") as f:
    json.dump({
        "expected_return": portfolio_return,
        "risk": risk,
        "sharpe_ratio": sharpe_ratio,
        "forecast_months": forecast_months
    }, f, indent=2)

with open("metrics/budget_adherence.json", "w") as f:
    json.dump({
        "allocation_strategy": allocation_strategy,
        "adherence_score": adherence_score,
        "category_adherence": adherence_dict
    }, f, indent=2)

# ------------------------
# Save insights JSON
# ------------------------
Path("data/analysis").mkdir(parents=True, exist_ok=True)
with open("data/analysis/insights.json", "w") as f:
    json.dump({
        "portfolio_return": portfolio_return,
        "risk": risk,
        "sharpe_ratio": sharpe_ratio,
        "allocation_strategy": allocation_strategy,
        "budget_adherence": adherence_dict
    }, f, indent=2)
