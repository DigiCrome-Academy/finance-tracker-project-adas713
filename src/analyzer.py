import numpy as np

class FinancialAnalyzer:
    def __init__(self, expenses: np.ndarray, incomes: np.ndarray, dates: np.ndarray = None):
        self.expenses = np.array(expenses, dtype=float)
        self.incomes = np.array(incomes, dtype=float)
        self.dates = np.array(dates) if dates is not None else None

    def calculate_moving_averages(self, window_size: int = 3):
        if window_size > len(self.expenses):
            raise ValueError("Window size cannot be greater than number of data points.")
        weights = np.ones(window_size) / window_size
        return np.convolve(self.expenses, weights, mode='valid')

    def analyze_spending_patterns(self):
        avg_expense = np.mean(self.expenses)
        std_expense = np.std(self.expenses)
        correlation = np.corrcoef(self.expenses, self.incomes)[0, 1] if len(self.expenses) == len(self.incomes) else None
        return {
            "mean_expense": avg_expense,
            "std_expense": std_expense,
            "expense_income_correlation": correlation
        }

    def project_future_balance(self, months_ahead: int = 6):
        if self.incomes is not None:
            balances = self.incomes - self.expenses
        else:
            balances = -self.expenses  

        cumulative = np.cumsum(balances)
        x = np.arange(len(cumulative))
        slope, intercept = np.polyfit(x, cumulative, 1)
        projected_balance = intercept + slope * (len(cumulative) + months_ahead - 1)
        return projected_balance


    def calculate_portfolio_metrics(self, returns: np.ndarray, risk_free_rate: float = 0.02):
        avg_return = np.mean(returns)
        volatility = np.std(returns)
        sharpe_ratio = (avg_return - risk_free_rate) / volatility if volatility != 0 else np.nan
        return {
            "average_return": avg_return,
            "volatility": volatility,
            "sharpe_ratio": sharpe_ratio
        }

    def optimize_budget_allocation(self, categories: list, budgets: np.ndarray, priorities: np.ndarray):
        priorities = np.array(priorities, dtype=float)
        budgets = np.array(budgets, dtype=float)
        allocation_ratios = priorities / np.sum(priorities)
        optimized_budget = allocation_ratios * np.sum(budgets)
        return dict(zip(categories, optimized_budget))


    def correlation_between_categories(self, category_expenses: np.ndarray):
        """
        Calculate correlation matrix between different spending categories.
        Each column in category_expenses is one category.
        """
        return np.corrcoef(category_expenses, rowvar=False)

    def spending_percentiles(self, q=[25, 50, 75]):
        """
        Calculate given percentiles for expenses.
        Defaults to quartiles.
        """
        return {f"{percent}th": np.percentile(self.expenses, percent) for percent in q}

    def detect_outliers(self, threshold: float = 1.5):
        """
        Detect outliers using IQR method.
        """
        q1 = np.percentile(self.expenses, 25)
        q3 = np.percentile(self.expenses, 75)
        iqr = q3 - q1
        lower_bound = q1 - threshold * iqr
        upper_bound = q3 + threshold * iqr
        outlier_mask = (self.expenses < lower_bound) | (self.expenses > upper_bound)
        return self.expenses[outlier_mask]

    def time_series_trend(self):
        """
        Fit a linear trend line to expenses over time.
        Returns slope and intercept.
        """
        if self.dates is None:
            raise ValueError("Dates are required for time-series analysis.")
        days = np.array([(d - self.dates[0]).days for d in self.dates])
        slope, intercept = np.polyfit(days, self.expenses, 1)
        return slope, intercept

    def recommend_budget_changes(self, category_expenses: np.ndarray, category_names: list, budget_limits: np.ndarray):
        """
        Recommend budget increases/decreases based on overspending.
        Positive recommendation = increase budget, negative = cut budget.
        """
        overspending = category_expenses - budget_limits
        return dict(zip(category_names, overspending))
