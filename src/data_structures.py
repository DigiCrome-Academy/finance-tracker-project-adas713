trans_categories = []
category_to_budget = {}
transaction_records = [] #list of tuples
merchant_names = set()
transaction_history =[]  #list of dictionaries

def get_categories():
    return trans_categories

def add_category(cat):
    trans_categories.append(cat)

def remove_category(cat):
    if cat in trans_categories:
        trans_categories.remove(cat)

def get_budget(cat):
    return category_to_budget[cat]

def add_record(rec):
    transaction_records.append(rec)

def get_records():
    return transaction_records

def get_merchants():
    return merchant_names

def merchant_exists(name):
    return name in merchant_names

def add_transaction(t_id, cat, amount, merchant):
    trans = {
        "id": t_id,
        "category": cat,
        "amount": amount,
        "merchant": merchant
    }
    transaction_history.append(trans)
    merchant_names.add(merchant)

def get_transaction_history():
    return transaction_history

def filter_by_category(cat):
    return [txn for txn in transaction_history if txn["category"] == cat]

def filter_by_merchant(name):
    return [txn for txn in transaction_history if txn["merchant"] == name]

def filter_by_amount(min_amt=None, max_amt=None):
    return [
        txn for txn in transaction_history
        if (min_amt is None or txn["amount"] >= min_amt) and
           (max_amt is None or txn["amount"] <= max_amt)
    ]