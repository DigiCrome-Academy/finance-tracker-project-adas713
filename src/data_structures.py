trans_categories = []
category_to_budget = {}
transaction_records = [] #list of tuples
merchant_names = set()
transaction_history =[]  #list of dictionaries

def get_categories():
    return trans_categories

def add_category(cat):
    trans_categories.append(cat)

def get_budget(cat):
    return category_to_budget[cat]

def add_record(rec):
    transaction_records.append(rec)