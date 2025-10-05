# src/data_pipeline.py

from functools import reduce
import re
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# -------------------------------------
# 1. Custom Exceptions
# -------------------------------------

class DataValidationError(Exception):
    """Raised when transaction data fails validation."""
    pass

class DataCleaningError(Exception):
    """Raised when transaction data cleaning fails."""
    pass

# -------------------------------------
# 2. Core Functional Helpers
# -------------------------------------

def compose(*functions):
    """
    Compose multiple functions into a single transformation pipeline.
    compose(f, g, h)(x) = f(g(h(x)))
    """
    def composed_func(data):
        for func in reversed(functions):
            data = func(data)
        return data
    return composed_func

# -------------------------------------
# 3. Validation Functions
# -------------------------------------

def validate_transaction_structure(transaction):
    """Check that transaction has required keys."""
    required_keys = {"id", "amount", "category", "date"}
    if not required_keys.issubset(transaction.keys()):
        raise DataValidationError(f"Missing keys in transaction: {transaction}")
    return transaction

def validate_amount_positive(transaction):
    """Ensure transaction amount is positive."""
    if transaction["amount"] <= 0:
        raise DataValidationError(f"Invalid amount in transaction: {transaction}")
    return transaction

def validate_date_format(transaction):
    """Ensure date is in YYYY-MM-DD format."""
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", transaction["date"]):
        raise DataValidationError(f"Invalid date format: {transaction}")
    return transaction

# -------------------------------------
# 4. Cleaning Functions
# -------------------------------------

def clean_category_whitespace(transaction):
    """Trim extra spaces from category name."""
    transaction["category"] = transaction["category"].strip()
    return transaction

def clean_amount_round(transaction):
    """Round amount to 2 decimal places."""
    transaction["amount"] = round(float(transaction["amount"]), 2)
    return transaction

# -------------------------------------
# 5. Pipeline Implementation
# -------------------------------------

def process_transactions(transactions):
    """
    Functional pipeline:
    - validate structure
    - clean data
    - filter valid transactions
    - map to processed transactions
    - reduce to total spending
    """
    try:
        # Validation pipeline using composition
        validate_pipeline = compose(
            validate_date_format,
            validate_amount_positive,
            validate_transaction_structure
        )

        # Cleaning pipeline using composition
        cleaning_pipeline = compose(
            clean_category_whitespace,
            clean_amount_round
        )

        # Step 1: Validate and clean
        validated_cleaned = map(lambda t: cleaning_pipeline(validate_pipeline(t)), transactions)

        # Step 2: Filter (example: remove transactions below $1)
        filtered = filter(lambda t: t["amount"] >= 1.0, validated_cleaned)

        # Step 3: Reduce to total spending
        total_spending = reduce(lambda acc, t: acc + t["amount"], filtered, 0.0)

        return total_spending

    except (DataValidationError, DataCleaningError) as e:
        logging.error(f"Processing error: {e}")
        return None
