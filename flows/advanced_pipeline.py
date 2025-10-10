# flows/advanced_pipeline.py

from prefect import flow, task, get_run_logger
from prefect.tasks import task_input_hash
from datetime import timedelta
from prefect.futures import wait_for_all

# ---------------------------
# Task Definitions
# ---------------------------

@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(hours=1))
def load_transactions(source_name: str):
    """
    Load transactions from a given data source (with caching for expensive tasks).
    """
    logger = get_run_logger()
    logger.info(f"Loading transactions from {source_name}")
    # TODO: Replace with your actual data loading logic
    data = [
        {"amount": 100, "source": source_name, "description": "Sample transaction 1"},
        {"amount": 200, "source": source_name, "description": "Sample transaction 2"}
    ]
    return data

@task
def validate_data(transactions):
    """
    Validate transactions for data quality.
    """
    logger = get_run_logger()
    logger.info(f"Validating {len(transactions)} transactions")
    is_valid = all("amount" in t for t in transactions)
    return is_valid, transactions

@task
def categorize_transactions(transactions):
    """
    Categorize transactions.
    """
    for t in transactions:
        t["category"] = "uncategorized"  # TODO: Replace with your categorization logic
    return transactions

@task
def calculate_balance(transactions):
    """
    Calculate the total balance from transactions.
    """
    balance = sum(t.get("amount", 0) for t in transactions)
    return balance

@task
def alert_budget_overrun(balance, budget_limit=1000):
    """
    Alert if total balance exceeds budget.
    """
    if balance > budget_limit:
        logger = get_run_logger()
        logger.warning(f"⚠️ Budget overrun! Total balance: {balance}")

# ---------------------------
# Flow Definition
# ---------------------------

@flow(name="advanced_transaction_pipeline")
def advanced_pipeline(sources: list[str], budget_limit: float = 1000):
    """
    Advanced workflow for daily transactions:
    - Loads multiple data sources in parallel
    - Validates and categorizes transactions
    - Calculates balances
    - Sends alerts for budget overruns
    """
    # 1️⃣ Parallel load of multiple sources
    futures = [load_transactions.submit(src) for src in sources]
    all_transactions = wait_for_all(futures)
    
    total_balance = 0
    
    for transactions in all_transactions:
        is_valid, transactions = validate_data(transactions)
        
        # Conditional branch based on data quality
        if not is_valid:
            print("Data quality check failed! Skipping this batch.")
            continue
        
        categorized = categorize_transactions(transactions)
        balance = calculate_balance(categorized)
        total_balance += balance

    # Alert if over budget
    if total_balance > budget_limit:
        alert_budget_overrun(total_balance, budget_limit)
    
    print(f"Advanced flow completed. Total balance: {total_balance}")

# ---------------------------
# Run the flow directly
# ---------------------------

if __name__ == "__main__":
    sources = ["bank_csv", "credit_card_csv", "wallet_csv"]
    advanced_pipeline(sources=sources, budget_limit=500)
