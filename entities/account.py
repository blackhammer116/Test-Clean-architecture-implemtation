class Account:
    """
    Account entity class
    Methods:
    - deposit: Deposit money into account
    - withdraw: Withdraw money from account
    """
    def __init__(self, account_id: str, balance: float):
        self.account_id = account_id
        self.balance = balance
    
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")
        self.balance += amount
    
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than 0")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
