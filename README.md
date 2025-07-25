[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/oOhdRy6d)
﻿# Personal Finance Tracker and Investment Portfolio Analyzer

## Project Overview
Build a comprehensive personal finance management system that tracks expenses, manages budgets, analyzes spending patterns, and provides investment portfolio insights. This project will test your Python fundamentals, data structures, NumPy operations, object-oriented programming, and modern ML engineering practices with DVC and Prefect.

## Learning Objectives
- Master Python data types and structures
- Implement custom classes and methods
- Utilize NumPy for numerical computations
- Work with functions and modules
- Implement data version control with DVC
- Create automated workflows with Prefect
- Practice file I/O and data persistence

## Project Structure
```
finance_tracker/
├── README.md
├── requirements.txt
├── .dvcignore
├── dvc.yaml
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
├── src/
│   ├── __init__.py
│   ├── data_types.py
│   ├── transaction.py
│   ├── portfolio.py
│   ├── analyzer.py
│   └── workflows.py
├── notebooks/
│   └── analysis.ipynb
├── tests/
│   └── test_classes.py
└── flows/
    └── prefect_pipeline.py
```

## Phase 1: Python Basics and Data Types

### Step 1.1: Environment Setup
**Instructions:**
- Create a new Python virtual environment
- Install required packages: numpy, pandas, matplotlib, dvc, prefect
- Initialize a Git repository
- Create the project directory structure as shown above
- Initialize DVC in your project (`dvc init`)

### Step 1.2: Basic Data Types Implementation
**File: `src/data_types.py`**

**Your Tasks:**
- Create a module that demonstrates all Python primitive data types
- Implement functions that work with integers, floats, strings, booleans
- Create a function that converts currency strings ("$1,234.56") to float values
- Implement a function that validates date strings in multiple formats
- Create utility functions for percentage calculations
- Add type hints to all functions
- Include docstrings following Google/NumPy style

### Step 1.3: Data Structures Implementation
**File: `src/data_structures.py`**

**Your Tasks:**
- Implement functions using lists to store transaction categories
- Use dictionaries to create category-to-budget mappings
- Utilize tuples for immutable transaction records
- Create sets for unique merchant names
- Implement nested data structures (list of dictionaries) for transaction history
- Create functions to manipulate each data structure type
- Add search and filtering capabilities using data structures

## Phase 2: Object-Oriented Programming 

### Step 2.1: Transaction Class
**File: `src/transaction.py`**

**Your Tasks:**
- Design a `Transaction` class with the following attributes:
  - transaction_id (string)
  - date (datetime object)
  - amount (float)
  - category (string)
  - merchant (string)
  - description (string)
  - account_type (string)
- Implement class methods:
  - `__init__` constructor with validation
  - `__str__` and `__repr__` methods
  - `to_dict()` method for serialization
  - `from_dict()` class method for deserialization
  - Property decorators for computed fields (e.g., month, year)
- Add validation methods for amount ranges and required fields
- Implement comparison methods (`__eq__`, `__lt__`, etc.) for sorting

### Step 2.2: Account Class
**File: `src/account.py`**

**Your Tasks:**
- Create an `Account` class with:
  - account_name, account_type, balance, transaction_list
- Implement methods:
  - `add_transaction()` 
  - `remove_transaction()`
  - `get_balance()`
  - `get_transactions_by_category()`
  - `get_monthly_summary()`
- Add inheritance: Create `CheckingAccount` and `SavingsAccount` subclasses
- Implement account-specific methods (e.g., overdraft protection)

### Step 2.3: Portfolio Class
**File: `src/portfolio.py`**

**Your Tasks:**
- Design an `InvestmentPortfolio` class containing:
  - portfolio_name, holdings (dictionary), cash_balance
- Create a nested `Holding` class for individual investments:
  - symbol, shares, purchase_price, current_price, purchase_date
- Implement portfolio methods:
  - `add_holding()`
  - `remove_holding()`
  - `update_prices()`
  - `calculate_total_value()`
  - `get_asset_allocation()`
- Add portfolio analytics methods using the Holding objects

## Phase 3: NumPy Integration 

### Step 3.1: Financial Calculations with NumPy
**File: `src/analyzer.py`**

**Your Tasks:**
- Create a `FinancialAnalyzer` class that uses NumPy arrays extensively
- Implement methods using NumPy:
  - `calculate_moving_averages()` - compute spending trends
  - `analyze_spending_patterns()` - statistical analysis of expenses
  - `project_future_balance()` - forecasting using linear regression
  - `calculate_portfolio_metrics()` - return, volatility, Sharpe ratio
  - `optimize_budget_allocation()` - budget optimization using NumPy
- Use NumPy functions: `np.mean()`, `np.std()`, `np.corrcoef()`, `np.polyfit()`
- Implement array operations for bulk calculations
- Create vectorized functions for performance optimization

### Step 3.2: Statistical Analysis
**Your Tasks:**
- Implement correlation analysis between different spending categories
- Calculate percentiles and quartiles for spending analysis
- Create functions for outlier detection using NumPy statistical functions
- Implement time-series analysis for expense trends
- Build a simple recommendation system using NumPy array operations

## Phase 4: Functions and Modules 

### Step 4.1: Utility Functions
**File: `src/utils.py`**

**Your Tasks:**
- Create pure functions for data cleaning and validation
- Implement higher-order functions (functions that take other functions as parameters)
- Create decorators for logging, timing, and error handling
- Implement functions with default parameters and *args, **kwargs
- Create lambda functions for data filtering operations
- Build recursive functions for nested data structure processing

### Step 4.2: Data Processing Pipeline
**File: `src/data_pipeline.py`**

