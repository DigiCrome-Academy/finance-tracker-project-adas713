from datetime import datetime

class Transaction:
    def __init__(self, transaction_id: str, date:datetime, amount:float, category:str, merchant:str, description:str, account_type:str):
        self.transaction_id = transaction_id
        self.date = date
        self.amount = amount
        self.category = category
        self.merchant = merchant
        self.description = description
        self.account_type = account_type

    def __str__(self):
        return f"Transaction: {self.transaction_id} \nDate: {self.date} \nAmount:{self.amount}\nCategory:{self.category}\nMerchant:{self.merchant}\nDescription:{self.description}\nAccount Type:{self.account_type}"
    
    def __repr__(self):
        return f"Transaction({self.transaction_id}, {self.date}, {self.amount}, {self.category}, {self.merchant}, {self.description}, {self.account_type})"
    
    def to_dict(self) -> dict:
        return {"transaction_id": self.transaction_id,
                "date": self.date,
                "amount": self.amount,
                "category": self.category,
                "merchant": self.merchant,
                "description": self.description,
                "account_type": self.account_type}
    
    def from_dict(cls, data:dict):
        return cls(data["transaction_id"], data["date"], data["amount"], data["category"], data["merchant"], data["description"], data["account_type"])

    def get_category(self):
        return self.category
    
    def get_date(self):
        return self.date