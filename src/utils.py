# src/utils.py

import time
import functools
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# -------------------------------------
# 1. Pure Functions (data cleaning & validation)
# -------------------------------------

def clean_whitespace(text: str) -> str:
    """Remove extra spaces and trim text."""
    return " ".join(text.strip().split())

def validate_positive_number(value: float) -> bool:
    """Check if a value is a positive number."""
    return isinstance(value, (int, float)) and value > 0

# -------------------------------------
# 2. Higher-order functions
# -------------------------------------

def apply_to_list(func, data_list):
    """Apply a function to all items in a list."""
    return [func(item) for item in data_list]

def conditional_apply(func, data_list, condition):
    """
    Apply func to items in data_list only if condition(item) is True.
    :param func: function to apply
    :param data_list: list of items
    :param condition: predicate function
    """
    return [func(item) if condition(item) else item for item in data_list]

# -------------------------------------
# 3. Decorators for logging, timing, error handling
# -------------------------------------

def log_call(func):
    """Log function calls and arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

def time_it(func):
    """Measure execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logging.info(f"{func.__name__} executed in {end - start:.4f}s")
        return result
    return wrapper

def handle_errors(func):
    """Catch and log exceptions."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {e}")
            return None
    return wrapper

# -------------------------------------
# 4. Functions with default params & *args, **kwargs
# -------------------------------------

@log_call
@time_it
@handle_errors
def flexible_sum(start=0, *args, **kwargs):
    """
    Sum numbers starting from `start`, including any values from kwargs.
    """
    total = start + sum(args)
    total += sum(v for v in kwargs.values() if isinstance(v, (int, float)))
    return total

# -------------------------------------
# 5. Lambda functions for data filtering
# -------------------------------------

filter_positive = lambda numbers: list(filter(lambda x: x > 0, numbers))
filter_by_threshold = lambda numbers, t: list(filter(lambda x: x >= t, numbers))

# -------------------------------------
# 6. Recursive functions for nested data
# -------------------------------------

def sum_nested_numbers(data):
    """
    Recursively sum all numeric values in a nested data structure
    (lists, tuples, dicts, sets).
    """
    total = 0
    if isinstance(data, (int, float)):
        return data
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            total += sum_nested_numbers(item)
    elif isinstance(data, dict):
        for value in data.values():
            total += sum_nested_numbers(value)
    return total
