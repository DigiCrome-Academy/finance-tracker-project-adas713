from data_structures import get_categories
from datetime import datetime, timedelta

class Account:
    def __init__(self, account_name, account_type):
        self.account_name = account_name
        self.account_type = account_type
        self.balance = 0
        self.transaction_list = []

    def add_transaction(self, transaction):
        """Add a transaction and update balance."""
        self.transaction_list.append(transaction)
        self.balance += transaction.amount

    def remove_transaction(self, t_id):
        """Remove transaction by ID and adjust balance."""
        for t in self.transaction_list:
            if t.transaction_id == t_id:
                self.transaction_list.remove(t)
                self.balance -= t.amount
                break

    def get_balance(self):
        return self.balance
    
    def get_transactions_by_category(self):
        """Return dict: category -> list of transactions."""
        trans_dict = {}
        categories = get_categories()

        for c in categories:
            trans_dict[c] = []

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
    def __init__(self, account_name, overdraft_limit=0.0):
        super().__init__(account_name, "Checking")
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """Withdraw with overdraft protection."""
        if self.balance - amount < -self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded")
        self.balance -= amount
        return self.balance


class SavingsAccount(Account):
    def __init__(self, account_name, interest_rate=0.01):
        super().__init__(account_name, "Savings")
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Apply interest to balance."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest        