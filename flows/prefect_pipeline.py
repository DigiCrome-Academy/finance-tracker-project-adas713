# prefect_pipeline.py

from prefect import flow, task, get_run_logger
from prefect.tasks import task_input_hash
from prefect.futures import wait_for_all
from prefect.deployments import DeploymentSpec
from prefect.orion.schemas.schedules import CronSchedule
from datetime import timedelta
import shutil
import os

# ---------------------------
# Phase 6.1: Basic Flow Tasks
# ---------------------------

@task(retries=3, retry_delay_seconds=10)
def load_and_validate_data(file_path: str):
    logger = get_run_logger()
    logger.info(f"Loading data from {file_path}")
    transactions = [{"amount": 100}, {"amount": 200}]
    if not transactions:
        raise ValueError("No transactions found!")
    return transactions

@task
def categorize_transactions(transactions):
    for t in transactions:
        t["category"] = "uncategorized"
    return transactions

@task
def calculate_balances(transactions):
    return sum(t.get("amount", 0) for t in transactions)

@task
def alert_budget_overrun(balance, budget_limit=1000):
    if balance > budget_limit:
        logger = get_run_logger()
        logger.warning(f"⚠️ Budget overrun! Balance: {balance}")

@flow(name="daily_transaction_pipeline")
def basic_pipeline(file_path: str, budget_limit: float = 1000):
    transactions = load_and_validate_data(file_path)
    categorized = categorize_transactions(transactions)
    balance = calculate_balances(categorized)
    if balance > budget_limit:
        alert_budget_overrun(balance, budget_limit)
    print(f"Flow completed. Final balance: {balance}")


# ---------------------------
# Phase 6.2: Advanced Flow Tasks
# ---------------------------

@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(hours=1))
def load_transactions(source_name: str):
    logger = get_run_logger()
    logger.info(f"Loading transactions from {source_name}")
    return [{"amount": 100, "source": source_name}, {"amount": 200, "source": source_name}]

@task
def validate_data(transactions):
    logger = get_run_logger()
    logger.info(f"Validating {len(transactions)} transactions")
    return all("amount" in t for t in transactions), transactions

@flow(name="advanced_transaction_pipeline")
def advanced_pipeline(sources: list[str], budget_limit: float = 1000):
    futures = [load_transactions.submit(src) for src in sources]
    all_transactions = wait_for_all(futures)
    total_balance = 0
    for transactions in all_transactions:
        is_valid, transactions = validate_data(transactions)
        if not is_valid:
            print("Data quality check failed! Skipping this batch.")
            continue
        categorized = categorize_transactions(transactions)
        balance = calculate_balances(categorized)
        total_balance += balance
    if total_balance > budget_limit:
        alert_budget_overrun(total_balance, budget_limit)
    print(f"Advanced flow completed. Total balance: {total_balance}")


# ---------------------------
# Phase 6.3: Scheduled Workflows
# ---------------------------

@task
def portfolio_analysis():
    logger = get_run_logger()
    logger.info("Running weekly portfolio analysis...")
    return 10000

@task
def budget_review():
    logger = get_run_logger()
    logger.info("Running monthly budget review...")
    return "On track"

@task
def alert_portfolio_change(current_value, previous_value, threshold=0.05):
    logger = get_run_logger()
    change = abs(current_value - previous_value) / previous_value
    if change > threshold:
        logger.warning(f"Significant portfolio change detected: {change*100:.2f}%")

@task
def backup_data(source_path: str, backup_path: str):
    logger = get_run_logger()
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)
    shutil.copy(source_path, backup_path)
    logger.info(f"Backed up {source_path} to {backup_path}")

@flow(name="weekly_portfolio_flow")
def weekly_portfolio_flow(previous_value: float = 9500):
    current_value = portfolio_analysis()
    alert_portfolio_change(current_value, previous_value)

@flow(name="monthly_budget_flow")
def monthly_budget_flow():
    budget_status = budget_review()
    backup_data("data/budget.csv", "backups/")

# ---------------------------
# Prefect Deployment Specs
# ---------------------------

DeploymentSpec(
    flow=weekly_portfolio_flow,
    name="weekly_portfolio_deployment",
    schedule=CronSchedule(cron="0 9 * * MON", timezone="UTC"),
    tags=["weekly", "portfolio"]
)

DeploymentSpec(
    flow=monthly_budget_flow,
    name="monthly_budget_deployment",
    schedule=CronSchedule(cron="0 10 1 * *", timezone="UTC"),
    tags=["monthly", "budget"]
)

# ---------------------------
# Run Locally for Testing
# ---------------------------

if __name__ == "__main__":
    basic_pipeline(file_path="data/daily_transactions.csv", budget_limit=500)
    advanced_pipeline(sources=["bank_csv", "credit_card_csv"], budget_limit=500)
    weekly_portfolio_flow()
    monthly_budget_flow()
