# src/main.py

import argparse
import logging
import yaml
from pathlib import Path

# Import your finance project components
# Classes
from finance_core import Transaction, Account, Portfolio
# Prefect flows
from prefect_pipeline import basic_pipeline, advanced_pipeline, weekly_portfolio_flow, monthly_budget_flow

# ---------------------------
# Logging Setup
# ---------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# ---------------------------
# Configuration Management
# ---------------------------

def load_config(config_file="config.yaml"):
    """
    Load environment-specific configuration.
    """
    if not Path(config_file).exists():
        logger.warning(f"{config_file} not found. Using default settings.")
        return {
            "daily_transactions_file": "data/daily_transactions.csv",
            "budget_limit": 500,
            "sources": ["bank_csv", "credit_card_csv"],
        }
    with open(config_file, "r") as f:
        config = yaml.safe_load(f)
    return config

# ---------------------------
# CLI Implementation
# ---------------------------

def parse_args():
    parser = argparse.ArgumentParser(description="Personal Finance Management System")
    parser.add_argument("--run-basic", action="store_true", help="Run the basic daily transaction pipeline")
    parser.add_argument("--run-advanced", action="store_true", help="Run the advanced transaction pipeline")
    parser.add_argument("--run-weekly", action="store_true", help="Run weekly portfolio flow")
    parser.add_argument("--run-monthly", action="store_true", help="Run monthly budget review")
    parser.add_argument("--config", type=str, default="config.yaml", help="Path to config file")
    return parser.parse_args()

# ---------------------------
# Main Workflow
# ---------------------------

def main():
    args = parse_args()
    config = load_config(args.config)

    # Run basic pipeline
    if args.run_basic:
        logger.info("Running basic daily transaction pipeline...")
        basic_pipeline(file_path=config["daily_transactions_file"], budget_limit=config["budget_limit"])

    # Run advanced pipeline
    if args.run_advanced:
        logger.info("Running advanced transaction pipeline...")
        advanced_pipeline(sources=config["sources"], budget_limit=config["budget_limit"])

    # Run weekly portfolio flow
    if args.run_weekly:
        logger.info("Running weekly portfolio flow...")
        weekly_portfolio_flow()

    # Run monthly budget review flow
    if args.run_monthly:
        logger.info("Running monthly budget review flow...")
        monthly_budget_flow()

    # Generate simple report
    logger.info("Generating summary report...")
    # TODO: Replace with actual report generation
    report = f"Report generated on {config['daily_transactions_file']}"
    logger.info(report)

# ---------------------------
# Entry Point
# ---------------------------

if __name__ == "__main__":
    main()
