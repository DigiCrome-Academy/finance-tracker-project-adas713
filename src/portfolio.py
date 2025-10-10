class InvestmentPortfolio:
    def __init__(self, portfolio_name):
        self.portfolio_name = portfolio_name
        self.holdings = {}
        self.cash_balance = 0

    class Holding:
        def __init__(self, symbol, shares, purchase_price, current_price, purchase_date):
            self.symbol = symbol
            self.shares = shares
            self.purchase_price = purchase_price
            self.current_price = current_price
            self.purchase_date = purchase_date
        
        def get_symbol(self):
            return self.symbol
        
        def market_value(self):
            return self.shares * self.current_price

    def add_holding(self, holding):
        self.holdings[holding.get_symbol()] = holding

    def remove_holding(self, holding):
        self.holdings.pop(holding.get_symbol())

    def update_prices(self, prices):
        for symbol, new_price in prices.items():
            if symbol in self.holdings:
                self.holdings[symbol].current_price = new_price

    def calculate_total_value(self):
        """Total portfolio value including cash."""
        holdings_value = sum(h.market_value() for h in self.holdings.values())
        return self.cash_balance + holdings_value

    def get_asset_allocation(self):
        """Percentage allocation by holding."""
        total_value = self.calculate_total_value()
        allocation = {}
        for symbol, h in self.holdings.items():
            allocation[symbol] = (h.market_value() / total_value) * 100
        if self.cash_balance > 0:
            allocation["CASH"] = (self.cash_balance / total_value) * 100
        return allocation
