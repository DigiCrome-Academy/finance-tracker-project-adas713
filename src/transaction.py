from datetime import datetime

class Transaction:
    def __init__(self, transaction_id: str, date:datetime, amount:float, category:str, merchant:str, description:str, account_type:str):
        self._validate_required("transaction_id", transaction_id)
        self._validate_required("category", category)
        self._validate_required("merchant", merchant)
        self._validate_required("account_type", account_type)
        self._validate_amount(amount)
        self._validate_date(date)
        
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

    @property
    def month(self) -> int:
        return self.date.month

    @property
    def year(self) -> int:
        return self.date.year

    def get_category(self):
        return self.category
    
    def get_date(self):
        return self.date
    
    def __eq__(self, other):
        if not isinstance(other, Transaction):
            return NotImplemented
        return self.transaction_id == other.transaction_id

    def __lt__(self, other):
        if not isinstance(other, Transaction):
            return NotImplemented
        return self.date < other.date

    def __gt__(self, other):
        if not isinstance(other, Transaction):
            return NotImplemented
        return self.date > other.date


    def _validate_amount(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        if amount < 0:
            raise ValueError("Amount must be non-negative")

    def _validate_date(self, date):
        if not isinstance(date, datetime):
            raise TypeError("Date must be a datetime object")

    def _validate_required(self, field_name, value):
        if not value:
            raise ValueError(f"{field_name} is required")