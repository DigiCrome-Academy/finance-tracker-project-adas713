# flows/basic_pipeline.py

from prefect import flow, task

# ---------------------------
# Task Definitions
# ---------------------------

@task(retries=3, retry_delay_seconds=10)
def load_and_validate_data(file_path: str):
    """
    Load daily transaction data and validate.
    """
    try:
        print(f"Loading data from {file_path}")
        # TODO: Replace with your actual data loading logic
        transactions = [
            {"amount": 100, "description": "Groceries"},
            {"amount": 200, "description": "Utilities"},
            {"amount": -50, "description": "Refund"}
        ]
        if not transactions:
            raise ValueError("No transactions found!")
        return transactions
    except Exception as e:
        print(f"Error loading data: {e}")
        raise

@task
def categorize_transactions(transactions):
    """
    Categorize transactions into budget categories.
    """
    # TODO: Replace with your actual categorization logic
    for t in transactions:
        t["category"] = "uncategorized"
    return transactions

@task
def calculate_balances(transactions):
    """
    Calculate total balance from transactions.
    """
    balance = 0
    for t in transactions:
        balance += t.get("amount", 0)
    return balance

@task
def alert_budget_overrun(balance, budget_limit=1000):
    """
    Generate alert if balance exceeds budget.
    """
    if balance > budget_limit:
        print(f"⚠️ Budget overrun! Current balance: {balance}")
        # TODO: Add actual alert mechanism (email, Slack, etc.)

# ---------------------------
# Flow Definition
# ---------------------------

@flow(name="daily_transaction_pipeline")
def basic_pipeline(file_path: str, budget_limit: float = 1000):
    """
    Prefect flow to process daily transactions.
    """
    # Task Execution
    transactions = load_and_validate_data(file_path)
    categorized = categorize_transactions(transactions)
    balance = calculate_balances(categorized)
    
    # Conditional logic
    if balance > budget_limit:
        alert_budget_overrun(balance, budget_limit)
    
    print(f"Flow completed. Final balance: {balance}")

# ---------------------------
# Run the flow directly
# ---------------------------

if __name__ == "__main__":
    basic_pipeline(file_path="data/daily_transactions.csv", budget_limit=500)
