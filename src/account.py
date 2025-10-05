from data_structures import get_categories
from datetime import datetime, timedelta

class Account:
    def __init__(self, account_name, account_type):
        self.account_name = account_name
        self.account_type = account_type
        self.balance = 0
        self.transaction_list = []

    def add_transaction(self, transaction):
        self.transaction_list.append(transaction)
    
    def remove_transaction(self, t_id):
        for t in self.transaction_list:
            if t.transaction_id == t_id:
                self.transaction_list.remove(t)
                break

    def get_balance(self):
        return self.balance
    
    def get_transactions_by_category(self):
        trans_dict = {}
        categories = get_categories()

        for c in categories:
            trans_dict[c] = ()

        for t in self.transaction_list:
            cat = t.get_category()
            trans_dict[cat].append(t)
        
        return trans_dict
    
    def get_monthly_summary(self):
        summary = []

        now = datetime.now()
        one_month = now - timedelta(days=30)
        for t in self.transaction_list:
            this_date = t.get_date()
            if one_month <= this_date <= now:
                summary.append(t)

        return summary
    
class CheckingAccount(Account):
    def __init__(self, account_name, account_type):
        super().__init__(account_name, account_type)

class SavingsAccount(Account):
    def __init__(self, account_name, account_type):
        super().__init__(account_name, account_type)
        