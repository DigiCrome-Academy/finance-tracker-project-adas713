# tests/test_classes.py

import pytest
import numpy as np

# Import your project classes here
# from finance_core import Transaction, Account, Portfolio

# ---------------------------
# Fixtures for test data
# ---------------------------

@pytest.fixture
def sample_transactions():
    return [
        {"amount": 100, "category": "groceries"},
        {"amount": 200, "category": "utilities"},
        {"amount": -50, "category": "refund"}
    ]

@pytest.fixture
def account_with_transactions(sample_transactions):
    # Example Account class with transactions
    acc = Account("Checking")
    for t in sample_transactions:
        acc.add_transaction(Transaction(**t))
    return acc

# ---------------------------
# Unit Tests for Transaction class
# ---------------------------

def test_transaction_creation():
    t = Transaction(amount=100, category="groceries")
    assert t.amount == 100
    assert t.category == "groceries"

def test_transaction_negative_amount():
    t = Transaction(amount=-50, category="refund")
    assert t.amount < 0

def test_transaction_invalid_amount():
    with pytest.raises(ValueError):
        Transaction(amount="invalid", category="error")  # invalid type

# ---------------------------
# Unit Tests for Account class
# ---------------------------

def test_account_add_transaction(account_with_transactions):
    acc = account_with_transactions
    assert len(acc.transactions) == 3
    assert sum(t.amount for t in acc.transactions) == 250

@pytest.mark.parametrize("amount,expected_balance", [
    (100, 100),
    (200, 200),
    (-50, -50),
])
def test_account_balance_calculation(amount, expected_balance):
    acc = Account("Test")
    acc.add_transaction(Transaction(amount=amount, category="test"))
    assert acc.get_balance() == expected_balance

def test_account_empty_transactions():
    acc = Account("Empty")
    assert acc.get_balance() == 0

# ---------------------------
# Unit Tests for NumPy operations
# ---------------------------

def test_numpy_array_operations():
    arr = np.array([1, 2, 3, 4])
    assert np.sum(arr) == 10
    assert np.mean(arr) == 2.5
    assert np.all(arr > 0)

# ---------------------------
# Integration Tests
# ---------------------------

def test_portfolio_account_integration(sample_transactions):
    port = Portfolio("My Portfolio")
    acc = Account("Checking")
    for t in sample_transactions:
        acc.add_transaction(Transaction(**t))
    port.add_account(acc)
    
    # Total portfolio balance should match account balance
    assert port.get_total_balance() == acc.get_balance()
    
    # Add another account
    acc2 = Account("Savings")
    acc2.add_transaction(Transaction(amount=500, category="salary"))
    port.add_account(acc2)
    
    assert port.get_total_balance() == acc.get_balance() + acc2.get_balance()