**Your Tasks:**
- Create a functional programming approach to data processing
- Implement a chain of functions that transform raw transaction data
- Use map(), filter(), and reduce() operations
- Create custom exceptions and error handling functions
- Implement data validation pipeline using function composition
- Build automated data cleaning functions

## Phase 5: DVC Implementation 

### Step 5.1: Data Version Control Setup
**Your Tasks:**
- Create sample datasets in `data/raw/` directory:
  - `transactions.csv` (generate 1000+ sample transactions)
  - `market_data.csv` (stock price data)
  - `budget_data.json` (budget configurations)
- Configure DVC to track these datasets
- Create `dvc.yaml` pipeline file with the following stages:
  - data-cleaning: Clean and validate raw transaction data
  - feature-engineering: Create derived features from transactions
  - analysis: Generate spending insights and portfolio metrics
  - reporting: Create summary reports and visualizations

### Step 5.2: DVC Pipeline Configuration
**Your Tasks:**
- Define dependencies and outputs for each pipeline stage
- Set up parameters in `params.yaml` for configurable analysis
- Create metrics tracking in `dvc.yaml` for:
  - Data quality metrics
  - Portfolio performance metrics
  - Budget adherence scores
- Implement data validation checks in your pipeline stages
- Set up DVC remote storage (local or cloud)

### Step 5.3: Experiment Tracking
**Your Tasks:**
- Create different parameter sets for analysis experiments
- Run DVC experiments with different budget allocation strategies
- Track model performance metrics across different time periods
- Use DVC plots to visualize experiment results
- Document experiment insights and conclusions

## Phase 6: Prefect Workflows 

### Step 6.1: Basic Flow Creation
**File: `flows/basic_pipeline.py`**

**Your Tasks:**
- Create a Prefect flow for daily transaction processing
- Implement tasks for:
  - Data loading and validation
  - Transaction categorization
  - Balance calculations
  - Alert generation for budget overruns
- Add error handling and retry logic to tasks
- Implement conditional logic in your workflow
- Set up task dependencies and execution order

### Step 6.2: Advanced Workflow Features
**File: `flows/advanced_pipeline.py`**

**Your Tasks:**
- Create a complex workflow that combines multiple data sources
- Implement parallel task execution where appropriate
- Add caching for expensive computations
- Create conditional branches based on data quality checks
- Implement workflow that triggers on data changes
- Set up logging and monitoring for workflow execution

### Step 6.3: Scheduled Workflows
**Your Tasks:**
- Create a Prefect deployment for scheduled execution
- Set up weekly portfolio analysis workflow
- Implement monthly budget review workflow
- Create alerting system for significant portfolio changes
- Add workflow that backs up processed data
- Implement integration with external APIs (optional)

## Phase 7: Integration and Testing 

### Step 7.1: Unit Testing
**File: `tests/test_classes.py`**

**Your Tasks:**
- Write comprehensive unit tests for all classes
- Test edge cases and error conditions
- Create fixtures for test data
- Implement parameterized tests for multiple scenarios
- Test NumPy array operations and mathematical functions
- Create integration tests for class interactions

### Step 7.2: End-to-End Integration
**File: `src/main.py`**

**Your Tasks:**
- Create a main application that integrates all components
- Implement a command-line interface for user interaction
- Create a complete workflow from data loading to report generation
- Add configuration management for different environments
- Implement logging throughout the application
- Create comprehensive documentation for all modules

### Step 7.3: Performance Optimization
**Your Tasks:**
- Profile your application to identify bottlenecks
- Optimize NumPy operations for better performance
- Implement caching strategies where appropriate
- Optimize database/file I/O operations
- Create benchmarking tests for performance monitoring

## Deliverables Checklist

### Code Quality Requirements:
- [ ] All functions have type hints and docstrings
- [ ] Code follows PEP 8 style guidelines
- [ ] Error handling implemented throughout
- [ ] Logging configured and used appropriately
- [ ] Unit tests with >80% coverage

### Technical Implementation:
- [ ] At least 5 different data types used meaningfully
- [ ] 3+ data structures implemented and manipulated
- [ ] 10+ NumPy operations integrated
- [ ] 5+ custom classes with inheritance
- [ ] 15+ functions with various parameter types
- [ ] DVC pipeline with 4+ stages
- [ ] 3+ Prefect workflows implemented

### Documentation:
- [ ] Complete README with setup instructions
- [ ] Inline code documentation
- [ ] API documentation for all classes
- [ ] Usage examples and tutorials
- [ ] Architecture decision documentation

## Assessment Criteria

### Technical Proficiency (40%):
- Correct implementation of Python fundamentals
- Effective use of NumPy for numerical operations
- Proper object-oriented design principles
- Clean, readable, maintainable code

### Data Engineering (30%):
- Effective DVC pipeline implementation
- Proper workflow orchestration with Prefect
- Data validation and error handling
- Performance considerations

### Best Practices (30%):
- Code organization and modularity
- Testing coverage and quality
- Documentation completeness
- Git workflow and version control

## Bonus Challenges (Optional):
- Implement a web dashboard using Flask/FastAPI
- Add machine learning predictions for spending patterns
- Create Docker containerization
- Implement real-time data streaming
- Add integration with actual banking APIs (with security considerations)
- Create mobile app interface using Kivy or similar

## Getting Started
1. Fork this repository
2. Set up your development environment
3. Start with Phase 1, Step 1.1
4. Commit regularly with meaningful commit messages
5. Document your progress and challenges
6. Ask questions and seek clarification when needed

## Submission Guidelines
- Submit your complete project repository
- Include a demo video showing your application in action
- Provide a reflection document discussing challenges and learnings
- Present your project architecture and key technical decisions

Good luck with your comprehensive Python project! This will give you hands-on experience with all the fundamental concepts while building something practical and impressive for your portfolio.